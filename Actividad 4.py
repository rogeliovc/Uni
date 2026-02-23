import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Cargar el dataset
# Asegúrate de que el archivo 'housing.csv' esté en la misma carpeta
df = pd.read_csv('Housing.csv')

# 2. Selección de variables
# Características (X) y Objetivo (y)
X = df[['area', 'bedrooms', 'bathrooms', 'stories']]
y = df['price']

# 3. Dividir el conjunto de datos (80% entrenamiento, 20% prueba)
# random_state asegura que los resultados sean replicables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 4. Entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 5. Realizar predicciones sobre el conjunto de prueba
y_pred = modelo.predict(X_test)

# 6. Calcular métricas de evaluación
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# 7. Mostrar resultados para tu presentación
print("--- RESULTADOS DEL MODELO ---")
print(f"Coeficientes: {modelo.coef_}")
print(f"Intercepto:    {modelo.intercept_:.2f}")
print("-" * 30)
print(f"MSE:  {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R2:   {r2:.4f}")