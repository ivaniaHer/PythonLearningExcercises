import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
ventana.geometry('1200x900')
ventana.configure(background='Pink')
ventana.title('Tkinter window')

def saludo(name):
    print(f'Hola {name}')

button1=ttk.Button(ventana, text='Enviar', command= lambda: saludo('Nico'))
button1.pack(pady=40)

ventana.mainloop()