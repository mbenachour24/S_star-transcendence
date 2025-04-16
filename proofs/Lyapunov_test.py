import sympy as sp
import random
import numpy as np

def recursive_cognition(thinking, recursion, data, iterations=100):
    """
    Simulates the recursion of cognition over multiple iterations and computes Lyapunov exponent.
    """
    S = sp.Symbol('S')  # Cognition state
    f_rec = recursion(S)  # Recursion function
    f_data = data(S)  # Data function
    f = f_rec + f_data
    f_prime = sp.diff(f, S)  # Compute derivative for Lyapunov exponent
    
    cognition = sp.Float(thinking)  # Ensure cognition is a SymPy float
    log = []
    lyapunov_sum = 0
    
    for i in range(iterations):
        cognition = f.subs(S, cognition)
        cognition = sp.simplify(cognition)
        log.append(f"Iteration {i+1}: {cognition}")
        
        # Compute Lyapunov exponent component
        derivative_value = abs(f_prime.subs(S, cognition))
        if derivative_value > 0:
            lyapunov_sum += np.log(float(derivative_value))
    
    # Compute final Lyapunov exponent
    lyapunov_exp = lyapunov_sum / iterations
    return cognition, log, lyapunov_exp

# Define the recursion function
recursion_function = lambda S: sp.sin(S) + sp.cos(S)  

# Expanded data functions
data_functions = {
    "None": lambda S: sp.Integer(0),
    "Logarithmic": lambda S: sp.log(1 + S) / 5,
    "Exponential Decay": lambda S: sp.exp(-S),
    "Sinusoidal Perturbation": lambda S: sp.sin(S) / 5,
    "Quadratic Growth": lambda S: S**2 / 20,
    "Inverse Decay": lambda S: 1 / (1 + S),
    "Hyperbolic Perturbation": lambda S: sp.tanh(S) / 5,
    "Cosine Influence": lambda S: sp.cos(S) / 5,
    "Sine-Exponential Mix": lambda S: sp.sin(S) * sp.exp(-S),
    "Fractional Root": lambda S: sp.sqrt(S) / 10,
    "Piecewise Adjustment": lambda S: sp.Piecewise((S / 10, S < 1), (sp.exp(-S), S >= 1)),
    "Log-Sine Coupling": lambda S: sp.log(1 + S) * sp.sin(S) / 5,
    "Cubic Perturbation": lambda S: S**3 / 50,
    "Random Noise": lambda S: sp.Float(random.uniform(-0.1, 0.1)),
}

# Initial cognition state
initial_thinking = sp.Float(1.0)  # Ensure SymPy float

# Create log file
log_output = ""
lyapunov_results = ""

# Run the recursive cognition model for different data functions
for name, data_function in data_functions.items():
    log_output += f"\n=== Testing Data Function: {name} ===\n\n"
    final_cognition, log, lyapunov_exp = recursive_cognition(initial_thinking, recursion_function, data_function, iterations=100)
    log_output += "\n".join(log) + "\n"
    lyapunov_results += f"{name}: Lyapunov Exponent = {lyapunov_exp}\n"

# Save log to a text file
with open("recursive_cognition_log.txt", "w") as log_file:
    log_file.write(log_output)

# Save Lyapunov exponents to a separate file
with open("lyapunov_exponents.txt", "w") as lyapunov_file:
    lyapunov_file.write(lyapunov_results)
