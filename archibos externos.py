from io import open
'''
archivo=open("archivo.txt","w")
frase="muere puto"
archivo.write(frase)
archivo.close()

archivo=open("archivo.txt","r")
texto=archivo.read()
archivo.close()
print(texto)

archivo=open("archivo.txt","r")
texto=archivo.readlines()
archivo.close()
print(texto)

archivo=open("archivo.txt","a")
texto=archivo.write("\n hoy aprendimos a jugar en python")
archivo.close()
'''

archivo=open("archivo.txt","r+") #lectura y escritura
print(archivo.read())
archivo.seek(11)
print(archivo.read(12))
archivo.close()
