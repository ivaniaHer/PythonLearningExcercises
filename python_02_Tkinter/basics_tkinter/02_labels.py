import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
ventana.geometry('1200x900')
ventana.configure(background='Pink')
ventana.title('Tkinter window')
# create a label
label1=ttk.Label(ventana, text='Holi')
# publish label
label1.pack(pady=30)
# Modify with configure
label1.configure(text='Modifying label with configure()')
# modify with keyvalue
label1['text'] = 'Modifying label with key value'

# mostrar
ventana.mainloop()