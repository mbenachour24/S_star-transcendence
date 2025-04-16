from mpmath import mp, cos, sin

# Configuration de la précision arbitraire (par exemple, 1000 chiffres décimaux)
mp.dps = 1000  # Nombre de chiffres décimaux de précision

# Fonction d'itération
def g(S):
    return cos(S) + sin(S)

# Point fixe théorique
S_star = mp.mpf("1.2587281774925669")  # Valeur de S^* avec haute précision

# Test de stabilité : calcul de g'(S^*)
def g_prime(S):
    return cos(S) - sin(S)

g_prime_S_star = g_prime(S_star)
print(f"g'(S^*) = {g_prime_S_star}")

# Simulation de l'itération
def simulate(S0, max_iterations=1000, tolerance=1e-100):
    S = S0
    history = []
    for i in range(max_iterations):
        S_new = g(S)
        history.append(S_new)
        if abs(S_new - S) < tolerance:
            print(f"Convergence atteinte après {i} itérations.")
            break
        S = S_new
    return history

# Point de départ (proche de S^*)
S0 = S_star + mp.mpf("1e-10")  # Petite perturbation

# Exécution de la simulation
history = simulate(S0, max_iterations=1000000, tolerance=1e-100)

# Affichage des dernières valeurs
print("Dernières valeurs de S_n :")
for i, S in enumerate(history[-10:]):
    print(f"Iteration {len(history) - 10 + i}: S_n = {S}")