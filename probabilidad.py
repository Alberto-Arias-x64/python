import random

def main(numero_de_tiros,numero_de_intentos):
    tiros=[]
    for _ in range(numero_de_intentos):
        secuencia_de_tiros_1=tirar_dado(numero_de_tiros)
        secuencia_de_tiros_2=tirar_dado(numero_de_tiros)
        for x in range(numero_de_tiros):
            tiros.append(secuencia_de_tiros_1[x]+secuencia_de_tiros_2[x])
            
    tiros_con_1=0
    for tiro in tiros:
        if 12 == tiro:
            tiros_con_1 += 1
    probabilidad_tiros_con_1=tiros_con_1/numero_de_intentos
    print(f"tener 12 {probabilidad_tiros_con_1}")

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros=[]
    for _ in range(numero_de_tiros):
        tiro=random.choice([1,2,3,4,5,6])
        secuencia_de_tiros.append(tiro)
    return secuencia_de_tiros

numero_de_tiros=int(input("Cuantos tiros del dado : "))
numero_de_intentos=int(input("Cuantas veces correra la simulacion : "))
main(numero_de_tiros, numero_de_intentos)