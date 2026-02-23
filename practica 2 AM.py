import numpy as np

X = np.array([[1,15,10],
              [1,22,5],
              [1,9,9],
              [1,12,4],
              [1,18,7]
             ])

Y = np.array([[100],
             [65],
             [82],
             [60],
             [91]
            ])

theta = np.array([[0.0],
                  [0.0],
                  [0.0]
                 ])

alpha = 0.01

y_0 = np.dot(X, theta)

error = Y-y_0

gradiente = np.dot(X.T, error)

theta_1  = theta + (alpha*gradiente)

print(theta_1)

y_1 = np.dot(X, theta_1)

print(y_1)

mse= np.mean((Y - y_1)**2)

rmse = np.sqrt(mse)

s_arriba = np.sum((Y-y_1)**2)
s_abajo = np.sum((Y-np.mean(Y))**2)

r2 = 1 - (s_arriba/s_abajo)

print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"R2: {r2}")
