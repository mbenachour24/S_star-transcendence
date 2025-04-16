import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Nouvelle approche : laisser le modèle découvrir l'invariant computationnel
class MetaInvariantAutoencoder(nn.Module):
    def __init__(self):
        super(MetaInvariantAutoencoder, self).__init__()
        # Encodeur : plus de dimensions pour capturer plus d'invariants
        self.encoder = nn.Sequential(
            nn.Linear(1, 20),
            nn.ReLU(),
            nn.Linear(20, 10),
            nn.ReLU(),
            nn.Linear(10, 5),
            nn.ReLU(),
            nn.Linear(5, 3)  # Espace latent plus large
        )
        # Décodeur
        self.decoder = nn.Sequential(
            nn.Linear(3, 5),
            nn.ReLU(),
            nn.Linear(5, 10),
            nn.ReLU(),
            nn.Linear(10, 20),
            nn.ReLU(),
            nn.Linear(20, 1)
        )
    
    def forward(self, x):
        latent = self.encoder(x)
        reconstructed = self.decoder(latent)
        return latent, reconstructed

# Nouvelle fonction de perte : on ne contraint pas un invariant spécifique
# On impose seulement une stabilité structurelle

def loss_meta(latent, reconstructed, input_value, model, lambda_reg=0.001):
    loss_reconstruction = torch.mean((reconstructed - input_value) ** 2)
    loss_stability = torch.mean(torch.abs(latent - torch.mean(latent, dim=0)))  # Encourage une structure stable
    l2_reg = sum(p.pow(2.0).sum() for p in model.parameters())
    return loss_reconstruction + loss_stability + lambda_reg * l2_reg

# Initialisation du réseau
model = MetaInvariantAutoencoder()
optimizer = optim.Adam(model.parameters(), lr=0.005, weight_decay=0.001)

# Stockage pour visualisation
latent_values = []
losses = []

# Générer des entrées aléatoires
num_samples = 5000
input_values = torch.tensor(np.random.uniform(-2, 2, (num_samples, 1)), dtype=torch.float32)

# Entraînement avec minibatchs
batch_size = 32
for epoch in range(2000):
    indices = np.random.choice(num_samples, batch_size, replace=False)
    batch_inputs = input_values[indices]
    
    optimizer.zero_grad()
    latent, reconstructed = model(batch_inputs)
    loss = loss_meta(latent, reconstructed, batch_inputs, model)
    loss.backward()
    optimizer.step()
    
    latent_values.append(latent.detach().numpy())
    losses.append(loss.item())
    
    if epoch % 200 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.6f}, Example Latent: {latent[0].detach().numpy()}, Reconstructed: {reconstructed[0].item():.6f}")

# Convertir les latents en numpy
latent_values = np.array(latent_values).squeeze()

# Assurer que latent_values a bien la forme (n, 3)
latent_values = latent_values.reshape(-1, 3)

# Clustering avec K-Means pour voir s'il y a des attracteurs computationnels spontanés
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(latent_values)
labels = kmeans.labels_

# Visualisation des clusters
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(latent_values[:, 0], latent_values[:, 1], latent_values[:, 2], c=labels, cmap='viridis', alpha=0.5)
ax.set_xlabel('Latent Dim 1')
ax.set_ylabel('Latent Dim 2')
ax.set_zlabel('Latent Dim 3')
ax.set_title('Clustering des représentations latentes (sans contrainte explicite)')
plt.show()

# Affichage des centres des clusters
print("Centres des clusters (attracteurs computationnels potentiels) :")
print(kmeans.cluster_centers_)

# Visualisation de la perte
plt.figure(figsize=(8, 6))
plt.plot(losses, label='Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Évolution de la perte (sans contrainte explicite)')
plt.legend()
plt.show()
