import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from mpmath import mp

# Set high precision
mp.dps = 100  # 100 decimal places

# Define the recurrence relation
def compute_s_star_live():
    S = mp.mpf(1)  # Initial guess
    S_star = mp.mpf(1.258728177492676458639139165965230970651878182473241819243245904146799655610615994764070973118763133)  # Fixed-point
    history = []
    errors = []
    iteration = 0
    
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    ax.set_xlabel("Iteration")
    ax.set_ylabel("S_n Value")
    
    while True:
        S = mp.sin(S) + mp.cos(S)
        history.append(float(S))
        errors.append(abs(float(S - S_star)))
        iteration += 1
        
        print(f"Iteration {iteration}: S* ≈ {S}")
        
        # Live updating plot
        ax.clear()
        ax.plot(history, marker='o', linestyle='-', color='b', label="S_n")
        ax.set_title(f"Convergence to S* (Iteration {iteration})")
        ax.set_xlabel("Iteration")
        ax.set_ylabel("S_n Value")
        ax.legend()
        plt.pause(0.05)  # Pause for live update
        
        if iteration > 100 and errors[-1] < 1e-50:  # Stop if convergence is reached
            break
        
        time.sleep(0.1)  # Slow it down a little for readability
    
    # Fit an exponential decay model
    def exp_decay(n, e0, lambda_):
        return e0 * np.exp(-lambda_ * n)
    
    iterations = np.arange(len(errors))
    popt, _ = curve_fit(exp_decay, iterations, errors, p0=(errors[0], 0.1))
    
    # Plot error decay
    plt.figure()
    plt.plot(iterations, errors, 'bo', label="Observed Errors")
    plt.plot(iterations, exp_decay(iterations, *popt), 'r-', label=f"Fit: e_n = {popt[0]:.5e} e^(-{popt[1]:.5f} n)")
    plt.yscale("log")
    plt.xlabel("Iteration")
    plt.ylabel("Error |S_n - S*|")
    plt.title("Error Decay in Log Scale")
    plt.legend()
    plt.show()

# Run the live computation
compute_s_star_live()