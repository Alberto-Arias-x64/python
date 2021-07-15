from tkinter import *

def codigoboton():
	minombre.set("simio")

raiz=Tk()
raiz.title("ventana de simio")
raiz.geometry("800x600")
raiz.resizable(0,0)
raiz.iconbitmap("Moto.ico")

minombre=StringVar()

myframe=Frame(raiz)
myframe.pack()
myframe.config(width=(800),height=(600),cursor="hand2")

Label(myframe, text="simio XDXD").grid(row=0,column=0,padx="30",pady="30")
try:
	th=PhotoImage(file="smo.jpg",width=(50),height=(50))
	Label(myframe, image=th).grid(row=0,column=1)
except:
	th=PhotoImage(file="thanos.gif",width=(50),height=(50))
	Label(myframe, image=th).grid(row=0,column=1)

Label(myframe, text="comentarios").grid(row=3,column=0)

cuadro=Entry(myframe,textvariable=minombre)
cuadro.grid(row=1,column=0)#sticky("n","s","w","e")

comen=Text(myframe,width=16,height=5)
comen.grid(row=3,column=1,padx=10,pady=10)


scrolly=Scrollbar(myframe,command=comen.yview)
scrolly.grid(row=3,column=2,sticky="nsw")
comen.config(yscrollcommand=scrolly.set)

boton1=Button(myframe,text="no le des",command=codigoboton)
boton1.grid(row=4,column=1)

raiz.mainloop()
