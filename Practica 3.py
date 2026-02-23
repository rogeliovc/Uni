import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [1,2]
    ])

y= np.array([0])

w = np.array([0.6,1.2])

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