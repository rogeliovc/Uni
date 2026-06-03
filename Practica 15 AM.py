import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

# Cargar el dataset de Iris
iris = load_iris()

# Seleccionar únicamente las dos últimas clases (clases 1 y 2)
# Y usar únicamente el Ancho del Sépalo (índice 1) y Ancho del Pétalo (índice 3)
X = iris.data[50:, [1, 3]]  # Filas 50-149 (clases 1 y 2), columnas 1 y 3
y = iris.target[50:] - 1    # Convertir a clases 0 y 1

# Función para entrenar el perceptrón
def entrenar_perceptron(epocas, X, y):
    # Iniciar los pesos de manera aleatoria
    w1 = np.random.randn()
    w2 = np.random.randn()
    b = np.random.randn()
    
    tasa_aprendizaje = 0.1
    error_por_epoca = []
    
    for epoca in range(epocas):
        errores_en_epoca = 0
        
        for i in range(len(X)):
            x1 = X[i][0]  # Ancho del sépalo
            x2 = X[i][1]  # Ancho del pétalo
            salida_esperada = y[i]
            
            suma_ponderada = (w1*x1)+(w2*x2)+b
            
            if suma_ponderada > 0:
                prediccion = 1
            else:
                prediccion = 0
            
            error = salida_esperada - prediccion
            
            if error != 0:
                w1 += tasa_aprendizaje * error * x1
                w2 += tasa_aprendizaje * error * x2
                b += tasa_aprendizaje * error
                errores_en_epoca += 1
        
        error_por_epoca.append(errores_en_epoca)
    
    return w1, w2, b, error_por_epoca

# Hacer 5 corridas con diferentes iteraciones
iteraciones = [20, 50, 100, 1000, 10000]
resultados = []

for epochs in iteraciones:
    w1, w2, b, errores = entrenar_perceptron(epochs, X, y)
    resultados.append({
        'epocas': epochs,
        'w1': w1, 'w2': w2, 'b': b,
        'errores': errores,
        'error_final': errores[-1] if errores else 0
    })
    print(f"Corrida con {epochs} épocas - Error final: {errores[-1] if errores else 0}")
    
# Crear plots para cada corrida
fig, axes = plt.subplots(2, 5, figsize=(20, 8))

for i, resultado in enumerate(resultados):
    # Plot 1: Línea de clasificación
    ax1 = axes[0, i]
    
    # Graficar puntos de datos
    ax1.scatter(X[y==0][:,0], X[y==0][:,1], color='red', label='Versicolor', alpha=0.7)
    ax1.scatter(X[y==1][:,0], X[y==1][:,1], color='blue', label='Virginica', alpha=0.7)
    
    # Calcular línea de decisión: w1*x1 + w2*x2 + b = 0
    # x2 = -(w1*x1 + b) / w2
    x_min = X[:, 0].min() - 0.5
    x_max = X[:, 0].max() + 0.5
    y_min = -(resultado['w1'] * x_min + resultado['b']) / resultado['w2']
    y_max = -(resultado['w1'] * x_max + resultado['b']) / resultado['w2']
    
    ax1.plot([x_min, x_max], [y_min, y_max], 'k-', lw=2, label='Frontera de decisión')
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(X[:, 1].min() - 0.5, X[:, 1].max() + 0.5)
    ax1.set_xlabel('Ancho del Sépalo')
    ax1.set_ylabel('Ancho del Pétalo')
    ax1.set_title(f'Clasificación - {resultado["epocas"]} épocas')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Épocas vs error acumulado
    ax2 = axes[1, i]
    epocas_range = range(1, len(resultado['errores']) + 1)
    ax2.plot(epocas_range, resultado['errores'], marker='o', linestyle='-', color='b', markersize=3)
    ax2.set_xlabel('Época')
    ax2.set_ylabel('Errores en la época')
    ax2.set_title(f'Error vs Épocas - {resultado["epocas"]} épocas')
    ax2.grid(True, alpha=0.3)
    
    # Si hay muchas épocas, mostrar solo cada n-ésima época para mejor visualización
    if resultado['epocas'] > 100:
        step = max(1, len(epocas_range) // 20)
        ax2.set_xticks(epocas_range[::step])
        ax2.set_xticklabels([str(x) for x in epocas_range[::step]], rotation=45)

plt.tight_layout()
plt.show()

# Resumen final de errores
print("\n" + "="*60)
print("RESUMEN DE ERRORES EN LA ÚLTIMA ÉPOCA")
print("="*60)
for resultado in resultados:
    print(f"Épocas: {resultado['epocas']:5d} | Error final: {resultado['error_final']:3d}")
print("="*60)