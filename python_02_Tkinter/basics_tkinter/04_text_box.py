import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('1200x900')
ventana.configure(background='Pink')
ventana.title('Tkinter window')


def mostrar():
    texto = txtbox_input.get()
    label2.configure(text=texto)

#etiqueta
label1 = ttk.Label(ventana, text='Escribe algo: ')
label1.pack(pady=60)

#Input
txtbox_input = ttk.Entry(ventana, font=('Courier Sans', 12))
txtbox_input.pack(pady=10) 

#Boton
button1 = ttk.Button(ventana, text='Enviar', command=mostrar)
button1.pack(pady=20)

label2 = ttk.Label(ventana, text='')
label2.pack(pady=20)
ventana.mainloop()
