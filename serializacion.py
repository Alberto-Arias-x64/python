import pickle 

'''
lista=["hola","puto","el","que","lo","lea"]
fichero=open("lista_nombres","wb")
pickle.dump(lista,fichero)
fichero.close()
del(fichero) 
'''
fichero=open("lista_nombres","rb")
lista=pickle.load(fichero)
print(lista)
