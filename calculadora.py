from tkinter import *
from io import *
from tkinter import messagebox
from tkinter import filedialog

global num1,resultado,operacion,num2,punto
resultado=0
operacion=0
punto=0

def cd(numero):
	global operacion,punto
	n=str(numero)
	if(pantalla.get()=="0" or operacion=="="):
		num.set("")
		operacion=0
	if(numero=="." and pantalla.get()==""):num.set("0")
	if(numero=="."):
		if(punto==0):
			num.set(pantalla.get()+n)
		punto=1
	else:num.set(pantalla.get()+n)

def cm(op):
	try:
		global num1,resultado,operacion,punto

		num1=num.get()

		if(op=="+"):
			if(resultado!="0"):num.set("")
			resultado=float(num1)+resultado
			num.set("")
		elif(op=="-"):
			if(resultado!="0"):num.set("")
			if(resultado==0):resultado=float(num1)
			else:resultado=resultado-float(num1)
			num.set("")
		elif(op=="*"):
			if(resultado!="0"):num.set("")
			if(resultado==0):resultado=float(num1)
			else:resultado=resultado*float(num1)
			num.set("")
		elif(op=="/"):
			if(resultado!="0"):num.set("")
			if(resultado==0):resultado=float(num1)
			else:resultado=resultado/float(num1)
			num.set("")
		elif(op=="="):
			try:
				if(operacion!="="):cm(operacion)
				guardar(resultado,op)
			except:num.set(str(resultado))
			num.set(str(resultado))
			resultado=0
			punto=0
		operacion=op

	except:
		num.set(".I. ERROR .I.        ")

def color(var):
	if(var==1):pantalla.config(fg="#0614E7")
	elif(var==2):pantalla.config(fg="#E70606")
	else:pantalla.config(fg="#468009")

def guardar(res,op):
	if(ck.get()==True and op=="="):
		archivo=open("res.txt","a")
		texto=archivo.write(str(res))
		texto=archivo.write("\n")
		archivo.close()

def pantalla2(parametro):
	if(parametro==1):
		messagebox.showinfo("Cerrar","aun no c hacerlo XD")
		raiz.destroy()
	elif(parametro==2):
		while(True):
			messagebox.showwarning("Ja Ja XD","Se va a trabar el PC")
	elif(parametro==3):
		respuesta=messagebox.askquestion("deseo","quiere limpiar la memoria")

def guardado():
	fichero=filedialog.askopenfilename(title="Puto", initialdir="C:", filetypes=(("Block de notas",".txt"),("Todos los archivos",".")))
	#return(fichero)

raiz=Tk()
barra=Menu(raiz)
raiz.title("calculadora del simio")
#raiz.iconbitmap("Moto.ico")
raiz.config(menu=barra)

archivo=Menu(barra,tearoff=0)
archivo.add_command(label="Guardado",command=guardado)
archivo.add_command(label="Cerrar",command=lambda:pantalla2(1))

herrameintas=Menu(barra,tearoff=0)
herrameintas.add_command(label="Limpiar",command=lambda:pantalla2(3))
herrameintas.add_separator()
herrameintas.add_command(label="Trabar PC",command=lambda:pantalla2(2))

barra.add_cascade(label="Archivo", menu=archivo)
barra.add_cascade(label="Herrameintas", menu=herrameintas)

fr=Frame(raiz)
fr.pack()

num=StringVar()
bar=IntVar()
ck=IntVar()

pantalla=Entry(fr,bg="black",justify="right",width=(20),textvariable=num)
pantalla.grid(row=0,column=0,padx="10",pady="10",columnspan=4)
pantalla.config(state="readonly")

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
boton0=Button(fr,text="0",command=lambda:cd(0),width=(3))
boton0.grid(row=4,column=3,padx="2",pady="2")
botond=Button(fr,text="/",command=lambda:cm("/"),width=(3))
botond.grid(row=1,column=0,padx="2",pady="2")
botonm=Button(fr,text="*",command=lambda:cm("*"),width=(3))
botonm.grid(row=1,column=1,padx="2",pady="2")
botonr=Button(fr,text="-",command=lambda:cm("-"),width=(3))
botonr.grid(row=1,column=2,padx="2",pady="2")
botons=Button(fr,text="+",command=lambda:cm("+"),width=(3))
botons.grid(row=1,column=3,padx="2",pady="2")
botons=Button(fr,text="=",command=lambda:cm("="),width=(3))
botons.grid(row=3,column=3,padx="2",pady="2")
botons=Button(fr,text=".",command=lambda:cd("."),width=(3))
botons.grid(row=2,column=3,padx="2",pady="2")

Radiobutton(fr,text="Azul",variable=bar, value=1,command=lambda:color(bar.get())).grid(row=5,column=0,padx="2",pady="2",columnspan=2)
Radiobutton(fr,text="Rojo",variable=bar, value=2,command=lambda:color(bar.get())).grid(row=5,column=2,padx="2",pady="2",columnspan=2)
color(bar.get())

Checkbutton(fr,text="Guardar",variable=ck,onvalue=True,offvalue=False).grid(row=1,column=5,padx="2",pady="2")

raiz.mainloop()