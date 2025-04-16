import hashlib
from collections import defaultdict
import numpy as np

class SystemSimulated:
    """Système autopoïétique simulé avec mémoire et récursion."""

    def __init__(self, name):
        self.name = name
        self.state = "1.0"  # Initial state as a string representation of a number
        self.memory = defaultdict(int)  # Mémoire évolutive pour observer les patterns
        self.attractor = None  # État attracteur stable
        self.last_states = []  # To store the last 10 states
        self.cycle_count = 0  # Compteur pour le nombre total de cycles

    def hash_state(self):
        """Génère un hash compact de l'état."""
        return hashlib.sha256(self.state.encode()).hexdigest()

    def observe_and_regulate(self):
        """Détection des attracteurs computationnels sans forçage."""
        state_hash = self.hash_state()
        self.memory[state_hash] += 1
        # Dès qu'un état est répété plus de 2 fois, il devient l'attracteur universel
        if self.memory[state_hash] > 2 and self.attractor is None:
            self.attractor = self.state  # Fixation de l'état stable

    def update_state(self):
        """Transformation récursive simulée par une équation mathématique discrète."""
        # Simulate the mathematical transformation using discrete steps
        current_value = float(self.state)
        new_value = np.sin(current_value) + np.cos(current_value)
        self.state = f"{new_value:.6f}"  # Update state as a string

        # Store the last 10 states
        if len(self.last_states) >= 10:
            self.last_states.pop(0)
        self.last_states.append(self.state)

    def fast_forward(self, cycles=10_000_000):
        """Condense des milliards d'itérations."""
        for _ in range(cycles):
            self.update_state()
            self.cycle_count += 1
            self.observe_and_regulate()
            if self.state == self.attractor:
                return True  # Arrêt immédiat si stabilisation détectée
        return False

    def print_status(self):
        """Print the current state, last 10 iterations, and total cycles."""
        print(f"Current State: {self.state}")
        print(f"Last 10 Iterations: {self.last_states}")
        print(f"Total Cycles: {self.cycle_count}")

class CoordinatorSimulated:
    """Société orchestrant des systèmes autopoïétiques."""

    def __init__(self):
        self.systems = {
            "System_A": SystemSimulated("System_A"),
            "System_B": SystemSimulated("System_B")
        }

    def simulate(self, max_iterations=10_000_000_000):
        """Exécute la simulation sans forçage de l’invariant computationnel."""
        for i in range(0, max_iterations, 10_000_000):  # Sauts de 10M de cycles
            stable_A = self.systems["System_A"].fast_forward(10_000_000)
            stable_B = self.systems["System_B"].fast_forward(10_000_000)
            # Vérification de la convergence
            if stable_A and stable_B:
                print("\033[92mInvariant computationnel atteint naturellement.\033[0m")
                # Print status of each system
                for sys in self.systems.values():
                    sys.print_status()
                return
            # Affichage périodique
            if i % 50_000_000 == 0:
                print(f"Iteration {i}: System_A Hash={self.systems['System_A'].hash_state()} | System_B Hash={self.systems['System_B'].hash_state()}")

# Lancer la simulation sans forçage de l’invariant computationnel
coordinator_sim = CoordinatorSimulated()
coordinator_sim.simulate(10_000_000_000)
