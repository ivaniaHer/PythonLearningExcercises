import tkinter as tk
# crear ventana
ventana = tk.Tk()
# redimensionar
ventana.geometry('1200x900')
# cambiar color de fondo
ventana.configure(background='Pink')
# cambiar titulo ventana
ventana.title('First tkinter window')
# restringir cambio de tamano de ventana
ventana.resizable(0,0)
# mostrar
ventana.mainloop()