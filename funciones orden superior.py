class Empleado:
	def __init__(self,nombre,cargo,salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {}".format(self.nombre,self.cargo,self.salario)

Lista=[
Empleado("simio","king",25000),
Empleado("froger","esclabo",10),
Empleado("father","utraking",50000),
Empleado("muther","tocino",40000)
]

"""
inpresindibles=filter(lambda empleado:empleado.salario>11,Lista)

for emp in inpresindibles:
	print(emp)"""

def calculo_cpmision(empleado):
	if(empleado.salario <= 10):
		empleado.salario=empleado.salario*1000
	return empleado

listacomision=map(calculo_cpmision,Lista)

for emp in listacomision:
	print(emp)
