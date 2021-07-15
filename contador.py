import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


n = 100000

comienzo = time.time()
factorial(n)
final = time.time()
print(f"exaustivo {final - comienzo}")

comienzo = time.time()
factorial_r(n)
final = time.time()
print(f"recursivo {final - comienzo}")