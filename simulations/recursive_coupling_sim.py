import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos

# Define autonomous SystemUnit
class SystemUnit:
    def __init__(self, name, func):
        self.name = name
        self.func = func
        self.history = []

    def operate(self, input_value):
        output = self.func(input_value)
        self.history.append(output)
        return output

# Coordinator handles coupling and recursion
class Coordinator:
    def __init__(self, system_units, coupling_rule=None):
        self.system_units = system_units
        self.state_history = []
        self.coupling_rule = coupling_rule or self.default_coupling

    def default_coupling(self, outputs):
        return sum(outputs)

    def step(self, current_state):
        outputs = [unit.operate(current_state) for unit in self.system_units]
        new_state = self.coupling_rule(outputs)
        self.state_history.append(new_state)
        return new_state

    def run(self, initial_state, steps=1000):
        state = initial_state
        self.state_history = [state]
        for _ in range(steps):
            state = self.step(state)
        return self.state_history

# 🔁 Create two autonomous systems: sin and cos

SinSystem = SystemUnit("Sin", lambda x: 2 * sin(x))
CosSystem = SystemUnit("Cos", lambda x: 2 * cos(x))

# Create the simulation engine
coordinator = Coordinator([SinSystem, CosSystem])

# ▶️ Run with logging
def run_with_logs(initial_state, steps=1000):
    state = initial_state
    print(f"{'Step':>4} | {'S_n':>12} | {'sin(S_n)':>12} | {'cos(S_n)':>12} | {'S_{n+1}':>12}")
    print("-" * 60)

    trajectory = [state]
    for n in range(steps):
        f_output = SinSystem.operate(state)
        g_output = CosSystem.operate(state)
        next_state = f_output + g_output

        print(f"{n:>4} | {state:>12.8f} | {f_output:>12.8f} | {g_output:>12.8f} | {next_state:>12.8f}")
        
        trajectory.append(next_state)
        state = next_state

    return trajectory

# 🔁 Run the simulation and get the full trajectory
trajectory = run_with_logs(initial_state=1.0, steps=1000)

# 📈 Plotting the result
plt.plot(trajectory, label="S_n")
plt.axhline(y=trajectory[-1], color='gray', linestyle='--', label=f"Final ≈ {trajectory[-1]:.6f}")
plt.title("Recursive System Trajectory: S_{n+1} = sin(S_n) + cos(S_n)")
plt.xlabel("Step n")
plt.ylabel("S_n")
plt.legend()
plt.grid(True)
plt.show()