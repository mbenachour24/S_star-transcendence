import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos
from tqdm import tqdm

# Define the recursive update function
def compute_attractor(a, b, initial_state=1.0, steps=500, tolerance=1e-6):
    state = initial_state
    for _ in range(steps):
        new_state = a * sin(state) + b * cos(state)
        if abs(new_state - state) < tolerance:
            return new_state
        state = new_state
    return np.nan  # no convergence

# Define the parameter space (wider range)
a_vals = np.linspace(-20, 20, 400)
b_vals = np.linspace(-20, 20, 400)
A, B = np.meshgrid(a_vals, b_vals)

# Prepare the result matrix
attractors = np.empty_like(A)

# Compute attractors for each (a, b)
for i in tqdm(range(A.shape[0]), desc="Computing attractors"):
    for j in range(A.shape[1]):
        attractors[i, j] = compute_attractor(A[i, j], B[i, j])

# Plot the heatmap
plt.figure(figsize=(10, 8))
plt.imshow(attractors, extent=[-20, 20, -20, 20], origin='lower', cmap='plasma', aspect='auto')
plt.colorbar(label="Attractor $S^*$")
plt.title("Attractors $S^*$ for $S_{n+1} = a \\sin(S_n) + b \\cos(S_n)$ over $[-20, 20]^2$")
plt.xlabel("a")
plt.ylabel("b")
plt.grid(False)
plt.show()
