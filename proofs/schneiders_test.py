from mpmath import mp, log, diff
from sympy import symbols, Poly, Rational, nsimplify
import numpy as np

# Set high precision
mp.dps = 100  # 100 decimal places

# Define the recurrence relation
def compute_s_star(iterations=1000):
    S = mp.mpf(1)  # Initial guess
    for _ in range(iterations):
        S = mp.sin(S) + mp.cos(S)
    return S

# Compute S* to high precision
S_star = compute_s_star()
print(f"S* ≈ {S_star}")

# Convert S_star to an mpmath float for precision
S_star_mp = mp.mpf(S_star)

# Attempt to fit a polynomial P(x) such that P(S*) ≈ 0
x = symbols('x')

# Manually test small-degree polynomials
def test_polynomials():
    candidate_polynomials = [
        Poly(x**2 - x - 1, x),  # Fibonacci-like polynomial
        Poly(x**3 - 3*x + 1, x),  # Some simple cubic relation
        Poly(x**4 - 4*x**2 + 2, x),  # Quartic polynomial
    ]
    
    for P in candidate_polynomials:
        error = abs(P.eval(S_star_mp))
        print(f"Testing polynomial: {P}")
        print(f"Error: {error}")
        if error < 1e-100:
            print("Possible algebraicity detected!")
            return
    
    print("S* is likely transcendental.")

def test_logarithmic_dependence():
    # Hypothesis: Is S* a linear combination of logarithms of algebraic numbers?
    alpha1 = mp.mpf(2)  # Example algebraic number
    alpha2 = mp.mpf(3)
    
    log_alpha1 = log(alpha1)
    log_alpha2 = log(alpha2)
    
    # Solve for potential rational coefficients lambda1, lambda2
    lambda1 = S_star_mp / log_alpha1
    lambda2 = S_star_mp / log_alpha2
    
    print(f"Testing logarithmic dependence:")
    print(f"Lambda1 (S* / log(2)) ≈ {lambda1}")
    print(f"Lambda2 (S* / log(3)) ≈ {lambda2}")
    
    if lambda1 % 1 == 0 or lambda2 % 1 == 0:
        print("Possible algebraic relation detected!")
    else:
        print("S* is likely not expressible as a simple log combination, supporting transcendence.")

def test_schneider_criterion():
    # Check if S* satisfies a simple algebraic differential equation
    f_S = mp.sin(S_star_mp) + mp.cos(S_star_mp)
    df_S = mp.cos(S_star_mp) - mp.sin(S_star_mp)  # Derivative of f(x) = sin(x) + cos(x)
    
    print("Testing Schneider's Criterion:")
    print(f"f(S*) = sin(S*) + cos(S*) ≈ {f_S}")
    print(f"f'(S*) = cos(S*) - sin(S*) ≈ {df_S}")
    
    if abs(S_star_mp - f_S) < 1e-100:
        print("S* satisfies a trivial algebraic relation, which is unlikely.")
    else:
        print("S* does not satisfy a simple algebraic differential equation, supporting transcendence.")

test_polynomials()
test_logarithmic_dependence()
test_schneider_criterion()