import tkinter as tk
from time import strftime

ventana = tk.Tk()
ventana.title("Reloj Digital")
ventana.geometry("250x100")

def reloj():
    etiqueta_reloj = strftime("%H:%M:%S %p") #Formato am | pm
    etiqueta.config(text = etiqueta_reloj)
    etiqueta.after(1000, reloj)

etiqueta = tk.Label(ventana, font=("Arial", 20), background='#f5f2f1', foreground="black")
etiqueta.pack(anchor="center", pady=30)

reloj()

ventana.mainloop()