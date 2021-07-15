def fd(fp):
	def fi(*args): #resibe parametros indeterminados
		print("vamos a realizar un calculo")
		fp(*args)
		print("hemos terminado el calculo")
	return fi

@fd
def suma(n1,n2):
	print(n1+n2)

def resta(n1,n2):
	print(n1-n2)

suma(3,2)
resta(3,2)