import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# ==================================
# 1️⃣ Autoencodeur Autopoïétique
# ==================================
class RecursiveAutoencoder(nn.Module):
    def __init__(self):
        super(RecursiveAutoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(1, 20), nn.ReLU(),
            nn.Linear(20, 10), nn.ReLU(),
            nn.Linear(10, 5), nn.ReLU(),
            nn.Linear(5, 3)
        )
        self.decoder = nn.Sequential(
            nn.Linear(3, 5), nn.ReLU(),
            nn.Linear(5, 10), nn.ReLU(),
            nn.Linear(10, 20), nn.ReLU(),
            nn.Linear(20, 1)
        )
    
    def forward(self, x):
        latent = self.encoder(x)
        reconstructed = self.decoder(latent)
        return latent, reconstructed

# ==================================
# 2️⃣ Société Récursive : Agents Couplés
# ==================================
class RecursiveSociety:
    def __init__(self, num_agents=3):
        self.agents = [RecursiveAutoencoder() for _ in range(num_agents)]
        self.optimizers = [optim.Adam(agent.parameters(), lr=0.005, weight_decay=0.001) for agent in self.agents]
        self.num_agents = num_agents
    
    def recursive_update(self, latents):
        """
        Implémente une loi de couplage structurel entre agents.
        """
        latents_stack = torch.stack([l.clone().detach() for l in latents])
        moyenne = torch.mean(latents_stack, dim=0)
        new_latents = [(latents[i].clone() + moyenne.clone()) / 2 for i in range(self.num_agents)]
        return new_latents
    
    def train(self, input_values, epochs=2000, batch_size=32):
        torch.autograd.set_detect_anomaly(True)  # Détecte les erreurs de gradient
        losses = []
        latent_history = []
        num_samples = input_values.shape[0]
        
        for epoch in range(epochs):
            indices = np.random.choice(num_samples, batch_size, replace=False)
            batch_inputs = input_values[indices]
            
            latents = []
            for agent in self.agents:
                latent, _ = agent(batch_inputs)
                latents.append(latent.clone())  # Évite toute modification in-place
            
            new_latents = self.recursive_update(latents)
            loss_epoch = 0
            
            for i, agent in enumerate(self.agents):
                self.optimizers[i].zero_grad()
                _, reconstructed = agent(batch_inputs)
                loss = torch.mean((reconstructed - batch_inputs) ** 2) + torch.mean(torch.abs(new_latents[i] - latents[i]))
                
                # Fix backward issue
                loss.backward(retain_graph=True if i < self.num_agents - 1 else False)  
                self.optimizers[i].step()
                loss_epoch += loss.item()
            
            latent_history.append(torch.cat([l.clone().detach() for l in new_latents]).cpu().numpy())
            losses.append(loss_epoch / self.num_agents)
            
            if epoch % 200 == 0:
                print(f"Epoch {epoch}, Loss: {loss_epoch / self.num_agents:.6f}")
        
        return np.array(latent_history), losses

# ==================================
# 3️⃣ Génération de S* par récurrence
# ==================================
def generate_s_star_sequence(n_iter=500, s0=1.0):
    """
    Génère une séquence récurrente de S* définie par S_{n+1} = sin(S_n) + cos(S_n)
    """
    S_values = [s0]
    for _ in range(n_iter):
        S_values.append(np.sin(S_values[-1]) + np.cos(S_values[-1]))
    return np.array(S_values)

# ==================================
# 4️⃣ Exécution de la simulation
# ==================================
num_samples = 5000
input_values = torch.tensor(np.random.uniform(-2, 2, (num_samples, 1)), dtype=torch.float32)

society = RecursiveSociety(num_agents=3)
latent_history, losses = society.train(input_values)

# ==================================
# 5️⃣ Clustering des latents finaux
# ==================================

# Reshape latent_history pour le clustering
latent_reshaped = latent_history.reshape(latent_history.shape[0], -1, 3)
final_latents = latent_reshaped[-1]  # Prendre la dernière époque

# Clustering des latents finaux
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(final_latents)
labels = kmeans.labels_

# ==================================
# 6️⃣ Superposition avec S*
# ==================================
S_star_seq = generate_s_star_sequence(n_iter=min(500, final_latents.shape[0]))

# Visualisation des clusters avec correction
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot avec les bons labels
scatter = ax.scatter(
    final_latents[:, 0], 
    final_latents[:, 1], 
    final_latents[:, 2], 
    c=labels,  # Labels des clusters
    cmap='viridis', 
    alpha=0.7,
    s=30  # Taille des points
)

# Ajout de la séquence de S*
seq_length = min(len(S_star_seq), 100)  # Limiter pour la visualisation
S_star_seq_limited = S_star_seq[:seq_length]
ax.plot(
    S_star_seq_limited, 
    np.zeros_like(S_star_seq_limited), 
    np.zeros_like(S_star_seq_limited), 
    'r-', 
    linewidth=2, 
    label="S* Sequence"
)

ax.set_xlabel('Latent Dim 1')
ax.set_ylabel('Latent Dim 2')
ax.set_zlabel('Latent Dim 3')
ax.set_title('Société computationnelle : émergence de normes computationnelles')
ax.legend()

# Ajouter une légende pour les clusters
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="upper right", title="Clusters")
ax.add_artist(legend1)

# ==================================
# 7️⃣ Convergence des latents vers S*
# ==================================

# Correction des dimensions avant calcul de la distance
min_length = min(latent_history.shape[0], S_star_seq.shape[0])
S_star_seq_truncated = S_star_seq[:min_length]

# Ajustement des dimensions pour correspondre à latent_history
S_star_seq_truncated = S_star_seq_truncated.reshape(-1, 1, 1)  # (min_length, 1, 1)

# Calcul des distances entre les latents et la séquence S*
distances = np.linalg.norm(latent_history[:min_length] - S_star_seq_truncated, axis=2)

# Visualisation de la convergence
plt.figure(figsize=(10, 6))
plt.plot(np.mean(distances, axis=1), label="Distance moyenne des latents à S*")
plt.xlabel("Epochs")
plt.ylabel("Distance à S*")
plt.title("Convergence des latents vers S*")
plt.legend()
plt.show()

# ==================================
# 8️⃣ Évolution de la perte
# ==================================
plt.figure(figsize=(8, 6))
plt.plot(losses, label='Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Évolution de la perte (Société computationnelle récursive)')
plt.legend()
plt.tight_layout()

plt.show()