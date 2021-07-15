import random
from bokeh.plotting import figure, show

class Dato:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def get_coord (self,id):
        pass

    def dist_measure(self, id1, id2):
        pass

#-------------------------------------------------------------------------------------------------------

def masive_data(quantity, x_max, y_max):

    dots = []
    x_values = []
    y_values = []

    for i in range(quantity):
        x = random.randrange(x_max+1)
        y = random.randrange(y_max+1)
        dot = Dato(x, y, i)

        dots.append(dot)
        x_values.append(x)
        y_values.append(y)

    return dots, x_values, y_values

#-------------------------------------------------------------------------------------------------------
def plot(dots, x_values, y_values):

    grafica = figure(title= 'Cluster hierarchy')

    grafica.circle(x= x_values, y= y_values, size=10)
    
    show(grafica)
#-------------------------------------------------------------------------------------------------------

def main():

    try:
        x_max = int(input('Ingrese tamaño del eje x (por defecto = 10):'))
    except ValueError:
        x_max = 10
    try:
        y_max = int(input('Ingrese tamaño del eje y (por defecto = 10):'))
    except ValueError:
        y_max = 10
    try:
        quantity = int(input('Ingrese la cantidad de puntos a generar (por defecto = 10):'))
    except ValueError:
        quantity = 10

    dots, x_values, y_values = masive_data(quantity, x_max, y_max)

    plot(dots, x_values, y_values)


if __name__ == "__main__":
    main()