import numpy as np
from statistics import mode,median
from collections import Counter

def main():
    temps = np.array([3,35,30,37,27,31,41,20,16,26,45,37,9,41,28,
                    21,31,35,10,26,11,34,36,12,22,17,33,43,19,
                    48,38,25,36,32,38,28,30,36,39,40])
    valores = np.unique(temps)
    print(Counter(temps))
    print('valores :',valores)
    print('Media: ',round(temps.mean(),2))
    print('Moda: ',mode(temps))
    print('Mediana: ',median(temps))
    print('Varianza: ',round(temps.var(),2))
    print('ubicacion del valor superior: posicion {} , numero {}'.format(temps.argmax(),temps[temps.argmax()])) 
    print('ubicacion del valor inferior: posicion {} , el numero es {}'.format(temps.argmin(),temps[temps.argmin()]))

main()