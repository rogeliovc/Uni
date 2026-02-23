import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

X = np.array([
    [3,2,1,3,0,4.19]
    ])

y= np.array([1])


modelo =  LogisticRegression()

w = np.array([2.5, -5.0, -1.2, 0.5, 2.0, 0.7])

b= np.array([0.1])

modelo.coef_ = w.reshape(1, -1)
modelo.intercept_ = b
modelo.classes_ = np.array([0, 1])

z = modelo.decision_function(X)
probabilidad_t = modelo.predict_proba(X)
probabilidad = probabilidad_t[:, 1]

w_a = modelo.coef_[0]
b_a = modelo.intercept_[0]

plt.figure(figsize=(10, 5))
z_limites= np.linspace(z.min()-10, z.max()+10, 100)
sigmoide= 1 / (1 + np.exp(-z_limites))

plt.plot(z_limites, sigmoide, color = 'black')
plt.scatter(z, probabilidad, s=100)
plt.grid(True)
plt.show()