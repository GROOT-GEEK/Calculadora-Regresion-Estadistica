import tkinter as tk
from Class_interpolacion import VentanaInterpolacion
from Class_integral import VentanaIntegrales
from Class_regresion import Regresion
from Class_Ecua import Ecuaciones
from tkinter.messagebox import *

icono = "Src/Icono.ico"

color_fondo = "#FEF5ED"


class interfaz():
    def __init__(self):
         # Configuracion pestaña
        self.v_principal = tk.Tk()
        self.v_principal.iconbitmap(icono)
        self.v_principal.configure(background=color_fondo)
        self.v_principal.resizable(width=0, height=0)
        self.v_principal.title('Calculadora Regresión Estadistica')
        self.v_principal.columnconfigure(0, weight=1)
        self.v_principal.columnconfigure(1, weight=1)
        self.v_principal.rowconfigure(0, weight=1)
        self.v_principal.rowconfigure(1, weight=2)
        self.v_principal.rowconfigure(2, weight=2)

        # GenerarImagenes
        self.img_titulo = tk.PhotoImage(file="Src/Titiulo_principal.png")
        self.img_regresion = tk.PhotoImage(file="Src/regresion.png")

        # Elementos pestaña
        self.titulo = tk.Button (self.v_principal, image=self.img_titulo, border=0, command=self.creador)
        self.botton3 = tk.Button(self.v_principal, image=self.img_regresion, command=self.regresion, border=0)

        # impresion de elementos
        self.titulo.grid(row=0, column=0, columnspan=2)
        self.botton3.grid(row=1, column=0,columnspan=2)


        self. v_principal.mainloop()

    def regresion(self):
        Regresion()

    def creador(self):
        showinfo(message="Jessica Bilbao - Github BilbaoJ \nSantiago Gomez - Github: SantiagoGM19 \nAlejandro Durango - Github: GROOT-GEEK ",
                title="Creadores")

def main():
    interfaz()
    return 0

if __name__ == '__main__':
    main()
