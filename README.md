# 🧠 S* Transcendence

**A computational, mathematical, and visual investigation of the transcendental invariant:**

`S* = limₙ→∞ ( sin(Sₙ) + cos(Sₙ) )`

---

## 📐 Objective

This project aims to experimentally and computationally demonstrate the **transcendence of \( S^* \)**—a recursively generated fixed point from the coupling of trigonometric functions. It does so through:

- **Polynomial approximations (LLL)**
- **Dependency testing (PSLQ)**
- **Autopoietic simulations**
- **High-precision visualizations**
- **Stability and convergence analysis**

---

## 🧬 Project Structure

```bash
.
├── AI/                    # Recursive cognition, symbolic prototypes
├── proofs/                # Analytical proofs (LLL, PSLQ, stability, Lyapunov)
├── visualizations/        # Heatmaps, 3D surfaces, animations, convergence plots
├── simulations/           # Recursive systems, institutional or coupled models
├── drafts/                # Experimental runs, logs, early-stage explorations
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🔍 Key Files

- `proofs/PSLQ_relation_analysis.py` — Checks PSLQ relations to π, e, ln(2), γ
- `proofs/algebraic_LLL.py` — Attempts to find polynomial annihilators for \( S^* \)
- `proofs/stability_test_S_star.py` — Local derivative-based stability analysis
- `visualizations/heatmap_dense_attractors_ab_plane.py` — Dense 2D map of \( S^* \) over \((a,b)\)
- `visualizations/attractor_surface_plot_3d.py` — 3D surface projection of attractors
- `simulations/recursive_coupling_sim.py` — Multi-agent recursive coupling simulation

---

## 📦 Installation

### 1. Clone the project

```bash
git clone https://github.com/your-username/S_star-transcendence.git
cd S_star-transcendence
```

### 2. Create a virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🧠 Hypothesis

> If a fixed point emerges from structurally coupled recursive functions (e.g., \( \sin \) and \( \cos \)), and that point resists algebraic detection via PSLQ and LLL even at high precision, it is likely **transcendental**—and models a **computational transcendental** invariant.

---

## 🔬 Philosophy

This project sits at the crossroads of:

- Computational epistemology
- Systems theory (inspired by Luhmann)
- Recursive transcendental philosophy
- Experimental mathematics
- Synthetic normativity and legal simulation

---

## 📚 Dependencies

- `numpy`, `matplotlib`, `mpmath`, `sympy`, `fpylll`, `pylatex`, `tqdm`
- Python 3.11+ is recommended

---

## ✍️ Author

**Mohamed Ben Achour** — Philosopher-engineer. 
Part of the broader research initiative **Optimus: Coding the State**.
contact me : mbenachour24@gmail.com

> *"Transcendence is not what lies beyond, but what emerges from within the repetition of logic over structure."*

---

## 🔗 Related Repositories & Platforms

- 🌐 [Optimus Live Platform](https://optimus-software.onrender.com/) — Real-time demonstration of institutional dynamics.
- 🧠 [OPTIMUS_projects](https://github.com/mbenachour24/OPTIMUS_projects) — Central research hub for simulations of governance and law.
- 💻 [OPTIMUS-software](https://github.com/mbenachour24/OPTIMUS-software) — Base code for recursive institutional modeling.
- 🔬 [IRS-SIM](https://github.com/mbenachour24/IRS-SIM) — Simulation of recursive institutional systems under stress.
- 📚 [optimus.lib](https://github.com/mbenachour24/optimus.lib) — Core library for structural recursion and systemic simulation.

## 📜 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license.

> You are free to share and adapt the material for non-commercial purposes, with proper attribution.  
> Commercial use and proprietary appropriation are strictly prohibited.

[View License Summary](https://creativecommons.org/licenses/by-nc/4.0/)  
© Mohamed Ben Achour. All rights reserved.
