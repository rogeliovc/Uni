import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

data= {
    'edad':['Joven','Joven','Joven','Adulto','Adulto','Adulto','Viejo','Viejo'],
    'ingresos':['Bajo','Bajo','Alto','Bajo','Bajo','Alto','Bajo','Alto'],
    'casado':['No','No','No','No','Si','Si','Si','Si'],
    'Acepta':['No','No','Si','Si','Si','Si','No','No']
    }

df = pd.DataFrame(data)

mapa_edad = {'Joven':0, 'Adulto':1, 'Viejo':2}
mapa_ingresos = {'Bajo':0, 'Alto':1}
mapa_casado = {'No':0, 'Si':1}

df['Edad_num'] = df['edad'].map(mapa_edad)
df['Ingresos_num'] = df['ingresos'].map(mapa_ingresos)
df['Casado_num'] = df['casado'].map(mapa_casado)

X = df[['Edad_num', 'Ingresos_num', 'Casado_num']]

y = df['Acepta']

arbol = DecisionTreeClassifier(criterion='entropy', max_depth=3)
arbol.fit(X,y)

plt.figure(figsize=(30,6))
plot_tree(arbol, feature_names=['Edad', 'Ingresos', 'Casado'], class_names=['No Acepta', 'Si Acepta'], filled=True)
plt.show()