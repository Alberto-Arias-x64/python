from borracho import borracho_tradicional
from campo import Campo
from coordenadas import Coordenada
from bokeh.plotting import*

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_medias_por_caminata = []
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media=round(sum(distancias)/ len(distancias), 4)
        distancia_maxima=max(distancias)
        distancia_minima=min(distancias)
        distancias_medias_por_caminata.append(distancia_media)

        print(f"{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos")
        print(f"media = {distancia_media}")
        print(f"max = {distancia_maxima}")
        print(f"min = {distancia_minima}")
    graficar(distancias_de_caminata, distancias_medias_por_caminata)

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre="simio")
    origen = Coordenada(0,0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo=Campo()
        campo.añadir_borracho(borracho,origen)
        sumulacion_caminata = caminata(campo,borracho,pasos)
        distancias.append(round(sumulacion_caminata, 1))
    return distancias

def caminata(campo,borracho,pasos):
    inicio = campo.obtener_coordenada(borracho)
    for _ in range(pasos):
        campo.mover_borracho(borracho)
    return inicio.distancia(campo.obtener_coordenada(borracho))

def graficar(x,y):
    grafica=Figure(title="camino borrachos")
    grafica.line(x,y, legend="distancia media")
    show(grafica)


distancias_de_caminata=[10,100,1000]
numero_de_intentos=100
main(distancias_de_caminata,numero_de_intentos,borracho_tradicional)

