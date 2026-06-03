import numpy as np
from sklearn.datasets import load_iris

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def umbral(a):
    return 1 if a >= 0.5 else 0

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Select only the last two classes (classes 1 and 2)
mask = y >= 1
X_filtered = X[mask]
y_filtered = y[mask]

# Use only Petal Length and Petal Width (features 2 and 3)
X_petal = X_filtered[:, [2, 3]]

# Convert labels to binary (class 1 -> 0, class 2 -> 1)
y_binary = (y_filtered == 2).astype(int)

# Network configuration according to specifications
# Weights from Neuron 1 (Petal Length) to hidden layer: [5, 0, 0, 0, 0]
# Weights from Neuron 2 (Petal Width) to hidden layer: [2, 0, 0, 0, 0]
w_oculta = np.array([
    [5, 0, 0, 0, 0],   
    [2, 0, 0, 0, 0]    
])

# Bias of hidden layer
b_oculta = np.array([-12, 0, 0, 0, 0])

# Weights from hidden layer to output
w_salida = np.array([10, 0, 0, 0, 0])

# Bias of output
b_salida = -5

print("Predicciones para el dataset Iris (clases 1 y 2, características Pétalo):")
print("Formato: [Largo Pétalo, Ancho Pétalo] -> Predicción (0=clase1, 1=clase2)")
print("=" * 70)

# Make predictions
class_0_correct = 0
class_1_correct = 0

print("CLASE 0 (Versicolor) - 50 muestras:")
print("-" * 50)
for i, x in enumerate(X_petal):
    z_oculta = np.dot(x, w_oculta) + b_oculta
    a_oculta = sigmoid(z_oculta)
    
    z_salida = np.dot(a_oculta, w_salida) + b_salida
    a_salida = sigmoid(z_salida)
    
    y_pred = umbral(a_salida)
    
    if y_binary[i] == 0:
        if y_pred == y_binary[i]:
            class_0_correct += 1
        print(f"[{x[0]:.1f}, {x[1]:.1f}] -> {y_pred} (real: {y_binary[i]})")
    else:
        break

print("\n" + "=" * 70)
print("CLASE 1 (Virginica) - 50 muestras:")
print("-" * 50)
for i in range(50, 100):
    x = X_petal[i]
    z_oculta = np.dot(x, w_oculta) + b_oculta
    a_oculta = sigmoid(z_oculta)
    
    z_salida = np.dot(a_oculta, w_salida) + b_salida
    a_salida = sigmoid(z_salida)
    
    y_pred = umbral(a_salida)
    
    if y_pred == y_binary[i]:
        class_1_correct += 1
    print(f"[{x[0]:.1f}, {x[1]:.1f}] -> {y_pred} (real: {y_binary[i]})")

print("\n" + "=" * 70)
print("RESUMEN:")
print(f"Clase 0 (Versicolor): {class_0_correct}/50 correctos ({class_0_correct*2}%)")
print(f"Clase 1 (Virginica): {class_1_correct}/50 correctos ({class_1_correct*2}%)")
print(f"Total: {(class_0_correct + class_1_correct)}/100 correctos ({(class_0_correct + class_1_correct)}%)")