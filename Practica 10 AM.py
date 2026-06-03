import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

data_frutas = {
    'Peso': [150, 160, 170, 145, 155, 180, 190, 185, 200, 195, 100, 105, 110, 95, 115],
    'Diametro': [7.1, 7.3, 7.5, 7.0, 7.2, 8.1, 8.3, 8.0, 8.5, 8.2, 5.1, 5.3, 5.5, 5.0, 5.4],
    'Acidez': [4.5, 4.4, 4.6, 4.5, 4.3, 3.8, 3.7, 3.9, 3.6, 3.8, 2.2, 2.3, 2.1, 2.4, 2.2],
    'Fruta': ['Manzana', 'Manzana', 'Manzana', 'Manzana', 'Manzana', 
              'Naranja', 'Naranja', 'Naranja', 'Naranja', 'Naranja', 
              'Limón', 'Limón', 'Limón', 'Limón', 'Limón']
}

df = pd.DataFrame(data_frutas)

X = df[['Peso', 'Diametro', 'Acidez']]
y_texto = df['Fruta']

le = LabelEncoder()
y = le.fit_transform(y_texto)

modelo = GaussianNB()

modelo.fit(X, y)


nueva_fruta = pd.DataFrame([{
    'Peso': 175, 
    'Diametro': 7.8, 
    'Acidez': 4.0
}])

prediccion_numerica = modelo.predict(nueva_fruta)
probabilidades = modelo.predict_proba(nueva_fruta)

prediccion_texto = le.inverse_transform(prediccion_numerica)

print(f"Caracteristicas de fruta a clasificar: \n {nueva_fruta}")

print(f"\n¿Qué fruta es probable? \nR: {prediccion_texto[0]}")
print(f"\nTodas las opciones: {le.classes_}")
print(f"Probabilidades: {probabilidades[0]}")