import random

# 1. Random string input
N = "legitimus"

# 2. Logiques institutionnelles
def L(x):  # Système juridique
    return x[::-1] + "_jus"

def M(x):  # Système politique
    return x.upper() + "_LEX"

# 3. Connecteur C
def C(a, b):
    return a + " || " + b

# 4. Coordinateur K
def K(output):
    max_length = 20
    return output[:max_length] + "..."

# 5. Mémoire du système
memory = []

# 6. Simulation récursive
Sn = N
for n in range(5):
    fi = L(Sn)
    fj = M(Sn)
    combined = C(fi, fj)
    Sn_next = K(combined)
    memory.append(Sn_next)
    print(f"S_{n+1} =", Sn_next)
    Sn = Sn_next  # mise à jour

# Affichage finale
print("\nMémoire :")
for i, state in enumerate(memory):
    print(f"  S_{i+1} = {state}")
