import hashlib
import random

def hash_state(state: str) -> str:
    """Génère un hash compact de l'état pour optimiser l'observation."""
    return hashlib.sha256(state.encode()).hexdigest()

def observe_and_compress(state: str, memory: dict) -> str:
    """Fonction avancée d'observation avec compression dynamique et perturbation externe."""
    state_hash = hash_state(state)
    
    # Si l'état est déjà observé plusieurs fois, on considère qu'il est stable
    if state_hash in memory:
        memory[state_hash] += 1
        if memory[state_hash] > 3:  # Seuil arbitraire de récurrence
            return "STABLE_INVARIANT"
    else:
        memory[state_hash] = 1

    # Compression symbolique
    compression_patterns = [
        ("A(B(A(B(A(B(", "Ω("),  
        ("A(B(A(B(", "Ψ("),
    ]
    
    for pattern, replacement in compression_patterns:
        if pattern in state:
            state = state.replace(pattern, replacement)

    return state

def apply_external_perturbation(state: str) -> str:
    """Ajoute une perturbation externe périodique pour forcer une adaptation."""
    perturbations = [
        lambda s: s.replace("A", "X", 1),  # Modifier un symbole de la récursion
        lambda s: s.replace("B", "Y", 1),
        lambda s: f"P({s})",  # Ajouter une nouvelle transformation
    ]
    perturbation = random.choice(perturbations)
    return perturbation(state)

def recursive_with_perturbation(n, state="start"):
    memory = {}  # Mémoire des états observés sous forme de hash et nombre d'apparitions
    
    for i in range(n):
        if i % 2 == 0:
            state = f"A({state})"
        else:
            state = f"B({state})"
        
        # Application de la perturbation tous les 500 000 cycles
        if i % 500_000 == 0 and i > 0:
            state = apply_external_perturbation(state)
            print(f"Perturbation externe appliquée à l'itération {i}")

        # Appliquer la règle d'observation et de compression
        state = observe_and_compress(state, memory)

        # Vérifier si on atteint un état stable
        if state == "STABLE_INVARIANT":
            print(f"Stabilisation atteinte à l'itération {i}")
            return state

        if i % 1_000_000 == 0:
            print(f"Iteration {i}: Hash={hash_state(state)}")

    return state

# Lancer la simulation avec perturbation externe
final_state = recursive_with_perturbation(10_000_000)
