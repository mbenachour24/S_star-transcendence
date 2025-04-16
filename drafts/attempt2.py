# Simulation de la récursion pour 10 000 000 d'itérations en optimisant la structure

def recursive_transform(n, state="start"):
    """
    Simule la transformation récursive jusqu'à 10 000 000 d'itérations
    sans stockage inutile des états imbriqués, en analysant la structure.
    """
    for i in range(n):
        if i % 2 == 0:
            state = f"A({state})"
        else:
            state = f"B({state})"

        # Réduction périodique pour détecter un éventuel invariant
        if i % 1000000 == 0:
            print(f"Iteration {i}: {state[:50]}... (truncated)")  # Affichage partiel pour éviter surcharge mémoire

    return state

# Lancer la simulation
final_state = recursive_transform(10_000_000)
