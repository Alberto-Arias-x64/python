import numpy as np
import random
from bokeh.plotting import Figure, output_file, show
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.datasets import make_blobs

rl = LogisticRegression()
fig = Figure()

def problema1():
    horas = ([0.5, 0.75, 1, 1.25, 1.5, 1.75, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 4, 4.25, 4.5, 4.75, 5, 5.5])
    aprobacion = ([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

    horas = np.array(horas).reshape(-1,1)
    aprobacion = np.array(aprobacion)

    rl.fit(horas,aprobacion)
    horas_nuevas = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

    prediccion = rl.predict(horas_nuevas)
    print(prediccion)

    pp = rl.predict_proba(horas_nuevas)
    print(pp)

def suport_vector():
    colores = []
    x,y = make_blobs(n_samples=100, centers=2, random_state=6)
    clf = svm.SVC(kernel="linear", C=1000)
    clf.fit(x,y)
    for color in range(len(y)):
        if y[color] == 0: 
            colores.append("blue")
        else:
            colores.append("red")
    fig.dot(x[:,0],x[:,1],size=20, color=colores)
    show(fig)

def algoritmo_genetico():

    def individual(min,max):
        return[random.randint(min,max) for i in range(largo)]

    def crear_poblacion():
        return[individual(1,9) for i in range(num) ]

    def calcuar_fitness(individual):
        fitness = 0
        for i in range(len(individual)):
            if individual[i] == modelo[i]:
                fitness += 1
        return fitness

    def seleccion_reproduccion(population):
        puntuados = [(calcuar_fitness(i),i) for i in population]
        puntuados = [i[1] for i in sorted(puntuados)]
        population = puntuados
        selected = puntuados[(len(puntuados)-pressure)]
        for i in range(len(population)-pressure):
            punto = random.randint(1, largo-1)
            padre = random.sample(selected, 2)

            #print(padre)
            population[i][:punto] = padre[:punto]
            population[i][punto:] = padre[punto:]

        return population

    def mutacion(population):
        for i in range(len(population)-pressure):
            if random.random() <= mutation_change:
                punto = random.randint(0,largo-1)
                nuevo_valor = random.randint(1,9)

                while nuevo_valor == population[i][punto]:
                    nuevo_valor = random.randint(1,9)
                population[i][punto] = nuevo_valor
        return population

    modelo = [1,1,1,1,1,1,1,1,1,1]
    largo = 10
    num = 10
    pressure = 3
    mutation_change = 0.2
    population = crear_poblacion()
    print(f"poblacion inicial{population}")
    for _ in range(100):
        population = seleccion_reproduccion(population)
        population = mutacion(population)
    print (f"poblacion final {population}")


algoritmo_genetico()