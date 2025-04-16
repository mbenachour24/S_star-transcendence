import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def compute_attractor(a, b, initial_state=1.0, steps=200, tolerance=1e-3):
    state = initial_state
    for _ in range(steps):
        new_state = a * np.sin(state) + b * np.cos(state)
        if abs(new_state - state) < tolerance:
            return new_state
        state = new_state
    return np.nan

a_vals = np.linspace(-20, 20, 60)
b_vals = np.linspace(-20, 20, 60)
A, B = np.meshgrid(a_vals, b_vals)
S = np.zeros_like(A)

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        S[i, j] = compute_attractor(A[i, j], B[i, j])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

def update(frame):
    ax.clear()
    surf = ax.plot_surface(A, B, S, cmap=cm.viridis, edgecolor='none')
    ax.set_title("Attractors $S^*$")
    ax.set_xlabel("a")
    ax.set_ylabel("b")
    ax.set_zlabel("$S^*$")
    ax.view_init(elev=30, azim=frame)
    return surf,

anim = FuncAnimation(fig, update, frames=np.linspace(0, 360, 60), blit=False)
anim.save("attractors_animation.mp4", fps=10, extra_args=['-vcodec', 'libx264'])
