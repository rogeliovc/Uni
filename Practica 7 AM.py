import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Cargar el dataset de Vinos
wine = load_wine()
# Usamos solo las dos primeras características (Alcohol y Ácido Málico) para poder graficar en 2D
X = wine.data[:, :2] 
y = wine.target
class_names = wine.target_names

# 2. Dividir los datos (70% entrenamiento, 30% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ==========================================
# 3. MODELO 1: DISTANCIA EUCLIDIANA (p=2)
# ==========================================
knn_euclidean = KNeighborsClassifier(n_neighbors=3, metric='euclidean') # o p=2
knn_euclidean.fit(X_train, y_train)
y_pred_euc = knn_euclidean.predict(X_test)

print("--- RESULTADOS DISTANCIA EUCLIDIANA ---")
print(f"Precisión global = {accuracy_score(y_test, y_pred_euc):.4f}")
print(classification_report(y_test, y_pred_euc, target_names=class_names))

# ==========================================
# 4. MODELO 2: DISTANCIA DE MANHATTAN (p=1)
# ==========================================
knn_manhattan = KNeighborsClassifier(n_neighbors=3, metric='manhattan') # o p=1
knn_manhattan.fit(X_train, y_train)
y_pred_man = knn_manhattan.predict(X_test)

print("--- RESULTADOS DISTANCIA DE MANHATTAN ---")
print(f"Precisión global = {accuracy_score(y_test, y_pred_man):.4f}")
print(classification_report(y_test, y_pred_man, target_names=class_names))

# ==========================================
# 5. GRÁFICA DE FRONTERAS (Usando el modelo Euclidiano)
# ==========================================
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

# Malla de puntos para dibujar las regiones
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.05), np.arange(y_min, y_max, 0.05))

# Predecir sobre cada punto de la malla (Cambiamos 'knn' por 'knn_euclidean')
Z = knn_euclidean.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap='viridis', s=50)
plt.title("KNN (k=3) - Dataset Wine (Distancia Euclidiana)")
plt.xlabel(wine.feature_names[0])
plt.ylabel(wine.feature_names[1])
plt.show()