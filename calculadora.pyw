from tkinter import *

global num1
global num2

def cd(numero):
	n=str(numero)
	num.set(pantalla.get()+n)

def cm(op):
	if(op=="="):
		num2=pantalla.get()
		n1=int(num1)
		n2=int(num2)
		x=str(n1+n2)
		num.set(x)
	elif(op=="+"):
		num1=pantalla.get()

raiz=Tk()
raiz.title("calculadora de simio")
raiz.iconbitmap("Moto.ico")

fr=Frame(raiz)
fr.pack()

num=StringVar()
num1=StringVar()
num2=StringVar()

pantalla=Entry(fr,bg="black",fg="#01DF01",justify="right",width=(20),textvariable=num)
pantalla.grid(row=0,column=0,padx="10",pady="10",columnspan=4)

boton1=Button(fr,text="1",command=lambda:cd(1),width=(3))
boton1.grid(row=4,column=0,padx="2",pady="2")
boton2=Button(fr,text="2",command=lambda:cd(2),width=(3))
boton2.grid(row=4,column=1,padx="2",pady="2")
boton3=Button(fr,text="3",command=lambda:cd(3),width=(3))
boton3.grid(row=4,column=2,padx="2",pady="2")
boton4=Button(fr,text="4",command=lambda:cd(4),width=(3))
boton4.grid(row=3,column=0,padx="2",pady="2")
boton5=Button(fr,text="5",command=lambda:cd(5),width=(3))
boton5.grid(row=3,column=1,padx="2",pady="2")
boton6=Button(fr,text="6",command=lambda:cd(6),width=(3))
boton6.grid(row=3,column=2,padx="2",pady="2")
boton7=Button(fr,text="7",command=lambda:cd(7),width=(3))
boton7.grid(row=2,column=0,padx="2",pady="2")
boton8=Button(fr,text="8",command=lambda:cd(8),width=(3))
boton8.grid(row=2,column=1,padx="2",pady="2")
boton9=Button(fr,text="9",command=lambda:cd(9),width=(3))
boton9.grid(row=2,column=2,padx="2",pady="2")
boton0=Button(fr,text="0",command=lambda:cd(0),width=(3),height=(3))
boton0.grid(row=3,column=3,padx="2",pady="2",rowspan=2)
botond=Button(fr,text="/",command=cm("/"),width=(3))
botond.grid(row=1,column=0,padx="2",pady="2")
botonm=Button(fr,text="*",command=cm("*"),width=(3))
botonm.grid(row=1,column=1,padx="2",pady="2")
botonr=Button(fr,text="-",command=cm("-"),width=(3))
botonr.grid(row=1,column=2,padx="2",pady="2")
botons=Button(fr,text="+",command=lambda:cm("+"),width=(3))
botons.grid(row=1,column=3,padx="2",pady="2")
botons=Button(fr,text="=",command=lambda:cm("="),width=(3))
botons.grid(row=2,column=3,padx="2",pady="2")

raiz.mainloop()
