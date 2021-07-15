class Carro():
	def desplazamiento(self):
		print("me desplazo con 4 ruedas")

class Moto():
	def desplazamiento(self):
		print("me desplazo con 2 ruedas")

class Camion():
	def desplazamiento(self):
		print("me desplazo con 6 ruedas")

def carrito(v):
	v.desplazamiento()

'''
carrito(input("hola puto: "))
input()
'''