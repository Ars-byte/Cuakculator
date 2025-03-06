import customtkinter as ct
from tkinter import *

def calcular():
    try:
        resultado = eval(entrada.get())
        label_resultado.configure(text=str(resultado))
    except:
        label_resultado.configure(text="Error")

ventana = ct.CTk()
ventana.geometry("640x369")
ventana.title("Cuakculator :) ")

bienvenida = ct.CTkLabel(ventana, text="Cuakculator :DD ")
bienvenida.pack(pady=20)

entrada = ct.CTkEntry(ventana, width=200)
entrada.pack(pady=20)

boton_calcular = ct.CTkButton(ventana, text="=", command=calcular)
boton_calcular.pack(pady=20)

label_resultado = ct.CTkLabel(ventana, text="")
label_resultado.pack(pady=20)

ventana.mainloop()


