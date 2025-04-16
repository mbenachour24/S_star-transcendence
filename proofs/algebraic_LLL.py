from mpmath import mp
from fpylll import IntegerMatrix, LLL

mp.dps = 50
S_star = mp.mpf('-0.26048100102248595')
degree = 6
precision = 50
scale = 10 ** precision

# Construction de la matrice
M = IntegerMatrix(degree + 2, degree + 2)
for i in range(degree + 1):
    for j in range(degree + 2):
        M[i, j] = 0
    M[i, i] = scale

for j in range(degree + 1):
    M[degree + 1, j] = int(S_star ** j * scale)
M[degree + 1, degree + 1] = 1

# Application de LLL
basis = LLL.reduction(M)
coeffs = list(basis[0])[:-1]
val = sum(c * (S_star ** i) for i, c in enumerate(coeffs))

print("Polynôme détecté :", coeffs)
print("Évaluation numérique :", val)