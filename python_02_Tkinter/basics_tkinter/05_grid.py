import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
ventana.geometry('1200x900')
ventana.configure(background='Pink')
ventana.title('Tkinter window')

button1 = ttk.Button(ventana, text='Button 1')
button2 = ttk.Button(ventana, text='Button 2')
button3 = ttk.Button(ventana, text='Button 3')

button1.grid(row=0, column=0, ipadx=30, ipady=30, pady=20, padx=20)# sticky = mover con coordenadas de grid
button2.grid(row=0, column=1, sticky=tk.SE, ipady=10, ipadx=10, pady=20)
button3.grid(row=0, column=2, sticky=tk.SE)

#configuracion de pesos de columnas
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)

#configuracion de pesos de filas
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=2)
ventana.rowconfigure(2, weight=1)

# mostrar
ventana.mainloop()