import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the recursive function S_{n+1} = sin(S_n) + cos(S_n)
def update_S(S_n):
    return np.sin(S_n) + np.cos(S_n)

# Initialize values
num_iterations = 100  # Number of iterations
S_values = [0]  # Initial condition S_0 = 0

# Generate values over iterations
for _ in range(num_iterations):
    S_values.append(update_S(S_values[-1]))

# Prepare figure for animation
fig, ax = plt.subplots()
ax.set_xlim(0, num_iterations)
ax.set_ylim(min(S_values) - 0.1, max(S_values) + 0.1)
line, = ax.plot([], [], 'o-', markersize=4, label=r'$S_{n+1} = \sin(S_n) + \cos(S_n)$')

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
ani = animation.FuncAnimation(fig, update, frames=num_iterations, init_func=init, blit=True, interval=100)

# Display animation
plt.xlabel("Iteration (n)")
plt.ylabel("S_n value")
plt.legend()
plt.title("Realtime Behavior of S_n+1 = sin(S) + cos(S)")

plt.show()
