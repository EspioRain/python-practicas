import tkinter as tk

vetana = tk.Tk()
vetana.config(width=300, height=300)
vetana.title("Calculadora")

cuno = tk.Entry()
cuno.place(x=20, y=50)
cdos = tk.Entry()
cdos.place(x=160, y=50)


vetana.mainloop()