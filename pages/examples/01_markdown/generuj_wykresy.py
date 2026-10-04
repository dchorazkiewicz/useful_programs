# -*- coding: utf-8 -*-
"""Wykresy do raportu o ciele na sprężynie.

Uruchom z katalogu pages/create: python generuj_wykresy.py
Kod odpowiada czterem blokom Python zamieszczonym w raporcie.
"""

# Blok A
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.integrate import solve_ivp

OUT = Path("files/sprezyna")
OUT.mkdir(parents=True, exist_ok=True)
BLUE, ORANGE, GREEN = "#2463A6", "#D47722", "#168578"
PURPLE, INK = "#8455A4", "#233044"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.titlesize": 13, "axes.titleweight": "bold",
    "axes.labelcolor": INK, "text.color": INK,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.18,
    "lines.linewidth": 2.3, "figure.facecolor": "white",
    "savefig.facecolor": "white",
})

m, k = 0.50, 20.0
x0, v0 = 0.10, 0.0
w0 = np.sqrt(k / m)
T = 2 * np.pi / w0
A = np.hypot(x0, v0 / w0)

def zapisz(fig, nazwa):
    fig.savefig(OUT / f"{nazwa}.png", dpi=180)
    if plt.get_backend().lower() != "agg":
        plt.show()
    plt.close(fig)

print(f"omega_0 = {w0:.6f} rad/s; T = {T:.6f} s")
print(f"f = {1/T:.6f} Hz; E = {0.5*k*A**2:.6f} J")

fig, ax = plt.subplots(figsize=(10, 3.4), layout="constrained")
ax.set(xlim=(-0.5, 7.0), ylim=(-0.6, 2.2))
ax.axis("off")
ax.add_patch(Rectangle((0, 0.3), 0.22, 1.25,
                       facecolor="#CBD5E1", hatch="///", edgecolor=INK))
ax.plot([0.2, 6.6], [0.3, 0.3], color=INK, lw=1.4)
sx = np.linspace(0.55, 4.25, 500)
ax.plot([0.22, 0.55], [0.95, 0.95], color=BLUE)
ax.plot(sx, 0.95 + 0.20*np.sin(np.linspace(0, 18*np.pi, 500)), color=BLUE)
ax.plot([4.25, 4.6], [0.95, 0.95], color=BLUE)
ax.add_patch(Rectangle((4.6, 0.3), 1.1, 1.3,
                       facecolor="#E3EEF9", edgecolor=BLUE, lw=2))
ax.text(5.15, 0.95, "$m$", ha="center", va="center", fontsize=22)
ax.text(2.3, 1.45, "sprężyna o stałej $k$", ha="center")
ax.plot([3.9, 3.9], [0.1, 1.65], "--", color="#64748B", lw=1.2)
ax.annotate("", xy=(5.15, -0.13), xytext=(3.9, -0.13),
            arrowprops={"arrowstyle": "<->", "color": INK})
ax.text(4.52, -0.42, "$x>0$", ha="center")
ax.text(3.9, 1.85, "równowaga: $x=0$", ha="center")
ax.annotate("", xy=(4.0, 1.7), xytext=(5.7, 1.7),
            arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 2.5})
ax.text(5.3, 1.98, "$F_s=-kx$", color=ORANGE, ha="center")
ax.set_title("Model: masa na poziomej sprężynie", loc="left")
zapisz(fig, "schemat")

# Blok B
t = np.linspace(0, 3*T, 1801)
x = x0*np.cos(w0*t) + (v0/w0)*np.sin(w0*t)
v = -x0*w0*np.sin(w0*t) + v0*np.cos(w0*t)
a = -w0**2*x
Ep, Ek = 0.5*k*x**2, 0.5*m*v**2

fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True,
                         layout="constrained")
for ax, y, label, color in zip(
    axes, [x, v, a], ["x [m]", "v [m/s]", "a [m/s²]"],
    [BLUE, ORANGE, PURPLE]
):
    ax.plot(t, y, color=color)
    ax.set_ylabel(label)
    ax.axhline(0, color=INK, lw=0.7, alpha=0.5)
    for n in range(1, 4):
        ax.axvline(n*T, color=INK, ls=":", lw=0.9, alpha=0.4)
axes[0].set_title("Ruch idealny: trzy okresy drgań", loc="left")
axes[-1].set_xlabel("Czas t [s]")
zapisz(fig, "polozenie_predkosc_przyspieszenie")

fig, ax = plt.subplots(figsize=(10, 4.2), layout="constrained")
ax.plot(t, Ep, color=BLUE, label="Potencjalna")
ax.plot(t, Ek, color=ORANGE, label="Kinetyczna")
ax.plot(t, Ep+Ek, color=GREEN, ls="--", label="Całkowita")
ax.set(xlabel="Czas t [s]", ylabel="Energia [J]", ylim=(-0.005, 0.12))
ax.set_title("Energia zmienia postać, ale jej suma pozostaje stała", loc="left")
ax.legend(loc="upper right", ncol=3, fontsize=9)
zapisz(fig, "energia")

# Jeden okres wystarczy, aby narysować pełną orbitę.
tf = np.linspace(0, T, 601)
xf = x0*np.cos(w0*tf) + (v0/w0)*np.sin(w0*tf)
vf = -x0*w0*np.sin(w0*tf) + v0*np.cos(w0*tf)
fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), layout="constrained")
for ax, xx, yy in zip(axes, [xf, xf/A], [vf, vf/(A*w0)]):
    ax.plot(xx, yy, color=BLUE)
    ax.scatter(xx[0], yy[0], color=ORANGE, zorder=3, label="Start")
    for j in [40, 190, 340, 490]:
        ax.annotate("", xy=(xx[j+15], yy[j+15]), xytext=(xx[j], yy[j]),
                    arrowprops={"arrowstyle": "->", "color": BLUE, "lw": 2})
    ax.axhline(0, color=INK, lw=0.7, alpha=0.4)
    ax.axvline(0, color=INK, lw=0.7, alpha=0.4)
axes[0].set(xlabel="Wychylenie x [m]", ylabel="Prędkość v [m/s]",
            title="Portret fazowy w jednostkach SI", xticks=np.linspace(-A, A, 5))
axes[0].legend(loc="upper right")
axes[1].set(xlabel="x / A", ylabel="v / (Aω₀)", title="Po normalizacji: okrąg")
axes[1].set_aspect("equal", adjustable="box")
zapisz(fig, "przestrzen_fazowa")

# Sprawdzamy prawo zachowania energii, a nie tylko wygląd rysunku.
blad_E = np.max(np.abs(Ep+Ek - 0.5*k*A**2))
assert blad_E < 1e-12
print(f"Maksymalny bezwzględny błąd energii: {blad_E:.3e} J")

# Blok C
b = 0.40
gamma = b / (2*m)
wd = np.sqrt(w0**2 - gamma**2)
td = np.linspace(0, 8*T, 3201)
C = x0
D = (v0 + gamma*x0) / wd
q = C*np.cos(wd*td) + D*np.sin(wd*td)
xd = np.exp(-gamma*td)*q
vd = np.exp(-gamma*td)*(
    -gamma*q - C*wd*np.sin(wd*td) + D*wd*np.cos(wd*td)
)
obwiednia = np.hypot(C, D)*np.exp(-gamma*td)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), layout="constrained")
axes[0].plot(td, xd, color=BLUE, label="x(t)")
axes[0].plot(td, obwiednia, "--", color=ORANGE, label="Obwiednie")
axes[0].plot(td, -obwiednia, "--", color=ORANGE)
axes[0].set(xlabel="Czas t [s]", ylabel="Wychylenie x [m]",
            title="Zanikające drgania")
axes[0].legend()
axes[1].plot(xd, vd, color=PURPLE)
axes[1].scatter(xd[0], vd[0], color=ORANGE, zorder=3, label="Start")
axes[1].scatter(0, 0, color=INK, marker="+", s=90, label="Równowaga")
for j in [90, 480, 1000]:
    axes[1].annotate("", xy=(xd[j+22], vd[j+22]), xytext=(xd[j], vd[j]),
                     arrowprops={"arrowstyle": "->", "color": PURPLE, "lw": 2})
axes[1].set(xlabel="Wychylenie x [m]", ylabel="Prędkość v [m/s]",
            title="Spirala w przestrzeni fazowej", xticks=np.linspace(-A, A, 5))
axes[1].legend(fontsize=9)
zapisz(fig, "tlumienie")

def symuluj(zeta, czasy):
    b_test = 2*zeta*np.sqrt(m*k)
    def rhs(czas, stan):
        xx, vv = stan
        return [vv, -(b_test/m)*vv - (k/m)*xx]
    sol = solve_ivp(rhs, (czasy[0], czasy[-1]), [x0, v0],
                    t_eval=czasy, rtol=1e-9, atol=1e-11)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y

tr = np.linspace(0, 2.5*T, 1201)
fig, ax = plt.subplots(figsize=(10, 4.4), layout="constrained")
for zeta, color, nazwa in [
    (0.15, BLUE, "Podkrytyczne"),
    (1.0, GREEN, "Krytyczne"),
    (2.0, ORANGE, "Nadkrytyczne"),
]:
    xr, vr = symuluj(zeta, tr)
    ax.plot(tr, xr, color=color, label=f"{nazwa}: ζ = {zeta:g}")
ax.axhline(0, color=INK, lw=0.8)
ax.set(xlabel="Czas t [s]", ylabel="Wychylenie x [m]")
ax.set_title("Ten sam stan początkowy, trzy rodzaje tłumienia", loc="left")
ax.legend(loc="upper right", fontsize=10)
zapisz(fig, "rodzaje_tlumienia")

# Niezależna kontrola: solver numeryczny kontra wzór analityczny.
xn, vn = symuluj(gamma/w0, td)
blad_x = np.max(np.abs(xn-xd))
blad_v = np.max(np.abs(vn-vd))
assert blad_x < 1e-8 and blad_v < 1e-7
Ed = 0.5*k*xd**2 + 0.5*m*vd**2
assert np.max(np.diff(Ed)) < 1e-12
print(f"Błąd x: {blad_x:.3e} m; błąd v: {blad_v:.3e} m/s")
print("Energia tłumionego oscylatora nie rośnie.")

# Blok D
F0 = 0.20
r = np.linspace(0, 2.2, 2201)
Omega = r*w0
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), layout="constrained")
for zeta, color in [(0.05, BLUE), (0.15, ORANGE), (0.40, GREEN)]:
    bz = 2*zeta*np.sqrt(m*k)
    amplituda = F0/np.hypot(k-m*Omega**2, bz*Omega)
    faza = np.arctan2(bz*Omega, k-m*Omega**2)
    axes[0].plot(r, 100*amplituda, color=color, label=f"ζ = {zeta:.2f}")
    axes[1].plot(r, faza, color=color)
    # Znane analityczne maksimum powinno zgadzać się z siatką.
    r_max = r[np.argmax(amplituda)]
    assert abs(r_max-np.sqrt(1-2*zeta**2)) < 2*(r[1]-r[0])
for ax in axes:
    ax.axvline(1, color=INK, lw=1, ls="--", alpha=0.5)
    ax.set_xlabel("Względna częstość wymuszenia Ω / ω₀")
    ax.set_xlim(0, 2.2)
axes[0].set(ylabel="Amplituda wychylenia [cm]", title="Odpowiedź amplitudowa")
axes[0].legend()
axes[1].set(ylabel="Opóźnienie fazowe δ [rad]", title="Odpowiedź fazowa",
            yticks=[0, np.pi/2, np.pi], yticklabels=["0", "π/2", "π"])
zapisz(fig, "rezonans")
print(f"Gotowe: zapisano 7 rysunków w {OUT.resolve()}")
