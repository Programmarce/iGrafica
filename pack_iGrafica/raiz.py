from tkinter import *
from tkinter import Tk, Label, Button, Entry
"""
ventana raiz
deimenciones

"""
def funcion_1():
    print("mensaje del boton")

raiz = Tk()
raiz.geometry("500x600")

label = Label(raiz,text="label_1")
label.place(relx=10,rely=10, relwidth=100,relheight=30)
label.pack()


txt = Entry(raiz, bg="pink")
txt.place(x=40,y=40, width=100,height=30)

boton = Button(raiz,text="ingresar", command=funcion_1)
boton.config(bg="orange", fg="blue")
boton.pack()

raiz.mainloop()

#def boton(raiz,msj,eventoFc)
