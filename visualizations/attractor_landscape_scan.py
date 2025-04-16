import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos
from tqdm import tqdm

# Parameters
steps = 500
tolerance = 1e-6
initial_state = 1.0

# Grid parameters
a_vals = np.linspace(-10, 10, 100)
b_vals = np.linspace(-10, 10, 100)
attractor_map = np.zeros((len(a_vals), len(b_vals)))

def compute_attractor(a, b, initial, steps=500, tol=1e-6):
    state = initial
    for _ in range(steps):
        new_state = a * sin(state) + b * cos(state)
        if abs(new_state - state) < tol:
            return new_state
        state = new_state
    return None  # did not converge

# Compute attractors
for i, a in tqdm(enumerate(a_vals), total=len(a_vals), desc="Scanning a"):
    for j, b in enumerate(b_vals):
        s_star = compute_attractor(a, b, initial_state, steps, tolerance)
        if s_star is not None and np.isfinite(s_star):
            attractor_map[i, j] = s_star
        else:
            attractor_map[i, j] = np.nan  # mark divergence or non-convergence

# Plot heatmap
plt.figure(figsize=(10, 8))
plt.imshow(attractor_map.T, origin='lower', extent=[-10, 10, -10, 10], aspect='auto', cmap='plasma')
plt.colorbar(label="Attractor $S^*$")
plt.xlabel("a")
plt.ylabel("b")
plt.title("Attractors $S^*$ for $S_{n+1} = a\\sin(S_n) + b\\cos(S_n)$ over $[-10,10]^2$")
plt.grid(False)
plt.tight_layout()
plt.show()
