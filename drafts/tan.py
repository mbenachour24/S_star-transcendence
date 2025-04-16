import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the recursive function S_{n+1} = sin(S_n) + cos(S_n) + tan(S_n)
def update_S(S_n):
    return np.sin(S_n) + np.cos(S_n) + np.tan(S_n)

# Initialize values
num_iterations = 500  # Limited iterations due to potential instability
S_values = [0.1]  # Start at 0.1 to avoid tan(0) issues

# Generate values over iterations, handling divergence
for _ in range(num_iterations):
    next_S = update_S(S_values[-1])
    if abs(next_S) > 10:  # Prevent runaway divergence for visualization
        break
    S_values.append(next_S)

# Prepare figure for animation
fig, ax = plt.subplots()
ax.set_xlim(0, num_iterations)
ax.set_ylim(min(S_values) - 1, max(S_values) + 1)
line, = ax.plot([], [], 'o-', markersize=4, label=r'$S_{n+1} = \sin(S_n) + \cos(S_n) + \tan(S_n)$')

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Update function for animation
def update(frame):
    x_data = np.arange(frame)
    y_data = S_values[:frame]
    line.set_data(x_data, y_data)
    return line,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(S_values), init_func=init, blit=True, interval=150)

# Display animation
plt.xlabel("Iteration (n)")
plt.ylabel("S_n value")
plt.legend()
plt.title("Realtime Behavior of S_n+1 = sin(S) + cos(S) + tan(S)")

plt.show()
