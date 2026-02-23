import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

wine = load_wine()
X = wine.data
y = wine.target
feature_names = wine.feature_names

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

n_arboles = [10, 50, 100]

for n in n_arboles:
    bosque = RandomForestClassifier(n_estimators=n, random_state=42)
    bosque.fit(X_train, y_train)
    
    y_pred = bosque.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\nCon {n} árboles:")
    print(f"Accuracy: {acc * 100:.2f}%")
    
    importancias = bosque.feature_importances_
    indices = np.argsort(importancias)[::-1] # Ordenar de mayor a menor
    
    print("Características más importantes:")
    for i in range(3):
        print(f"{i+1}. {feature_names[indices[i]]} ({importancias[indices[i]]:.4f})")


    plt.figure(figsize=(8, 4))
    plt.bar(range(X.shape[1]), importancias)
    plt.xticks(range(X.shape[1]), feature_names, rotation=90)
    plt.title(f"Importancia con {n} árboles")
    plt.show()