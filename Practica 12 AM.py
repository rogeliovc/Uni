import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_wine
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score, davies_bouldin_score

wine = load_wine()
X_all = wine.data
X_vis = wine.data[:, :2]

k_values = range(1, 6)
silhouette_scores = []
davies_bouldin_scores = []
etiquetas_por_k = {}
kmeans_por_k = {}

mejor_k_sil = None
mejor_silhouette = -1
mejor_k_db = None
mejor_db = float('inf')

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init = 'auto')
    etiquetas = kmeans.fit_predict(X_all)

    kmeans_por_k[k] = kmeans
    etiquetas_por_k[k] = etiquetas

    print(f" Para k={k}:") 
    
    if k == 1:
        print(f" Silhouette Score: No aplicable (se necesitan al menos 2 clústeres)")
        print(f" Davies-Bouldin Score: No aplicable (se necesitan al menos 2 clústeres)")
        silhouette_scores.append(-1)  # Valor inválido para k=1
        davies_bouldin_scores.append(float('inf'))  # Valor inválido para k=1
    else:
        score_sil = silhouette_score(X_all, etiquetas)
        score_db = davies_bouldin_score(X_all, etiquetas)
        silhouette_scores.append(score_sil)
        davies_bouldin_scores.append(score_db)
        
        print(f" Silhouette Score: {score_sil}") 
        print(f" Davies-Bouldin Score: {score_db}")

        if score_sil > mejor_silhouette:
            mejor_silhouette = score_sil
            mejor_k_sil = k
        
        if score_db < mejor_db:
            mejor_db = score_db
            mejor_k_db = k

print(f"\n Mejor k según Silhouette: {mejor_k_sil} (score: {mejor_silhouette})")
print(f" Mejor k según Davies-Bouldin: {mejor_k_db} (score: {mejor_db})")

if mejor_k_sil == mejor_k_db:
    print(f" Ambas métricas coinciden: el mejor k es {mejor_k_sil}")
else:
    print(f" Las métricas no coinciden. Silhouette sugiere k={mejor_k_sil}, Davies-Bouldin sugiere k={mejor_k_db}")
    print(f" Se usará k={mejor_k_sil} para visualización (mayor Silhouette)")

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

etiquetas_mejor = etiquetas_por_k[mejor_k_sil]
sample_silhouette_values = silhouette_samples(X_vis, etiquetas_mejor)

y_lower = 10
colores_dict = {0: 'red', 1: 'blue', 2: 'green', 3: 'yellow'}

for i in range(mejor_k_sil):
    ith_cluster_silhouette_values = sample_silhouette_values[etiquetas_mejor == i]
    ith_cluster_silhouette_values.sort()

    size_cluster_i = ith_cluster_silhouette_values.shape[0]
    y_upper = y_lower + size_cluster_i

    color = colores_dict.get(i, '#333333')
    ax1.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values, facecolor=color, edgecolor=color)

    ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
    y_lower = y_upper + 10

ax1.set_xlabel("Silhouette Coefficient Values")
ax1.set_ylabel("Cluster Labels")
ax1.axvline(x=mejor_silhouette, color="red", linestyle="--")
ax1.set_yticks([])
ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax1.set_xlim([-0.1, 1.0])

ax2.plot(k_values, silhouette_scores, marker='o')
ax2.set_xlabel('Número de Clusters (k)')
ax2.set_ylabel('Silhouette Score')
ax2.set_xticks(k_values)
ax2.grid(axis='both')

ax3.plot(k_values, davies_bouldin_scores, marker='o')
ax3.set_xlabel('Número de Clusters (k)')
ax3.set_ylabel('Davies-Bouldin Score')
ax3.set_xticks(k_values)
ax3.grid(axis='both')
plt.tight_layout()
plt.show()