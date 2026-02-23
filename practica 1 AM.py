from calendar import c
import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([2,2.5,3.2,4,4.5,5.1,5.8,6.5,7,8.2,9,9.5,10.2,11,12])
y = np.array([420,510,650,810,890,1030,1150,1300,1390,1650,1780,1910,2050,2200,2380])

n = len(x)

m = (n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x**2)-(np.sum(x))**2)

b= (np.sum(y)-m*np.sum(x))/(n)

print(f"Modelo encontrado: y = {m}x + {b}")

prediccion5 = m*15 + b
print(f"Prediccion = {prediccion5}")

plt.scatter(x,y, color="blue")
plt.plot(x, m*x+b, color="red")
plt.show()

# hola
