from pathlib import Path
from PIL import Image

src = Path(__file__).parent / "merge"
files = sorted(src.glob("*.png"), key=lambda p: p.name)
images = []
for path in files:
    im = Image.open(path).convert("RGB")
    images.append(im)

if not images:
    raise SystemExit("Brak plików PNG w folderze merge")

out = Path(__file__).parent / "ikonografiki.pdf"
images[0].save(out, save_all=True, append_images=images[1:], resolution=150.0)
print("Zapisano", out)
