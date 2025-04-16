from sympy import sin, cos, nsolve, Symbol

# Define the symbol and the equation
S = Symbol('S', real=True)
eq = sin(S) + cos(S) - S

# Solve for S* with high precision
S_star = nsolve(eq, S, 1.0, prec=50)

# Print the result
print(f"The value of S* is: {S_star}")
