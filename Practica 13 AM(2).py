#kmeans
from sklearn.cluster import KMeans
import seaborn as sns
import importlib.util
spec = importlib.util.spec_from_file_location("practica_13_AM", "/home/rogeliovc/Uni/Practica 13 AM.py")
prac = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prac)
import matplotlib.pyplot as plt
import pandas as pd

kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
etiquetas_kmeans = kmeans.fit_predict(prac.X)

df_comparacion = pd.DataFrame({
    'K-means': etiquetas_kmeans,
    'HAC': prac.etiquetas
})

tabla_contingencia = pd.crosstab(df_comparacion['HAC'], df_comparacion['K-means'])
print(tabla_contingencia)

plt.figure(figsize=(10, 8))
sns.heatmap(tabla_contingencia, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Contingencia')
plt.xlabel('Etiquetas K-Means')
plt.ylabel('Etiquetas HAC')
plt.show()