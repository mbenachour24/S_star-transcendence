from typing import Callable, List, Dict
import random
import time

# Définition des couleurs pour la console
colors = [31, 32, 33, 34, 35, 36, 37]  # Rouge, Vert, Jaune, Bleu, Magenta, Cyan, Blanc

# Définition de la classe System avec couplage structurel
class System:
    class Coupling:
        def __init__(self, func: Callable, connection: 'System'):
            self.connection = connection
            self.func = func

    def __init__(self, name: str, logics: Dict[str, Callable]):
        self.name: str = name
        self.logics: Dict[str, Callable] = logics
        self.state: Dict[str, List[str]] = {}
        self.couplings: List['System.Coupling'] = []
        self.color = random.choice(colors)

    def get_state(self) -> Dict[str, List[str]]:
        """Retourne l'état actuel du système."""
        return self.state
    
    def process(self, process_name: str, *args, **kwargs) -> str:
        """Exécute un processus logique et met à jour l'état du système."""
        print(f"\033[{self.color}m{self.name} processing {process_name}\033[0m")
        if process_name not in self.logics:
            raise ValueError(f"Process {process_name} is not defined in logics.")
        result = self.logics[process_name](*args, **kwargs)
        self.state.setdefault(process_name, []).append(result)
        
        # Activer le couplage structurel après chaque processus
        for coupling in self.couplings:
            coupling.func(self, coupling.connection, result)
        
        return result
    
    def add_coupling(self, func: Callable, unit: 'System'):
        """Crée un couplage avec un autre système."""
        coupling = System.Coupling(func, unit)
        self.couplings.append(coupling)

# === Définition des logiques de transformation ===
def logic_A(data: str) -> str:
    """Processus de transformation spécifique à System_A."""
    return f"A({data})"

def logic_B(data: str) -> str:
    """Processus de transformation spécifique à System_B."""
    return f"B({data})"

# === Fonction de couplage structurel ===
def structural_coupling(system1: System, system2: System, input_data: str):
    """Échange de données entre deux systèmes après chaque itération."""
    print(f"\033[90m[CoupLage] {system1.name} → {system2.name} : {input_data}\033[0m")
    system2.process("transform", input_data)

# === Initialisation des systèmes ===
System_A = System("System_A", logics={"transform": logic_A})
System_B = System("System_B", logics={"transform": logic_B})

# === Ajout du couplage bidirectionnel ===
System_A.add_coupling(structural_coupling, System_B)
System_B.add_coupling(structural_coupling, System_A)

# === Exécution récursive ===
initial_input = "start"

print("\n\033[95m=== Début de la récursion ===\033[0m\n")
System_A.process("transform", initial_input)

# Ajout d'une boucle pour observer l'évolution
results = []
for i in range(5):
    time.sleep(0.5)
    print("\n\033[95m=== Nouvelle itération ===\033[0m\n")
    result = System_A.process("transform", f"cycle_{i}")
    results.append(result)

# Retourner les derniers états des systèmes
System_A.get_state(), System_B.get_state()
