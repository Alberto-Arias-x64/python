import sqlite3

Coneccion=sqlite3.connect("Labase2")

cursor1=Coneccion.cursor()

'''
cursor1.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")
cursor1.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

variosproductos=[("camiseta",10,"Deportes"),("jarron",10,"ceramica"),("camion",10,"jugeteria")]
cursor1.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosproductos)

cursor1.execute("SELECT * FROM PRODUCTOS")
bar=cursor1.fetchall()

print(bar)

Coneccion.commit()
'''

try:
	cursor1.execute('''
		CREATE TABLE PRODUCTOS (
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
		PRECIO INTEGER, 
		SECCION VARCHAR(20))
	''')
except:
	n=0

variosproductos=[
	("camiseta",10,"Deportes"),
	("jarron",10,"Ceramica"),
	("camion",10,"Jugeteria"),
	("camion2",12,"Jugeteria"),
	("camion3",15,"Jugeteria")
]

cursor1.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", variosproductos)
Coneccion.commit()

cursor1.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Jugeteria'")
bar=cursor1.fetchall()
Coneccion.commit()
print(bar)

cursor1.execute("UPDATE PRODUCTOS SET PRECIO=250 WHERE NOMBRE_ARTICULO='camion3'")
Coneccion.commit()

cursor1.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO='camion2'")
Coneccion.commit()

cursor1.execute("SELECT * FROM PRODUCTOS")
bar=cursor1.fetchall()
Coneccion.commit()
print(bar)


Coneccion.close()