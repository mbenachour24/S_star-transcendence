import mpmath
import matplotlib.pyplot as plt

class SystemMathematical:
    """Système computationnel utilisant une précision arbitraire avec un test avancé de stabilité."""
    def __init__(self, name, initial_value):
        self.name = name
        self.state_value = mpmath.mpf(initial_value)  # État initial en haute précision
        self.previous_values = []  # Mémorisation pour la détection de convergence
        self.max_deviation = mpmath.mpf("0")  # Écart maximal à l'équilibre
        self.previous_diffs = []  # Mémorisation des variations successives

    def update_state(self):
        """Transformation récursive avec mpmath."""
        new_value = mpmath.sin(self.state_value) + mpmath.cos(self.state_value)
        diff = abs(new_value - self.state_value)
        self.previous_values.append(self.state_value)
        self.previous_diffs.append(diff)
        self.state_value = new_value

        if len(self.previous_values) > 50:
            self.previous_values.pop(0)
            self.previous_diffs.pop(0)

        # Mise à jour de l'écart maximal par rapport à l'attracteur supposé
        self.max_deviation = max(self.max_deviation, diff)

    def has_converged(self):
        """Détecte si le système atteint un invariant computationnel en utilisant des critères avancés."""
        if len(self.previous_values) < 50:
            return False

        # Vérification de la décroissance des oscillations
        if self.max_deviation > mpmath.mpf("1e-12"):
            return False

        # Vérification de la décroissance des variations successives
        if max(self.previous_diffs) > mpmath.mpf("1e-30"):
            return False

        return True

class CoordinatorMathematical:
    """Société récursive orchestrant la convergence en haute précision avec un test avancé de stabilité."""
    def __init__(self, initial_values):
        self.systems = {
            f"System_{i}": SystemMathematical(f"System_{i}", init_val)
            for i, init_val in enumerate(initial_values)
        }

    def detect_dominant_attractor(self):
        """Détecte l'invariant computationnel global en précision arbitraire."""
        attractors = [sys.state_value for sys in self.systems.values()]
        return sum(attractors) / len(attractors)

    def simulate(self, max_iterations=100_000_000):
        """Exécute la simulation avec haute précision et enregistre les trajectoires."""
        state_histories = {name: [] for name in self.systems.keys()}

        for i in range(max_iterations):
            for name, system in self.systems.items():
                system.update_state()
                state_histories[name].append(float(system.state_value))  # Convertir pour affichage

            # Vérification de convergence
            if all(sys.has_converged() for sys in self.systems.values()):
                global_attractor = self.detect_dominant_attractor()
                print("\033[92mInvariant computationnel atteint après", i, "itérations.\033[0m")
                print(f"Valeur de l'invariant: {global_attractor}")
                self.plot_trajectories(state_histories)
                return state_histories

            if i % 5_000_000 == 0:
                print(f"Iteration {i}: " + " | ".join([
                    f"{name}={sys.state_value}" for name, sys in self.systems.items()
                ]))

        print("\033[91mAucune convergence atteinte après 100 millions d'itérations.\033[0m")
        self.plot_trajectories(state_histories)
        return state_histories

    def plot_trajectories(self, state_histories):
        """Affiche les trajectoires des systèmes."""
        plt.figure(figsize=(10, 6))
        for name, history in state_histories.items():
            plt.plot(history, label=name)
        plt.xlabel("Iterations")
        plt.ylabel("Valeur de l'état")
        plt.title("Convergence en haute précision vers l'invariant computationnel")
        plt.legend()
        plt.show()

# Lancer la simulation avec plusieurs conditions initiales en haute précision
mpmath.mp.dps = 50  # Définir la précision décimale à 50 chiffres
initial_values = [mpmath.mpf(x) for x in mpmath.linspace(0, 2, 10)]
coordinator_math = CoordinatorMathematical(initial_values)
coordinator_math.simulate()
