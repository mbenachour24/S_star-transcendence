import numpy as np
import multiprocessing as mp
from mpmath import mpf, sin, cos, pslq
import pandas as pd
from tqdm import tqdm

mp.dps = 50  # High precision

def compute_attractor(a, b, s0=1.0, steps=200):
    s = mpf(s0)
    for _ in range(steps):
        s = a * sin(s) + b * cos(s)
    return s

def is_transcendental(s_star, degree=6, tol=1e-30):
    coeffs = [s_star**i for i in range(degree + 1)]
    relation = pslq(coeffs, tol)
    return relation is None

def process_point(params):
    a, b = params
    try:
        s_star = compute_attractor(mpf(a), mpf(b))
        transcendental = is_transcendental(s_star)
        return (a, b, float(s_star), int(transcendental))
    except Exception as e:
        print(f"Error processing point ({a}, {b}): {e}")
        return (a, b, None, None)

if __name__ == '__main__':
    a_vals = np.linspace(-100, 100, 200)
    b_vals = np.linspace(-100, 100, 200)
    grid = [(a, b) for a in a_vals for b in b_vals]

    with mp.Pool(processes=mp.cpu_count()) as pool:
        results = list(tqdm(pool.imap(process_point, grid), total=len(grid)))

    df = pd.DataFrame(results, columns=['a', 'b', 'S_star', 'transcendental'])
    df.to_csv("attractors_transcendental_sweep.csv", index=False)
    print("✅ Sweep terminé. Résultats enregistrés dans attractors_transcendental_sweep.csv.")
