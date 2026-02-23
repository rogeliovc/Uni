import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc, roc_auc_score, accuracy_score, precision_score, recall_score, f1_score

# Cargar dataset
wine = datasets.load_wine()
X, y = wine.data, wine.target
class_names = wine.target_names

# División 80/20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo con número de iteraciones específico
max_iter = 15  # Cambiar este valor manualmente: 1, 15, 50, 100

print(f"\n=== Modelo con {max_iter} iteraciones ===")
modelo = LogisticRegression(max_iter=max_iter, random_state=42)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)

# Calcular métricas
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Calcular especificidad para cada clase
cm = confusion_matrix(y_test, y_pred)
especificidades = []
for i in range(len(class_names)):
    tn = cm.sum() - (cm[i, :].sum() + cm[:, i].sum() - cm[i, i])
    fp = cm[:, i].sum() - cm[i, i]
    especificidad = tn / (tn + fp) if (tn + fp) > 0 else 0
    especificidades.append(especificidad)
especificidad_promedio = np.mean(especificidades)

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
print(f"Especificidad promedio: {especificidad_promedio:.4f}")

print(f"\n=== Visualizaciones usando modelo con {max_iter} iteraciones ===")
ConfusionMatrixDisplay(cm, display_labels=class_names).plot(cmap='viridis')
plt.show()

print(classification_report(y_test, y_pred, target_names=class_names))

y_test_bin = label_binarize(y_test, classes=[0, 1, 2])
n_classes = y_test_bin.shape[1]

y_score = modelo.decision_function(X_test)

plt.figure(figsize=(10, 6))
colors = ['blue', 'red', 'green']

for i, color in zip(range(n_classes), colors):
    fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_score[:, i])
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, color=color, lw=2, label=f'ROC{class_names[i]}')

plt.xlabel('FP')
plt.ylabel('TP')
plt.legend(loc='lower right')
plt.title('Curva ROC-AUC')
plt.show()

# Resumen final y respuesta a la pregunta
print("\n" + "="*60)
print("ANÁLISIS FINAL: ¿Se logró una regresión 'perfecta'?")
print("="*60)

mejor_accuracy = 0
mejor_modelo_info = None
for iter_num, metrics in resultados.items():
    if metrics['accuracy'] > mejor_accuracy:
        mejor_accuracy = metrics['accuracy']
        mejor_modelo_info = (iter_num, metrics)

print(f"\nMejor modelo: {mejor_modelo_info[0]} iteraciones")
print(f"Accuracy: {mejor_modelo_info[1]['accuracy']:.4f}")
print(f"Precision: {mejor_modelo_info[1]['precision']:.4f}")
print(f"Recall: {mejor_modelo_info[1]['recall']:.4f}")
print(f"F1-Score: {mejor_modelo_info[1]['f1']:.4f}")
print(f"Especificidad: {mejor_modelo_info[1]['especificidad']:.4f}")