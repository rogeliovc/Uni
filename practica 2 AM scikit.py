import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([[1,15,10],
              [1,22,5],
              [1,9,9],
              [1,12,4],
              [1,18,7]
             ])

Y = np.array([100, 65, 82, 60, 91])

X_sk1 = X[:,1:]

modelo = LinearRegression()

modelo.fit(X_sk1, Y)

b = modelo.intercept_

theta = modelo.coef_

y_pred = modelo.predict(X_sk1)

mse = mean_squared_error(Y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(Y , y_pred)

print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"R2: {r2}")
