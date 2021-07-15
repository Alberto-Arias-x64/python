import re
'''
cadena="expreciones regulares, vamo a mata rana y vamo a comer qk"
texto="vamo"

if re.search(texto,cadena) is not None:
	print("se encontro")
	"""
	smo=re.search(texto,cadena)
	print(smo.start())
	print(smo.end())
	print(smo.span())"""
else:
	print("no se encontro")

print(len(re.findall(texto,cadena)))
'''

lista=["simio ar","froger put","tocion ot","padre ar","fufin to","camion1","camión5"]

for elemento in lista:
	"""
	if re.findall('^f',elemento):
		print(elemento)
	if re.findall('r$',elemento):
		print(elemento)
	if re.findall('[o]',elemento):
		print(elemento)
	if re.findall('cami[oó]n',elemento):
		print(elemento)
	if re.findall('[a-o]$',elemento):
		print(elemento)
	if re.findall('[^a-r]$',elemento):#negacion
		print(elemento)
	"""
	if re.findall('[1-3a-c]$',elemento):
		print(elemento)

n1="simio arias"
n2="gordo toni"
n3="fufin tovar"
n1="Simio Kaka"
n5="3545345346345"

if re.match(".imio",n1,re.IGNORECASE):#IGNORA MAYUSCULA Y MINUSCULA
	print("encontrado")
else:
	print("no encontrado")

if re.match("\d",n5,):#encontrar numero al principio
	print("numero encontrado")
else:
	print("numero no encontrado")

#re.match() busca al principio
#re.search() busca en todo el texto