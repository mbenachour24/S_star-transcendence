import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def f(x):
    """Fonction transcendantale définie comme sin(x) + cos(x)"""
    return np.sin(x) + np.cos(x)

def plot_transcendental_computation(S_init, max_iter=100):
    """
    Crée une visualisation complète du transcendantal computationnel:
    1. Évolution temporelle de l'état
    2. Diagramme de phase
    3. Systèmes couplés
    """
    # Calcul de l'évolution des états
    states = [S_init]
    for _ in range(max_iter):
        S_next = f(states[-1])
        states.append(S_next)
    
    states = np.array(states)
    
    # Création de la figure avec sous-graphiques
    plt.figure(figsize=(15, 12))
    gs = GridSpec(2, 2)
    
    # 1. Représentation Graphique de l'Équation
    ax1 = plt.subplot(gs[0, 0])
    iterations = np.arange(len(states))
    ax1.plot(iterations, states, 'b-', linewidth=1.5)
    ax1.axhline(y=states[-1], color='r', linestyle='--', label='Attracteur Stable')
    ax1.set_xlabel('Itérations (n)')
    ax1.set_ylabel('État (S_n)')
    ax1.set_title('Évolution vers l\'Attracteur Computationnel')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Diagramme de Phase
    ax2 = plt.subplot(gs[0, 1])
    ax2.plot(states[:-1], states[1:], 'g-', linewidth=1)
    ax2.plot(states[-2], states[-1], 'ro', markersize=8, label='Point Fixe')
    # Ligne diagonale y=x (points fixes)
    x_range = np.linspace(min(states), max(states), 100)
    ax2.plot(x_range, x_range, 'k--', alpha=0.5, label='y = x')
    # Courbe de la fonction
    ax2.plot(x_range, f(x_range), 'b-', alpha=0.5, label='S_n+1 = f(S_n)')
    ax2.set_xlabel('S_n')
    ax2.set_ylabel('S_n+1')
    ax2.set_title('Diagramme de Phase')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. Réseau de Systèmes Couplés
    ax3 = plt.subplot(gs[1, :])
    
    # Définir deux systèmes couplés avec des conditions initiales différentes
    S_A = [S_init]
    S_B = [S_init * 1.5]  # Condition initiale différente
    
    # Couplage: chaque système influence l'autre
    coupling_strength = 0.2
    
    for i in range(max_iter):
        # Calcul de l'état suivant avec couplage
        next_A = f(S_A[-1]) + coupling_strength * (S_B[-1] - S_A[-1])
        next_B = f(S_B[-1]) + coupling_strength * (S_A[-1] - S_B[-1])
        
        S_A.append(next_A)
        S_B.append(next_B)
    
    # Tracer les deux systèmes
    ax3.plot(np.arange(len(S_A)), S_A, 'b-', label='Système A')
    ax3.plot(np.arange(len(S_B)), S_B, 'g-', label='Système B')
    ax3.set_xlabel('Itérations')
    ax3.set_ylabel('État')
    ax3.set_title('Systèmes Autopoïétiques Couplés')
    ax3.axhline(y=S_A[-1], color='b', linestyle='--', alpha=0.5)
    ax3.axhline(y=S_B[-1], color='g', linestyle='--', alpha=0.5)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Données sur la convergence
    print(f"Valeur initiale: {S_init}")
    print(f"Attracteur stable: {states[-1]}")
    print(f"Différence entre les systèmes couplés: {abs(S_A[-1] - S_B[-1])}")

# Démonstration avec une condition initiale aléatoire
np.random.seed(42)  # Pour reproductibilité
S_init = np.random.rand() * 5
plot_transcendental_computation(S_init, max_iter=1000)