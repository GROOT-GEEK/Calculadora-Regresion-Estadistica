from tkinter import *
import tkinter as tk
import tkinter.font as TkFont
from tkinter import ttk
from sympy import *
import numpy as np
import math
from tkinter.messagebox import *
import matplotlib.pyplot as plt

icono = "Src/Icono.ico"
tamano_default = '890x600'
color_fondo ="#FEF5ED"


class Regresion:
    def __init__(self):
        self.vregresion = Toplevel()
        self.vregresion.geometry(tamano_default)
        self.vregresion.resizable(width=0, height=0)
        self.vregresion.iconbitmap(icono)
        self.vregresion.title('Regresión Lineal')
        self.vregresion.configure(bg=color_fondo)

        self.img_title=tk.PhotoImage(file="Src/Tregresion.png")
        self.titulo= tk.Button(self.vregresion,image=self.img_title, border=0,command=self.creador)
        self.titulo.pack(side=TOP)

        self.Fdatos = tk.Frame(self.vregresion, bg=color_fondo)
            


        self.x = Symbol('x')
        self.fun = vars(math)

        # FS --> FontStyle
        self.FStitulos = TkFont.Font(family='Segoe Print', size=18)
        self.FStexto = TkFont.Font(family='Segoe Print', size=12)

#FRAME 1
        self.Fdatos = tk.Frame(self.vregresion, background=color_fondo)
        self.lblDatosX = ttk.Label(self.Fdatos, text='Valores de X separados por comas: ', font=self.FStexto)
        self.lblDatosX.configure(background=color_fondo)
        self.lblDatosX.place(x=70, y=70)

        self.inputDatosX = ttk.Entry(self.Fdatos, background='white')
        self.inputDatosX.configure(width=40)
        self.inputDatosX.place(x=450, y=75)

        self.lblDatosY = ttk.Label(self.Fdatos, text='Valores de Y separados por comas: ', font=self.FStexto)
        self.lblDatosY.configure(background=color_fondo)
        self.lblDatosY.place(x=70, y=140)

        self.inputDatosY = ttk.Entry(self.Fdatos, background='white')
        self.inputDatosY.configure(width=40)
        self.inputDatosY.place(x=450, y=145)

        self.imgbtn = tk.PhotoImage(file="Src/btn.png")
        self.btnCalcular= tk.Button(self.Fdatos, image=self.imgbtn,command=self.calcular)
        self.btnCalcular.place(x=100, y=255)

        self.lblLineaRegresion = ttk.Label(self.Fdatos, text='Linea de regresión', font=self.FStexto)
        self.lblLineaRegresion.configure(background='#D3E4CD', width=45)
        self.lblLineaRegresion.place(x=250, y=225)

        self.lblCoeficienteDeterminacion = ttk.Label(self.Fdatos, text='Coeficiente de determinación', font=self.FStexto)
        self.lblCoeficienteDeterminacion.configure(background='#D3E4CD', width=45)
        self.lblCoeficienteDeterminacion.place(x=250, y=265)

        self.lblCoeficienteCorrelacion = ttk.Label(self.Fdatos, text='Coeficiente de correlación', font=self.FStexto)
        self.lblCoeficienteCorrelacion.configure(background='#D3E4CD', width=45)
        self.lblCoeficienteCorrelacion.place(x=250, y=305)
        
        self.Fdatos.pack(expand=True, fill='both')
        
#METODOS OPCIÓN 1
    def calcular(self):
        valoresx = self.inputDatosX.get().split(',')
        valoresx2 = list(map(float, valoresx))
        valores_x = np.array(valoresx2)

        valoresy = self.inputDatosY.get().split(',')
        valoresy2 = list(map(float, valoresy))
        valores_y = np.array(valoresy2)

        linea, coeficienteDeterminacion, coeficienteCorrelacion = self.regresion_lineal(
            valores_x, valores_y)

        self.lblLineaRegresion.config(text=linea)
        self.lblCoeficienteDeterminacion.config(text=coeficienteDeterminacion)
        self.lblCoeficienteCorrelacion.config(text=coeficienteCorrelacion)
        
        self.grafica = Toplevel()
        self.grafica.geometry("800x500")
        self.grafica.title("Grafica")
        self.grafica.resizable(width=0, height=0)
        plt.style.use('seaborn-whitegrid')
        plt.scatter(valores_x,valores_y,marker='o')
        plt.savefig("grafico.png")
        self.img_fra=tk.PhotoImage(file="grafico.png")
        plt.clf()
        self.graficaI= tk.Button(self.grafica,image=self.img_fra, border=0)
        self.graficaI.pack(side=TOP)

    def regresion_lineal(self, x, y):
        """
        x e y: arreglos de numpy
        """
        n = x.shape[0]
        sumaxy = 0
        sumax = 0
        sumay = 0
        sumax2 = 0
        for i in range(n):
            sumaxy += x[i]*y[i]
            sumax += x[i]
            sumay += y[i]
            sumax2 += x[i]**2

        mediay = sumay/n
        mediax = sumax/n

        a1 = ((n*sumaxy) - (sumax*sumay))/((n*sumax2) - (sumax**2))

        a0 = mediay - a1*mediax

        #print("Intercepto con y: ", a0)
        #print("Pendiente: ", a1)

        yest = a0 + a1*x

        # Medidas de bondad y ajuste
        St = sum((b-mediay)**2 for b in y)
        Sr = sum((yt - ye)**2 for yt, ye in zip(y, yest))

        R2 = (St - Sr)/St
        R = np.sqrt(abs(R2))

        coeDeterminacion = R2
        coeCorrelacion = R
        linea = "y = " + "(" + str(a0) + ")" + " + " + "(" + str(a1) + ")" + "*x"

        return linea, coeDeterminacion, coeCorrelacion

    def creador(self):
            showinfo(message="Jessica Bilbao - Github BilbaoJ \nSantiago Gomez - Github: SantiagoGM19 \nAlejandro Durango - Github: GROOT-GEEK ",
                title="Creadores")