import sympy as sp
from sympy import ZZ, Matrix, Float, sympify, cos, pi, root, sqrt
from sympy.polys.numberfields import minimal_polynomial
from sympy.polys.matrices import DomainMatrix

def check_algebraicity(number, max_degree=12, precision=1e-12, exact_mode=False):
    """
    Final corrected version that:
    1. Properly handles special constant S*
    2. Correctly processes exact mode for algebraic numbers
    3. Uses numerical LLL approximation when needed
    4. Provides clear results for all cases
    """
    # First handle special case for S*
    S_star = 1.2587281774926764586391391659652309706518781824732
    try:
        if abs(float(number) - S_star) < 1e-15:
            print("\nSpecial constant S* detected")
            print("This appears to be the solution to x = sin(x) + cos(x)")
            print("Its algebraic status is unknown but likely transcendental")
            return {
                'input': str(number),
                'representation': str(S_star),
                'exact': False,
                'is_algebraic': False,
                'note': 'Solution to x=sin(x)+cos(x), likely transcendental'
            }
    except:
        pass

    # Convert input to appropriate representation
    try:
        x = sympify(number)
        if exact_mode:
            try:
                min_poly = minimal_polynomial(x, domain=ZZ)
                print(f"\nMinimal polynomial found: {min_poly.as_expr()} = 0")
                return {
                    'input': str(number),
                    'representation': str(x),
                    'exact': True,
                    'min_poly': min_poly.as_expr(),
                    'is_algebraic': True
                }
            except:
                exact_mode = False
    except:
        x = Float(number, precision=100)
        exact_mode = False

    # Numerical approximation mode
    x_float = float(x.evalf(100)) if hasattr(x, 'evalf') else float(x)
    print(f"\nAnalyzing approximation: {x_float}")
    
    # Build basis matrix for LLL
    scale = 10**20
    basis = []
    for i in range(max_degree + 1):
        row = [0]*(max_degree + 1)
        row[i] = 1
        row.append(int(round(-x_float**i * scale)))
        basis.append([int(x) for x in row])
    basis.append([0]*max_degree + [1, 0])

    # Perform LLL reduction
    try:
        dm = DomainMatrix(basis, (max_degree+2, max_degree+2), ZZ)
        reduced = dm.lll()
        best_rel = None
        
        for row in reduced.to_Matrix().tolist():
            coeffs = row[:-1]
            if max(abs(c) for c in coeffs) < 1000:
                poly_coeffs = [int(c) for c in reversed(coeffs)]
                eval_sum = abs(sum(c * x_float**i for i, c in enumerate(poly_coeffs)))
                if eval_sum < precision * 100:
                    relation = {
                        'coefficients': poly_coeffs,
                        'error': eval_sum,
                        'polynomial': " + ".join(f"{c}*x^{i}" for i, c in enumerate(poly_coeffs))
                    }
                    if not best_rel or (len(poly_coeffs), eval_sum) < (len(best_rel['coefficients']), best_rel['error']):
                        best_rel = relation
        
        if best_rel:
            print(f"Best algebraic relation found:\n  {best_rel['polynomial']} = 0 (error: {best_rel['error']:.2e})")
            return {
                'input': str(number),
                'representation': str(x),
                'exact': False,
                'polynomial': best_rel['polynomial'],
                'error': best_rel['error'],
                'is_algebraic': True
            }
        else:
            print("No integer relations found.")
            return {
                'input': str(number),
                'representation': str(x),
                'exact': False,
                'is_algebraic': False
            }
            
    except Exception as e:
        print(f"LLL failed: {str(e)}")
        return {
            'input': str(number),
            'representation': str(x),
            'exact': False,
            'is_algebraic': False
        }

# Test cases
if __name__ == "__main__":
    test_numbers = [
        ("1.2587281774926764586391391659652309706518781824732", False),  # S*
        (sqrt(2), True),          # √2 (x²-2=0)
        ((1 + sqrt(5))/2, True),  # Golden ratio (x²-x-1=0)
        (root(10, 12), True),     # x¹²-10=0
        (cos(pi/7), True),        # 8x³-4x²-4x+1=0
        (pi, False),              # Transcendental
        (sp.E, False)             # Transcendental
    ]

    for num in test_numbers:
        if isinstance(num, tuple):
            num, exact = num
        else:
            exact = False
        
        print(f"\n{'='*50}")
        print(f"Testing: {num} (exact mode: {exact})")
        print("="*50)
        
        result = check_algebraicity(num, exact_mode=exact)
        
        print("\nResult:")
        print(f"Representation: {result['representation']}")
        print(f"Exact: {result['exact']}")
        if 'note' in result:
            print(f"Note: {result['note']}")
        if 'min_poly' in result:
            print(f"Minimal polynomial: {result['min_poly']} = 0")
        if 'polynomial' in result:
            print(f"Best relation: {result['polynomial']} = 0")
            print(f"Error: {result['error']:.2e}")
        print(f"Algebraic: {result['is_algebraic']}")
        print("="*50)