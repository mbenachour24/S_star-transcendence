import numpy as np
import matplotlib.pyplot as plt

def recursive_transform(x, iterations=20):
    values = [x]
    for _ in range(iterations):
        x = np.sin(x) + np.cos(x)
        values.append(x)
    return values

# Définition de deux valeurs initiales très différentes
initial_A = 1.0
initial_B = 955.5

values_A = recursive_transform(initial_A, 20)
values_B = recursive_transform(initial_B, 20)

# Tracé des courbes de convergence
plt.plot(values_A, label="System A (1.0)", marker='o')
plt.plot(values_B, label="System B (9.5)", marker='s')

plt.axhline(1.2587281775, color='red', linestyle='--', label="Attracteur Computationnel")
plt.xlabel("Itérations")
plt.ylabel("Valeur de l'état")
plt.title("Convergence vers l'attracteur")
plt.legend()
plt.grid()
plt.show()
