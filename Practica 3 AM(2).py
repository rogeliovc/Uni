import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    1.7, -2.2, 0.6, 2.9,
    -1.4, 1.1, 0.2, 1.4,
    -0.4, 2.2, 0.8, -0.6, 
    0.95, -1.7, 3.9
    ])

Y = np.array([1,0,1,1,0,0,0,1,0,1,1,0,0,0,1])

w = np.array([0.6, 1.2])

b= -8.0

z = np.dot(X, w) + b

probabilidad = 1 / (1 + np.exp(-z))
predicion = (probabilidad >= 0.5).astype(int)

print(f"Probabilidad = {probabilidad}")   

plt.figure(figsize=(10, 5))
z_limites= np.linspace(z.min()-10, z.max()+10, 100)
sigmoide= 1 / (1 + np.exp(-z_limites))

plt.plot(z_limites, sigmoide, color = 'black')
plt.scatter(z, probabilidad, s=100)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))

for i in range(len(Y)):
    
    color = 'green' if Y[i] == 1 else 'red'
    plt.scatter(X[i, 0], X[i, 1], color=color, s=100)     
 
print(f"Probabilidad = {probabilidad}")   
x1 = np.linspace(0, 10, 100)
x2 = -(0.61*x1 + b) / 1.2

plt.plot(x1, x2)
plt.grid(True)

