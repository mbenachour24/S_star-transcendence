import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos
from mpl_toolkits.mplot3d import Axes3D

# Define the recursive function S_{n+1} = a * sin(S_n) + b * cos(S_n)
def compute_attractor(a, b, steps=500, tol=1e-9):
    s = 1.0  # initial value
    for _ in range(steps):
        new_s = a * sin(s) + b * cos(s)
        if abs(new_s - s) < tol:
            return new_s
        s = new_s
    return s  # return final value even if it didn't converge

# Define grid over [-20, 20]^2
a_vals = np.linspace(-20, 20, 200)
b_vals = np.linspace(-20, 20, 200)
A, B = np.meshgrid(a_vals, b_vals)

# Compute attractor S* for each (a, b)
S_star = np.zeros_like(A)

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        try:
            S_star[i, j] = compute_attractor(A[i, j], B[i, j])
        except Exception:
            S_star[i, j] = np.nan  # for numerical stability

# Plotting the 3D surface
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(A, B, S_star, cmap='plasma', edgecolor='none')
ax.set_title(r'3D Projection of $S^*$ from $S_{n+1} = a\sin(S_n) + b\cos(S_n)$', fontsize=14)
ax.set_xlabel("a")
ax.set_ylabel("b")
ax.set_zlabel(r"$S^*$")
fig.colorbar(surf, shrink=0.5, aspect=10, label=r"$S^*$")
plt.tight_layout()
plt.show()
