import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Rozwiązanie wzorcowe prowadzącego.
# Przykładowy indeks 123456 -> v0 = 12 m/s, alpha = 56 deg.
v0 = 12.0
alpha = math.radians(56.0)
g = 9.81

# Parametry dla modelu oporu kwadratowego
m = 0.145        # kg
rho = 1.225      # kg/m^3
Cd = 0.47
A = 0.0042       # m^2
beta = 0.5 * rho * Cd * A / m

def vacuum():
    tf = 2 * v0 * math.sin(alpha) / g
    t = np.linspace(0, tf, 300)
    x = v0 * math.cos(alpha) * t
    y = v0 * math.sin(alpha) * t - 0.5 * g * t**2
    vx = np.full_like(t, v0 * math.cos(alpha))
    vy = v0 * math.sin(alpha) - g * t
    return t, x, y, vx, vy

def rhs(t, s):
    x, y, vx, vy = s
    speed = math.hypot(vx, vy)
    return [
        vx,
        vy,
        -beta * speed * vx,
        -g - beta * speed * vy,
    ]

def ground(t, s):
    return s[1] if t > 1e-8 else 1.0

ground.terminal = True
ground.direction = -1

tv, xv, yv, vxv, vyv = vacuum()
sol = solve_ivp(
    rhs,
    [0, 10],
    [0, 0, v0*math.cos(alpha), v0*math.sin(alpha)],
    events=ground,
    dense_output=True,
    max_step=0.01,
    rtol=1e-9,
    atol=1e-11,
)
tf = sol.t_events[0][0]
td = np.linspace(0, tf, 300)
xd, yd, vxd, vyd = sol.sol(td)

# 1. Trajektoria
plt.figure()
plt.plot(xv, yv, label="bez oporu")
plt.plot(xd, yd, label="z oporem")
plt.xlabel("x [m]"); plt.ylabel("y [m]")
plt.legend(); plt.grid(alpha=0.3); plt.tight_layout()
plt.savefig("trajektoria.png", dpi=150)
plt.close()

# 2. Wysokość
plt.figure()
plt.plot(tv, yv, label="bez oporu")
plt.plot(td, yd, label="z oporem")
plt.xlabel("t [s]"); plt.ylabel("y [m]")
plt.legend(); plt.grid(alpha=0.3); plt.tight_layout()
plt.savefig("wysokosc_czas.png", dpi=150)
plt.close()

# 3. Prędkość
sv = np.hypot(vxv, vyv)
sd = np.hypot(vxd, vyd)
plt.figure()
plt.plot(tv, sv, label="bez oporu")
plt.plot(td, sd, label="z oporem")
plt.xlabel("t [s]"); plt.ylabel("|v| [m/s]")
plt.legend(); plt.grid(alpha=0.3); plt.tight_layout()
plt.savefig("predkosc_czas.png", dpi=150)
plt.close()

# 4. Energia na jednostkę masy
Ev = 0.5*sv**2 + g*yv
Ed = 0.5*sd**2 + g*yd
plt.figure()
plt.plot(tv, Ev, label="bez oporu")
plt.plot(td, Ed, label="z oporem")
plt.xlabel("t [s]"); plt.ylabel("E/m [J/kg]")
plt.legend(); plt.grid(alpha=0.3); plt.tight_layout()
plt.savefig("energia_czas.png", dpi=150)
plt.close()
