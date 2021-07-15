from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5)
#keyboard.press('a')
#keyboard.release('a')

#keyboard.press(Key.cmd)
#keyboard.release(Key.cmd)

#Keyboard.type("escribe esto para mi por favor")
'''
for x in "mi pito es el mas grande":
    keyboard.press(x)
    keyboard.release(x)
    time.sleep(0.12)
'''

u=0
d=0
c=0
for rep in range (0,101):
    def caracter(a1,a2,a3):
        A=str(a1)
        B=str(a2)
        C=str(a3)
        lista=(A,B,C)
        return (lista)

    numero=caracter(c,d,u)

    for x in numero:
        keyboard.press(x)
        keyboard.release(x)
        time.sleep(0.12)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    u=u+1
    if u==10:
        u=0
        d=d+1
    if d==10:
        d=0
        c=c+1
