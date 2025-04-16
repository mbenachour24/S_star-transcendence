def observe(state: str) -> str:
    """ Fonction d'observation qui tente de simplifier la récursion """
    # Exemple : Si A(B(A(B(x)))) apparaît fréquemment, on le remplace par un symbole unique
    state = state.replace("A(B(A(B(", "Ω(")  # Hypothèse d'un motif stable
    return state

def recursive_transform(n, state="start"):
    for i in range(n):
        if i % 2 == 0:
            state = f"A({state})"
        else:
            state = f"B({state})"
        
        # Application de l'observateur
        state = observe(state)

        if i % 1000000 == 0:
            print(f"Iteration {i}: {state[:50]}... (truncated)")
    
    return state

# Lancer la simulation avec observation intégrée
final_state = recursive_transform(10_000_000)
