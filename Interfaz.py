import tkinter as tk
from Class_interpolacion import VentanaInterpolacion
from Class_integral import VentanaIntegrales
from Class_regresion import Regresion
from Class_Ecua import Ecuaciones
from tkinter.messagebox import *

icono = "Src/Icono.ico"
tamano_default = '500x500'
color_fondo = "#FEF5ED"


class interfaz():
    def __init__(self):
         # Configuracion pestaña
        self.v_principal = tk.Tk()
        self.v_principal.iconbitmap(icono)
        self.v_principal.configure(background=color_fondo)
        self.v_principal.geometry(tamano_default)
        self.v_principal.resizable(width=0, height=0)
        self.v_principal.title('Calculadora Analisis numerico')
        self.v_principal.columnconfigure(0, weight=1)
        self.v_principal.columnconfigure(1, weight=1)
        self.v_principal.rowconfigure(0, weight=1)
        self.v_principal.rowconfigure(1, weight=2)
        self.v_principal.rowconfigure(2, weight=2)

        # GenerarImagenes
        self.img_titulo = tk.PhotoImage(file="Src/Titiulo_principal.png")
        self.img_interpolacion = tk.PhotoImage(file="Src/Interpolacion.png")
        self.img_integracion = tk.PhotoImage(file="Src/integracion.png")
        self.img_regresion = tk.PhotoImage(file="Src/regresion.png")
        self.img_diferencial = tk.PhotoImage(file="Src/diferencial.png")

        # Elementos pestaña
        self.titulo = tk.Button (self.v_principal, image=self.img_titulo, border=0, command=self.creador)
        self.botton1 = tk.Button(self.v_principal, image=self.img_interpolacion, command=self.interpolacion, border=0)
        self.botton2 = tk.Button(self.v_principal, image=self.img_integracion, command=self.inte_definidas, border=0)
        self.botton3 = tk.Button(self.v_principal, image=self.img_regresion, command=self.regresion, border=0)
        self.botton4 = tk.Button(self.v_principal, image=self.img_diferencial, command=self.ecu_dife_ordi, border=0)

        # impresion de elementos
        self.titulo.grid(row=0, column=0, columnspan=2)
        self.botton2.grid(row=1, column=1)
        self.botton3.grid(row=2, column=0)
        self.botton1.grid(row=1, column=0)
        self.botton4.grid(row=2, column=1)

        self. v_principal.mainloop()

    def interpolacion(self):
        VentanaInterpolacion()

    def inte_definidas(self):
        VentanaIntegrales()

    def regresion(self):
        Regresion()

    def ecu_dife_ordi(self):
        Ecuaciones()

    def creador(self):
        showinfo(message="Santiago Gomez - Github: SantiagoGM19 \nAlejandro Durango - Github: AlejandroDurango ",
                title="Creadores")

def main():
    interfaz()
    return 0

if __name__ == '__main__':
    main()
