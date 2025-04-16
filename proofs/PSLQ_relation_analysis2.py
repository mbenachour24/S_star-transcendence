from mpmath import mp, mpf, pslq, nstr

# Set precision (number of decimal places)
mp.dps = 100  # You can increase this for more precision

# Define the constant S* numerically
S_star = mpf("1.2587281774926764586391391659652309706518781824732")

# Maximum degree to test
max_degree = 100

# Threshold for residue (how close to zero the polynomial should evaluate)
residue_threshold = mpf("1e-40")

# Try to find a minimal integer relation
for degree in range(2, max_degree + 1):
    # Construct vector [1, x, x^2, ..., x^n]
    vec = [S_star ** i for i in range(degree + 1)]

    # Use PSLQ to find integer relation
    relation = pslq(vec, maxcoeff=int(1e10))
    
    if relation:
        # Compute the residue of the found polynomial at S*
        residue = sum([c * S_star ** i for i, c in enumerate(relation)])

        if abs(residue) < residue_threshold:
            print(f"\n✅ Relation found at degree ≤ {degree} with residue ≈ {nstr(residue, 3)}")
            poly_str = " + ".join(f"{c}·x^{i}" for i, c in enumerate(relation) if c != 0)
            print("Polynomial approximation:")
            print("P(x) =", poly_str)
            break
else:
    print("❌ No algebraic relation found up to degree", max_degree)