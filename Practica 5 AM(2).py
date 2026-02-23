from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. Cargar datos
wine = load_wine()
X, y = wine.data, wine.target

# 2. División 80/20 (Requisito: Usar 80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 3. Probar profundidades (Requisito: 3, 5, 10)
profundidades = [3, 5, 10]

for d in profundidades:
    # Entrenar
    arbol = DecisionTreeClassifier(criterion='entropy', max_depth=d, random_state=42)
    arbol.fit(X_train, y_train)
    
    # Evaluar
    predicciones = arbol.predict(X_test)
    precision = accuracy_score(y_test, predicciones)
    
    # Mostrar Árbol (Requisito: Mostrar los árboles)
    plt.figure(figsize=(20, 8))
    plot_tree(arbol, feature_names=wine.feature_names, class_names=wine.target_names, filled=True)
    plt.title(f"Árbol de Decisión - Profundidad: {d} | Precisión: {precision:.2f}")
    plt.show()
    
    print(f"Profundidad {d} -> Precisión en Test: {precision * 100:.2f}%")
    