from pathlib import Path
import math
import shutil
import subprocess

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

SRC = Path("pages/solutions")
DST = Path("pages/solutions-bb")

# Copy every baseline file from solutions without deleting instructor files
# that have already been added to solutions-bb.
shutil.copytree(SRC, DST, dirs_exist_ok=True)

# ---------------------------------------------------------------------
# 02 Colab: generate all repository artifacts required by the exercise.
# ---------------------------------------------------------------------
p = DST / "02_sol_colab"
p.mkdir(parents=True, exist_ok=True)

k = np.arange(1, 21)
fig = plt.figure(figsize=(6, 4))
plt.plot(k, k**2, marker="o")
plt.xlabel("k")
plt.ylabel(r"$k^2$")
plt.title(r"Wykres $y=k^2$")
plt.grid(alpha=0.3)
plt.tight_layout()
fig.savefig(p / "wykres.png", dpi=150)
plt.close(fig)

t = np.linspace(0, 6*np.pi, 600)
x = (1 + 0.35*np.cos(5*t))*np.cos(t)
y = (1 + 0.35*np.cos(5*t))*np.sin(t)
z = 0.35*np.sin(5*t)
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")
ax.plot(x, y, z, label="Modified parametric curve")
ax.set_title("3D Parametric Curve")
ax.set_xlabel("x(t)")
ax.set_ylabel("y(t)")
ax.set_zlabel("z(t)")
ax.legend()
plt.tight_layout()
fig.savefig(p / "parametric_curve.png", dpi=150)
plt.close(fig)

# Animated pendulum GIF. The MP4 is intentionally not committed, in
# accordance with the exercise instructions.
frames = []
W, H = 480, 340
pivot = (W//2, 60)
L = 175
for i in range(42):
    tau = 2*math.pi*i/42
    theta = 0.65*math.cos(tau)
    bx = int(pivot[0] + L*math.sin(theta))
    by = int(pivot[1] + L*math.cos(theta))
    im = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(im)
    d.line([pivot, (bx, by)], fill="black", width=4)
    d.ellipse([pivot[0]-6, pivot[1]-6, pivot[0]+6, pivot[1]+6], fill="black")
    d.ellipse([bx-18, by-18, bx+18, by+18], outline="black", width=3)
    d.text((14, 14), "Animacja wahadla", fill="black")
    frames.append(im)
frames[0].save(
    p / "video.gif",
    save_all=True,
    append_images=frames[1:],
    duration=70,
    loop=0,
    optimize=True,
)
mp4 = p / "video.mp4"
if mp4.exists():
    mp4.unlink()

# ---------------------------------------------------------------------
# 03 GitHub/Codespaces: exact PDF merge and Pandoc exports.
# ---------------------------------------------------------------------
p = DST / "03_sol_github"
subprocess.run(["python", "merge_pngs.py"], cwd=p, check=True)

subprocess.run(["pandoc", "document.md", "-o", "document.docx"], cwd=p, check=True)
subprocess.run(
    [
        "pandoc",
        "document.md",
        "--standalone",
        "--pdf-engine=weasyprint",
        "-o",
        "document.pdf",
    ],
    cwd=p,
    check=True,
)

# Keep a small reusable export helper for the instructor.
export_sh = p / "export_document.sh"
export_sh.write_text(
    '#!/usr/bin/env bash\n'
    'set -e\n'
    'cd "$(dirname "$0")"\n'
    'pandoc document.md -o document.docx\n'
    'pandoc document.md --standalone --pdf-engine=weasyprint -o document.pdf\n',
    encoding="utf-8",
)

# ---------------------------------------------------------------------
# 04 VS Code: generate the plots referenced by raport.md.
# ---------------------------------------------------------------------
p = DST / "04_sol_vscode"
subprocess.run(["python", "generuj_wykresy.py"], cwd=p, check=True)

print("solutions-bb built successfully")
