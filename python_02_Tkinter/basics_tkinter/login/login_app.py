import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

def validar(event):
    user = txt_box_user.get()
    password = txt_box_pass.get()
    if user == 'root' and password == 'admin':
        showinfo(title='Login', message='Successfull login')
    else:
        showerror(title='Error', message='Invalid data')

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(background='#C26D9B')
ventana.title('Login')

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

frame1=ttk.Frame(ventana)
frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1,weight=3)

label1=ttk.Label(frame1,text='Login', font=('Century Gothic', 20))
label1.grid(row=0, column=0, columnspan=2)

label_user = ttk.Label(frame1, text='User:')
label_user.grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)
txt_box_user = ttk.Entry(frame1)
txt_box_user.grid(row=1, column=1, sticky=tk.E, pady=5, padx=5)

label_pass = ttk.Label(frame1, text='Password:')
label_pass.grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)
txt_box_pass = ttk.Entry(frame1, show='*')
txt_box_pass.grid(row=2, column=1, sticky=tk.E, pady=5, padx=5)

login_btn = ttk.Button(frame1, text='Access')
login_btn.grid(row=3, columnspan=2, pady=10)

#eventos
login_btn.bind('<Return>', validar)
login_btn.bind('<Button-1>', validar)

styles = ttk.Style(ventana)
styles.theme_use('clam')
styles.configure(ventana, background='#C26D9B', foreground='white',
                 fieldbackground='#933E6B')
styles.configure('TButton', background='#53233C')
styles.map('TButton', background=[('active','#DCACC6')])

frame1.grid(row=0, column=0)
ventana.mainloop()