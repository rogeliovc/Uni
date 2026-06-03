import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url= "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columnas = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv(url, names=columnas)

X = iris[['sepal_length', 'sepal_width']].values

def distancia_euclidiana(p1, p2):
    suma_cuadrados = 0
    for i in range(len(p1)):
        suma_cuadrados += (p1[i] - p2[i]) ** 2
    return np.sqrt(suma_cuadrados)

k=3
np.random.seed()
indices_aleatorios = np.random.choice(X.shape[0], k, replace=False)
centroides = X[indices_aleatorios]

colores = ['blue', 'green', 'red']

num_iteraciones = 5

for iteracion in range(num_iteraciones):
    asignaciones = []

    for punto in X:
        distancias = []
        for centroide in centroides:
            distancias.append(distancia_euclidiana(punto, centroide))

        clusiter_asignado = distancias.index(min(distancias))
        asignaciones.append(clusiter_asignado)

    asignaciones = np.array(asignaciones)

    plt.figure(figsize=(8, 6))
    for i in range(k):
        puntos_cluster = np.array([X[j] for j in range(len(X)) if asignaciones[j] == i])

        if len(puntos_cluster) > 0:
            plt.scatter(puntos_cluster[:, 0], puntos_cluster[:, 1], 
                        color=colores[i], label=f'Cluster {i+1}')
    plt.scatter(centroides[:, 0], centroides[:, 1], 
                color='black', marker='X', s=200, label='Centroides')
    plt.title(f'Iteración {iteracion + 1}')
    plt.xlabel('Largo del Sépalo')
    plt.ylabel('Ancho del Sépalo')
    plt.legend()
    plt.show()

    nuevos_centroides = []
    for i in range(k): 
        puntos_cluster = [X[j] for j in range(len(X)) if asignaciones[j] == i]
        if len(puntos_cluster) > 0:
            nuevo_x = sum(punto[0] for punto in puntos_cluster) / len(puntos_cluster)
            nuevo_y = sum(punto[1] for punto in puntos_cluster) / len(puntos_cluster)
            nuevos_centroides.append([nuevo_x, nuevo_y])
        else:
            nuevos_centroides.append(centroides[i])

    centroides = np.array(nuevos_centroides)