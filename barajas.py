import random
import collections

PALOS = ["espada","corazon","rombo","trebol"]#en mayuscula valores inmutables
VALORES = ["as","2","3","4","5","6","7","8","9","10","jota","queen","king"]

def crear_baraja ():
    baraja = []
    for palo in PALOS:
        for valor in VALORES:
            baraja.append((palo, valor))
    return baraja

def obtener_mano(baraja, tamaño_mano):
    mano = random.sample(baraja,tamaño_mano)
    return mano

def main(tamaño_mano,intentos):
    baraja = crear_baraja()
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(baraja,tamaño_mano)
        manos.append(mano)
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1
                break
    probabilidad_par = pares/intentos
    print(f"probabilidad de encontrar un par es {probabilidad_par}")


tamaño_mano = int(input("Tamaño de mano: "))
intentos = int(input("intentos: "))
main(tamaño_mano,intentos)