import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load and clean
df = pd.read_csv("attractors_transcendental_sweep.csv")

# ⚠️ Supprimer toutes les lignes avec NaN ou Inf
df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=["a", "b", "transcendental"])
df.to_csv("attractors_transcendental_sweep.csv", index=False)

# Pivot table pour visualiser (matrice a x b)
pivot = df.pivot_table(index="b", columns="a", values="transcendental")

# Reconvertir en array numpy pour imshow
heatmap = pivot.to_numpy()

# Récupérer les axes pour extent
a_vals = pivot.columns.values
b_vals = pivot.index.values

# Tracer la heatmap
plt.figure(figsize=(10, 8))
plt.imshow(heatmap, extent=[a_vals.min(), a_vals.max(), b_vals.min(), b_vals.max()],
           origin='lower', cmap='hot', aspect='auto')
plt.colorbar(label='1 = Transcendental, 0 = Algebraic')
plt.title("Zones Transcendantales dans S* pour Sₙ₊₁ = a·sin(Sₙ) + b·cos(Sₙ)")
plt.xlabel("a")
plt.ylabel("b")
plt.tight_layout()
plt.savefig("transcendental_heatmap.png")
plt.show()
