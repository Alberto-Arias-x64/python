'''
def numeru():
	print("si puedes leer esto es que sabes leer, ahora introduce un numero")
	bandera=False
	num=input()
	for x in range(0,999):
		y=str(x)
		if(num==y):
		    print("Muy bien no eres tan pendejo")
		    bandera=True
		    break
	else:
		print("Que pendejo >:v")
numeru()
'''
class Vehiculo():
	def __init__(self,marca,modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelerando=False
		self.frenando=False

	def enmarcha(self):
		self.enmarcha=True
	def acelerando(self):
		self.acelerando=True
	def frenando(self):
		self.frenando=True
	def estado(self):
		print("marca = ",self.marca,"\nmodelo = ",self.modelo,"\nen marcha = ",
			self.enmarcha,"\nacelerando = ",self.acelerando,"\nfrenando = ",self.frenando)

class Moto(Vehiculo):#hereda en vehiculos

	def __init__(self,marca,modelo):
		super().__init__(marca,modelo)
		self.hcaballo=False

	def caballo(self):
		self.hcaballo=True
	def estado(self): #sobre escrtitura de metodos
		print("marca = ",self.marca,"\nmodelo = ",self.modelo,"\nen marcha = ",
			self.enmarcha,"\nacelerando = ",self.acelerando,"\nfrenando = ",self.frenando,"\nhaciendo welle= ",self.hcaballo)
'''
class Cuatrimoto(Vehiculo,Moto):#herencia multiple
	pass
'''

mimoto=Moto("mazda","miata")
#mimoto.caballo()
mimoto.estado()
input()

'''
class Carro():
	#propiedades
	def __init__(self):#constructor

		self.largochasis=260
		self.anchichasis=120
		self.__ruedas=4   #encapsulacion"proteger datos"
		self.enmarcha=False
	#metodos
	def arrancar(self, valor):
		self.enmarcha=valor
		if(self.enmarcha):
			chek=self.__chequeo_interno()
		if(self.enmarcha==True and chek): 
			return"el carro esta en marcha"
		elif(self.enmarcha==True and chek==False): 
			return"el carro esta en marcha pero falla algo"
		else:
			return"el carro esta parado"

	def estado(self):
		print("largo del chasis = ", self.largochasis)
		print("ancho del chasis = ", self.anchichasis)
		print("cantidad de ruedas = ", self.__ruedas)

	def __chequeo_interno(self):
		print("chequeo interno")
		self.gasolina=True
		self.aceite=True
		self.puertas=False

		if(self.gasolina and self.aceite and self.puertas):
			return(True)
		else:
			return(False)
		

micarro=Carro()

print(micarro.arrancar(True))
micarro.estado()


miata=Carro()
print(miata.arrancar(False))
miata.estado()
input()

def intro(numero):
	valor=type(numero) is int
	if(valor==True):
		print("muy bien no eres tan pendejo")
	else:
		print("que pendejo >:v")
intro(int(num))
'''
