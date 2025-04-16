import numpy as np

class SystemMathematical:
    """Système autopoïétique computationnel."""
    def __init__(self, name, initial_value=1.0):
        self.name = name
        self.state_value = initial_value  # État initial
        self.previous_values = []  # Mémorisation pour la détection de convergence
        self.attractor = None

    def update_state(self):
        """Transformation récursive."""
        self.state_value = np.sin(self.state_value) + np.cos(self.state_value)
        self.previous_values.append(self.state_value)
        if len(self.previous_values) > 10:
            self.previous_values.pop(0)

    def has_converged(self):
        """Détecte si le système atteint un invariant computationnel."""
        if len(self.previous_values) < 10:
            return False

        # Vérification de la stabilité des dernières valeurs
        diffs = np.diff(self.previous_values)
        return np.all(np.abs(diffs) < 1e-9)  # Tolérance plus fine

class CoordinatorMathematical:
    """Société récursive orchestrant la convergence."""
    def __init__(self, initial_values=None):
        if initial_values is None:
            initial_values = {"System_A": 1.0, "System_B": 9.5}  # Default initial values

        self.systems = {
            "System_A": SystemMathematical("System_A", initial_values["System_A"]),
            "System_B": SystemMathematical("System_B", initial_values["System_B"]),
        }

    def detect_dominant_attractor(self):
        """Détecte l'invariant computationnel global."""
        attractors = [sys.state_value for sys in self.systems.values()]
        return np.mean(attractors)  # Estimation plus fine

    def simulate(self, max_iterations=1_000_000):
        """Exécute la simulation."""
        state_history = []
        for i in range(max_iterations):
            for system in self.systems.values():
                system.update_state()

            # Enregistrement des valeurs d'état
            state_history.append((i, self.systems['System_A'].state_value, self.systems['System_B'].state_value))

            # Vérification de convergence
            if all(sys.has_converged() for sys in self.systems.values()):
                global_attractor = self.detect_dominant_attractor()
                print("\033[92mInvariant computationnel atteint après", i, "itérations.\033[0m")
                print(f"Valeur de l'invariant: {global_attractor:.16f}")
                # Print the state history
                print("State History:")
                for iteration, state_a, state_b in state_history:
                    print(f"Iteration {iteration}: System_A={state_a:.10f} | System_B={state_b:.10f}")
                return state_history

            if i % 100_000 == 0:
                print(f"Iteration {i}: System_A={self.systems['System_A'].state_value:.10f} | "
                      f"System_B={self.systems['System_B'].state_value:.10f}")

# Lancer la simulation avec des valeurs initiales spécifiques
initial_conditions = {"System_A": 1.0, "System_B": 0.3}  # Modification ici
coordinator_math = CoordinatorMathematical(initial_conditions)
coordinator_math.simulate()
