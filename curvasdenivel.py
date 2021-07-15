import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np 

# Definimos la función.
def f(x, y):
    return x**2 + y**2

# Creamos el rango de valores para X y Y.
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

# Calculamos las coordenadas de los puntos (X, Y).
X, Y = np.meshgrid(x, y)
Z = f(X, Y) # Llamamos la función.

fig = plt.figure()  # Se crea la figura.
fig.set_size_inches(10, 6)  # Se le indica el tamaño.
ax = plt.axes(projection="3d")  # Especifica que es 3D.
p=ax.plot_surface(X, Y, Z, cmap=cm.coolwarm);  # Generación de la superficie.
fig.colorbar(p,ax=ax) # Barra que indica el valor de los colores.

fig = plt.figure()  # Se crea la figura.
fig.set_size_inches(10, 8)  # Se le indica el tamaño.
plt.contour(X,Y,Z, levels=50, cmap="coolwarm") # Creamos el contorno de la figura.
plt.colorbar()  # Creamos la barra de colores.

fig = plt.figure()  # Se crea la figura.
fig.set_size_inches(10, 8)  # Se le indica el tamaño.
plt.contourf(X,Y,Z, levels=50, cmap="coolwarm") # Creamos el contorno de la figura.
plt.colorbar()  # Creamos la barra de colores.
plt.show()