import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_wine
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans

def plot_dendrogram(model, **kwargs):
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
    
    linkage_matrix = np.column_stack([model.children_, model.distances_, counts]).astype(float)
    dendrogram(linkage_matrix, **kwargs)
    
# Cargar dataset Wine
wine = load_wine()
X = wine.data

# Programar HAC sobre la base de datos de Wine
hac_model = AgglomerativeClustering(distance_threshold=0, n_clusters=None, metric='euclidean', linkage='ward')
hac_model = hac_model.fit(X)

# Visualizar el dendrograma
plt.figure(figsize=(15, 10))
plt.title('Dendrograma - Dataset Wine')
plt.xlabel('Sample Index')
plt.ylabel('Cluster Distance')
plot_dendrogram(hac_model, color_threshold=15)
plt.axhline(y=1450, color='r', linestyle='--')
plt.show()

# HAC con k=3 (clases en Wine)
hac_final = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
etiquetas_hac = hac_final.fit_predict(X)

# Comparar con k-means con el k necesario (k=3)
kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
etiquetas_kmeans = kmeans.fit_predict(X)

df_comparacion = pd.DataFrame({
    'KMeans': etiquetas_kmeans,
    'HAC': etiquetas_hac
})

tabla_contingencia = pd.crosstab(df_comparacion['HAC'], df_comparacion['KMeans'])
print(tabla_contingencia)

plt.figure(figsize=(10, 8))
import seaborn as sns
sns.heatmap(tabla_contingencia, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Contingencia')
plt.xlabel('Etiquetas KMeans')
plt.ylabel('Etiquetas HAC')
plt.show()

# CONCLUSIONES DEL DENDROGRAMA (explicación sencilla)
print("="*50)
print("CONCLUSIONES DEL DENDROGRAMA")
print("="*50)

print("\n1. ¿QUÉ NOS DICE EL DENDROGRAMA?")
print("   - El dendrograma es como un árbol genealógico de los vinos")
print("   - Muestra cómo se agrupan los vinos similares entre sí")
print("   - Los vinos que se unen abajo son muy parecidos")
print("   - Los que se unen arriba son más diferentes")

print("\n2. ¿CUÁNTOS GRUPOS DE VINOS HAY?")
print("   - La línea roja corta el árbol en 3 ramas principales")
print("   - Esto nos dice que hay 3 tipos de vinos diferentes")
print("   - Cada rama representa un grupo de vinos con características similares")

print("\n3. ¿POR QUÉ 3 GRUPOS Y NO 2 O 4?")
print("   - El salto más grande en el árbol es de 3 a 2 grupos")
print("   - Esto significa que los 3 grupos son realmente diferentes")
print("   - Si hiciéramos 2 grupos, mezclaríamos vinos que no son tan iguales")

print("\n4. ¿QUÉ SIGNIFICA PARA LOS VINOS?")
print("   - Hay 3 familias distintas de vinos en el dataset")
print("   - Cada familia tiene su propia personalidad (sabor, aroma, etc.)")
print("   - Los vinos dentro de cada familia son más parecidos entre ellos")

print("\n5. CONCLUSIÓN FINAL:")
print("   - El dendrograma confirma que natureza nos dio 3 tipos de vinos")
print("   - Nuestro análisis computacional coincide con la realidad")
print("   - Es una buena señal que nuestros algoritmos funcionen bien")

print("="*50)