import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import load_diabetes

# 1. Cargar la base de datos de diabetes
diabetes = load_diabetes()

# 2. Usar la primer columna y solo 100 instancias
X = diabetes.data[:100, 0].reshape(-1, 1)
y = diabetes.target[:100]

# 3. Generar una línea con valores posibles de X para visualizar la predicción
X_lineal = np.linspace(X.min(), X.max(), 500).reshape(-1, 1)

# Configuraciones solicitadas
valores_k = [1, 5, 15]
distancias = ['euclidean', 'manhattan']

# Crear figura para los gráficos (2 filas para distancias, 3 columnas para valores K)
fig, axes = plt.subplots(nrows=len(distancias), ncols=len(valores_k), figsize=(15, 10))
fig.suptitle('KNN Regresión en Dataset Diabetes\n(100 instancias, 1ra característica)', fontsize=16)

# Iterar sobre las distancias y los valores de K
for i, distancia in enumerate(distancias):
    for j, k in enumerate(valores_k):
        
        # 4. Entrenar el modelo con el K y la distancia correspondiente
        knn = KNeighborsRegressor(n_neighbors=k, metric=distancia)
        knn.fit(X, y)
        
        # 5. Predecir para cada punto en la línea
        y_pred = knn.predict(X_lineal)
        
        # 6. Mostrar la línea de predicciones en el subgráfico correspondiente
        ax = axes[i, j]
        ax.scatter(X, y, color='gray', alpha=0.6, label='Datos Reales')
        
        # Usaremos rojo para euclidiana y azul para manhattan
        color_linea = 'red' if distancia == 'euclidean' else 'blue'
        ax.plot(X_lineal, y_pred, color=color_linea, linewidth=2, label=f'Predicción')
        
        ax.set_title(f'K = {k} | Distancia: {distancia.capitalize()}')
        ax.set_xlabel('Característica 0')
        ax.set_ylabel('Progresión de la enfermedad')
        ax.legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajustar espaciado para el título principal
plt.show()