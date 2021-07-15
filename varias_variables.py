#Librerías necesarias: Matplotlib y Numpy
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np 

#linspace retorna valores entre los intervalos que se indican
u=np.linspace(-5,5,100)
v=np.linspace(-6,6,100)

#Funciona similar que en Matlab
[x,y]=np.meshgrid(u,v)

#Esta es la ecuación
z=np.cos(x)*np.cos(y)*np.exp(-np.sqrt(x**2+y**2)/20)

#Se crea la figura
fig = plt.figure()

#Se le indica el tamaño
fig.set_size_inches(10, 6)

#Especifica que es 3D
ax = plt.axes(projection="3d")

#Generación de la superficie
p=ax.plot_surface(x, y, z, cmap='inferno')

#Barra que indica el valor de los colores
fig.colorbar(p,ax=ax)

plt.show()