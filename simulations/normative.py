import numpy as np
import matplotlib.pyplot as plt

# Simulation de deux modèles normatifs
class NormativeSystem:
    def __init__(self, num_agents, adaptation_rate=0.1, centralization=False):
        self.num_agents = num_agents
        self.centralization = centralization  # Si True, impose une norme unique
        self.adaptation_rate = adaptation_rate  # Vitesse d'adaptation des normes
        self.norms = np.random.rand(num_agents)  # Valeurs initiales des normes des agents
        self.global_norm = np.mean(self.norms) if centralization else None

    def update_norms(self):
        if self.centralization:
            # Tous les agents doivent se conformer à la norme globale figée
            self.norms = np.full(self.num_agents, self.global_norm)
        else:
            # Chaque agent ajuste sa norme en fonction de son environnement
            perturbation = np.random.randn(self.num_agents) * self.adaptation_rate
            self.norms += perturbation  # Ajustement local des normes
            self.norms = np.clip(self.norms, 0, 1)  # Normes entre 0 et 1

    def get_stability_metric(self):
        return np.var(self.norms)  # Plus la variance est faible, plus le système est stable

# Configuration de la simulation
num_agents = 100
num_iterations = 100

# Initialisation des deux systèmes
system_centralized = NormativeSystem(num_agents, centralization=True)
system_adaptive = NormativeSystem(num_agents, adaptation_rate=0.05, centralization=False)

# Stockage des métriques
stability_centralized = []
stability_adaptive = []

# Exécution de la simulation
for _ in range(num_iterations):
    system_centralized.update_norms()
    system_adaptive.update_norms()
    
    stability_centralized.append(system_centralized.get_stability_metric())
    stability_adaptive.append(system_adaptive.get_stability_metric())

# Affichage des résultats
plt.figure(figsize=(10, 5))
plt.plot(stability_centralized, label="Système Centralisé (norme figée)", linestyle='--')
plt.plot(stability_adaptive, label="Système Adaptatif (normes évolutives)")
plt.xlabel("Itérations")
plt.ylabel("Variance des Normes (instabilité)")
plt.legend()
plt.title("Comparaison de la stabilité normative")
plt.show()