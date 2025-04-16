import time
import matplotlib.pyplot as plt
from mpmath import mp

# Set high precision
mp.dps = 100  # 100 decimal places

# Define the recurrence relation
def compute_s_star_live():
    S = mp.mpf(1)  # Initial guess
    convergence_threshold = mp.mpf("1e-50")
    history = []
    iteration = 0
    
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    ax.set_xlabel("Iteration")
    ax.set_ylabel("S_n Value")
    
    while True:
        next_S = mp.sin(S) + mp.cos(S)
        history.append(float(next_S))
        iteration += 1
        
        print(f"Iteration {iteration}: S* ≈ {next_S}")
        
        # Convergence check
        if abs(next_S - S) < convergence_threshold:
            break
        
        # Update S
        S = next_S
        
        # Live updating plot
        ax.clear()
        ax.plot(history, marker='o', linestyle='-', color='b')
        ax.set_title(f"Convergence to S* (Iteration {iteration})")
        ax.set_xlabel("Iteration")
        ax.set_ylabel("S_n Value")
        plt.pause(0.05)  # Pause for live update
        
        time.sleep(0.1)  # Slow it down a little for readability

# Run the live computation
compute_s_star_live()
