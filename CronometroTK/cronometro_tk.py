import tkinter as tk


class Cronometro:
    def __init__(self, ventana):
        self.ventana = ventana
        self.hora = 0
        self.minuto = 0
        self.segunto = 0
        self.milisegundo = 0
        self.corriendo = False
        self.vista = tk.StringVar()
        self.actualizar_vista = ('00:00:00:000')

        #Configuracion de la ventana
        self.ventana.title("Cronometro")
        self.ventana.configure(bg = '#f5f2f1')
        self.ventana.geometry("350x200") #utilizar siempre la x en las medidas de ventanas
        self.vista_etiqueta = tk.Label(ventana, textvariable=self.vista, font=("Arial", 36), bg='#f5f2f1', fg='black' ) #La tipografia es una tupla de tipo y tamano

        self.vista_etiqueta.pack() #Para mostrar la etiqueta en la ventana

        #Frame de los botones y botones (Iniciar | Detener | Reiniciar)
        self.botones_frame = tk.Frame(ventana, bg='#f5f2f1')
        self.botones_frame.pack()

        self.boton_inicar = tk.Button(self.botones_frame, text='Iniciar', command=self.iniciar_cronometro, bg='#2ecc71', fg='black')
        self.boton_inicar.pack(side=tk.LEFT, padx=5, pady=10) #Mostramos el boton a la izquierda

        self.boton_detener = tk.Button(self.botones_frame, text='Detener', command=self.detener_cronometro, bg='#3498db', fg='black')
        self.boton_detener.pack(side=tk.LEFT, padx=5, pady=10) #Mostramos el boton al centro
        
        self.boton_reiniciar = tk.Button(self.botones_frame, text='Reiniciar', command=self.reiniciar_cronometro, bg='#e74c3c', fg='black')
        self.boton_reiniciar.pack(side=tk.LEFT, padx=5, pady=10) #Mostramos el boton a la derecha

        #FIN DEL CONSTRUCTOR
  
    def actualizar_cronometro(self):
        if self.corriendo:
            self.milisegundo += 10
            if self.milisegundo == 1000:
                self.milisegundo = 0
                self.segunto += 1
            if self.segunto == 60:
                self.segunto = 0
                self.minuto += 1
            if self.minuto == 60:
                self.minuto = 0
                self.hora += 1

            tiempo = f"{self.hora:02}:{self.minuto:02}:{self.segunto:02}:{self.milisegundo:03}"
            self.vista.set(tiempo)
            self.ventana.after(10, self.actualizar_cronometro)

    def iniciar_cronometro(self):
        if not self.corriendo:
            self.corriendo = True
            self.actualizar_cronometro()

    def detener_cronometro(self):
        self.corriendo = False

    def reiniciar_cronometro(self):
        self.hora = 0
        self.minuto = 0
        self.segunto = 0
        self.milisegundo = 0      
        self.vista.set('00:00:00:000')


if __name__=='__main__':
    ventana = tk.Tk()
    cronometro = Cronometro(ventana)
    ventana.mainloop()