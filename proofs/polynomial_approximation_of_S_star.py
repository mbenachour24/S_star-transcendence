from mpmath import mp
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

test_polynomials()
