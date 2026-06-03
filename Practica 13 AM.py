import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering

def plot_dendogram(model, **kwargs):
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    dendrogram(linkage_matrix, **kwargs)

iris = load_iris()
X = iris.data

hac_model = AgglomerativeClustering(distance_threshold=0, n_clusters=None, metric = 'euclidean', linkage= 'ward')
hac_model = hac_model.fit(X)

plt.figure(figsize=(15, 10))
plt.title("Dendrograma")
plt.xlabel("Sample Index")
plt.ylabel("Cluster Distance")
plot_dendogram(hac_model, color_threshold=10)
plt.axhline(y=10, color='r', linestyle='--')
plt.show()

hac_final = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
etiquetas = hac_final.fit_predict(X)

#kmeans
from sklearn.cluster import KMeans
import seaborn as sns

kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
etiquetas_kmeans = kmeans.fit_predict(X)

df_comparacion = pd.DataFrame({
    'K-means': etiquetas_kmeans,
    'HAC': etiquetas
})

tabla_contingencia = pd.crosstab(df_comparacion['HAC'], df_comparacion['K-Means'])
print(tabla_contingencia)

plt.figure(figsize=(10, 8))
sns.heatmap(tabla_contingencia, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Contingencia')
plt.xlabel('Etiquetas K-Means')
plt.ylabel('Etiquetas HAC')
plt.show()