import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos
from mpmath import mp, mpf, pslq

# Increase numerical precision
mp.dps = 50

# Recursive function to compute attractor S^*
def compute_attractor(a, b, s0=1.0, steps=200):
    s = mpf(s0)
    for _ in range(steps):
        s = a * mp.sin(s) + b * mp.cos(s)
    return s

# Function to test if S* satisfies a low-degree integer polynomial using PSLQ
def is_transcendental(s_star, degree=6, tol=1e-30):
    coeffs = [s_star**i for i in range(degree + 1)]
    relation = pslq(coeffs, tol)
    return relation is None  # If no relation found, assume transcendental

# Create a grid of (a, b) values
a_values = np.linspace(-3, 3, 50)
b_values = np.linspace(-3, 3, 50)
heatmap = np.zeros((len(a_values), len(b_values)))

# Evaluate for each (a, b)
for i, a in enumerate(a_values):
    for j, b in enumerate(b_values):
        try:
            s_star = compute_attractor(mpf(a), mpf(b))
            heatmap[i, j] = 1.0 if is_transcendental(s_star) else 0.0
        except:
            heatmap[i, j] = np.nan  # Mark failed computations

# Plot the heatmap
plt.figure(figsize=(10, 8))
plt.imshow(heatmap.T, extent=(-3, 3, -3, 3), origin='lower', aspect='auto', cmap='hot')
plt.colorbar(label='1 = likely transcendental, 0 = likely algebraic')
plt.title("Heatmap of Attractors S* for S_{n+1} = a·sin(S_n) + b·cos(S_n)")
plt.xlabel("a")
plt.ylabel("b")
plt.grid(False)
plt.show()
