import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.naive_bayes import MultinomialNB

data = {
    'Edad': ['Joven', 'Joven', 'Adulto', 'Anciano', 'Anciano', 'Anciano', 'Adulto', 'Joven', 'Joven', 'Anciano', 'Joven', 'Adulto', 'Adulto', 'Anciano'],
    'Ingresos': ['Altos', 'Altos', 'Altos', 'Medios', 'Bajos', 'Bajos', 'Bajos', 'Medios', 'Bajos', 'Medios', 'Medios', 'Medios', 'Altos', 'Medios'],
    'Estudiante': ['No', 'No', 'No', 'No', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No'],
    'Credito': ['Regular', 'Excelente', 'Regular', 'Regular', 'Regular', 'Excelente', 'Excelente', 'Regular', 'Regular', 'Regular', 'Excelente', 'Excelente', 'Regular', 'Excelente'],
    'Compra': ['No', 'No', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No']
}

df = pd.DataFrame(data)
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_encoded = encoder.fit_transform(df[['Edad', 'Ingresos', 'Estudiante', 'Credito']])
y = df['Compra']

modelo = MultinomialNB()
modelo.fit(X_encoded, y)

nuevo_cliente = pd.DataFrame([{
    'Edad': 'Anciano',
    'Ingresos': 'Bajos',
    'Estudiante': 'No',
    'Credito': 'Excelente'
}])

nuevo_cliente_encoded = encoder.transform(nuevo_cliente)
prediccion = modelo.predict(nuevo_cliente_encoded)
probabilidades = modelo.predict_proba(nuevo_cliente_encoded)

print(f"--- Resultado para el nuevo cliente ---")
print(f"¿Comprará la computadora?: {prediccion[0]}")
print(f"Probabilidades [No, Sí]: {probabilidades[0]}")