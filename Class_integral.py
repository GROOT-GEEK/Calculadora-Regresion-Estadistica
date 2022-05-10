from tkinter import *
import tkinter as tk
import tkinter.font as TkFont
from tkinter import ttk
from sympy import *
import numpy as np
import math
from tkinter.messagebox import *


icono = "Src/Icono.ico"
tamano_default = '800x600'
color_fondo ="#FEF5ED"

class VentanaIntegrales:
    def __init__(self):
        self.raizIntegrales = Toplevel()
        self.raizIntegrales.geometry(tamano_default)
        self.raizIntegrales.resizable(width=0, height=0)
        self.raizIntegrales.title('Calculadora Integración Numerica')
        self.raizIntegrales.configure(bg=color_fondo)

        self.img_title=tk.PhotoImage(file="Src/tintegracion.png")
        self.titulo= tk.Button(self.raizIntegrales,image=self.img_title, border=0,command=self.creador)
        self.titulo.pack(side=TOP)

        self.Fdatos = tk.Frame(self.raizIntegrales, bg='#FEF5ED')
        self.Fdatos2 = tk.Frame(self.raizIntegrales, bg='#FEF5ED')

        def visualizarframe1 ():
            self.Fdatos2.pack_forget()
            self.Fdatos.pack(expand=True, fill='both')


        def visualizarframe2 ():
            self.Fdatos.pack_forget()
            self.Fdatos2.pack(expand=True, fill='both')

        self.img_title2=tk.PhotoImage(file="Src/OpIntegra1.png")
        self.titulo2= tk.Button(self.raizIntegrales,image=self.img_title2, border=0,command=visualizarframe1)
        self.titulo2.pack(side=TOP)

        self.img_title3=tk.PhotoImage(file="Src/OpIntegra2.png")
        self.titulo3= tk.Button(self.raizIntegrales,image=self.img_title3, border=0,command=visualizarframe2)
        self.titulo3.pack(side=TOP)



        self.x = Symbol('x')
        self.fun = vars(math)

        # FS --> FontStyle
        self.FStitulos = TkFont.Font(family='Segoe Print', size=18)
        self.FStexto = TkFont.Font(family='Segoe Print', size=12)

#FRAME 1
        self.lblTipo = ttk.Label(
            self.Fdatos, text='INTEGRALES CON FUNCIÓN MATEMÁTICA', font=self.FStitulos)
        self.lblTipo.configure(background='#FEF5ED')
        self.lblTipo.pack(side=TOP)

        self.lblValorInicial = ttk.Label(
            self.Fdatos, text='Valor inicial del intervalo: ', font=self.FStexto)
        self.lblValorInicial.configure(background='#FEF5ED')
        self.lblValorInicial.place(x=70, y=70)

        self.inputValorInicial = ttk.Entry(self.Fdatos, background='white')
        self.inputValorInicial.configure(width=40)
        self.inputValorInicial.place(x=450, y=75)

        self.lblDatosValorFinal = ttk.Label(
            self.Fdatos, text='Valor final del intervalo: ', font=self.FStexto)
        self.lblDatosValorFinal.configure(background='#FEF5ED')
        self.lblDatosValorFinal.place(x=70, y=140)

        self.inputValorFinal = ttk.Entry(self.Fdatos, background='white')
        self.inputValorFinal.configure(width=40)
        self.inputValorFinal.place(x=450, y=145)

        self.lblFuncion = ttk.Label(
            self.Fdatos, text='Función a integrar: ', font=self.FStexto)
        self.lblFuncion.configure(background='#FEF5ED')
        self.lblFuncion.place(x=70, y=210)

        self.inputFuncion = ttk.Entry(self.Fdatos, background='white')
        self.inputFuncion.configure(width=40)
        self.inputFuncion.place(x=450, y=220)

        self.lblParticiones = ttk.Label(
            self.Fdatos, text='Número de particiones (solo pares): ', font=self.FStexto)
        self.lblParticiones.configure(background='#FEF5ED')
        self.lblParticiones.place(x=70, y=280)

        self.inputParticiones = ttk.Entry(self.Fdatos, background='white')
        self.inputParticiones.configure(width=40)
        self.inputParticiones.place(x=450, y=285)

        self.imgbtn = tk.PhotoImage(file="Src/btn.png")
        self.btnCalcular= tk.Button(self.Fdatos, image=self.imgbtn,command=self.calcular)
        self.btnCalcular.place(x=200, y=360)

        self.lblResultado = ttk.Label(self.Fdatos, text='Resultado', font=self.FStexto)
        self.lblResultado.configure(background='#D3E4CD', width=30)
        self.lblResultado.place(x=350, y=365)

#FRAME 2
        self.lblTipo1 = ttk.Label(
            self.Fdatos2, text='INTEGRALES PARA UNA TABLA DE VALORES', font=self.FStitulos)
        self.lblTipo1.configure(background='#FEF5ED')
        self.lblTipo1.pack(side=TOP)

        self.lblDatosX1 = ttk.Label(
            self.Fdatos2, text='Valores de X separados por comas: ', font=self.FStexto)
        self.lblDatosX1.configure(background='#FEF5ED')
        self.lblDatosX1.place(x=70, y=70)

        self.inputDatosX1 = ttk.Entry(self.Fdatos2, background='white')
        self.inputDatosX1.configure(width=40)
        self.inputDatosX1.place(x=450, y=75)

        self.lblDatosY1 = ttk.Label(
            self.Fdatos2, text='Valores de Y separados por comas: ', font=self.FStexto)
        self.lblDatosY1.configure(background='#FEF5ED')
        self.lblDatosY1.place(x=70, y=140)

        self.inputDatosY1 = ttk.Entry(self.Fdatos2, background='white')
        self.inputDatosY1.configure(width=40)
        self.inputDatosY1.place(x=450, y=145)

        self.imgbtn2 = tk.PhotoImage(file="Src/btn.png")
        self.btnCalcular2= tk.Button(self.Fdatos2, image=self.imgbtn2,command=self.calcular1)
        self.btnCalcular2.place(x=200, y=360)

        self.lblResultado1 = ttk.Label(self.Fdatos2, text='Resultado', font=self.FStexto)
        self.lblResultado1.configure(background='#D3E4CD', width=30)
        self.lblResultado1.place(x=350, y=365)

#METODOS FUNCIÓN
    def calcular(self):
        valorIncial = float(self.inputValorInicial.get())
        valorFinal = float(self.inputValorFinal.get())
        funcion = self.inputFuncion.get()
        numeroParticiones = int(self.inputParticiones.get())
        resultado = self.simpson_1_3_multiple(valorIncial, valorFinal, funcion, numeroParticiones)
        self.lblResultado.config(text = str(resultado))

    def simpson_1_3_multiple(self,x0,xn,f,n):
        h = (xn-x0)/n
        x = np.linspace(x0,xn,n+1)
        termImpar = 0
        termPar = 0

        for i in range(1, len(x)-1):
            if(i%2 == 0):
                termPar += eval(f, self.fun, {'x': x[i]})
            else:
                termImpar += eval(f, self.fun, {'x': x[i]})

        I = (h/3)*(eval(f, self.fun, {'x': x0}) + 4*termImpar + 2*termPar + eval(f, self.fun, {'x': xn}))
        return I

#METODOS TABLA
    def calcular1(self):
        valoresx = self.inputDatosX1.get().split(',')
        valores_x = list(map(float, valoresx))

        valoresy = self.inputDatosY1.get().split(',')
        valores_y = list(map(float, valoresy))
        resultado = self.integrarTabla1(valores_y, valores_x)
        self.lblResultado1.config(text = str(resultado))

    def integrarTabla1(self, f, x):
        n = len(x)
        if(len(x) % 2 == 0):
            I1 = self.simpson_1_3_multiple1(f[0:n-3], x[0:n-3])
            print(I1)
            I2 = self.simpson_3_81(f[n-4:n], x[n-4:n])
            I = I1 + I2
        else:
            I = self.simpson_1_3_multiple1(f,x)
        return I

    def simpson_1_3_multiple1(self,f,x):
        termImpar = 0
        termPar = 0
        h = x[1] - x[0]
        for i in range(1, len(x)-1):
            if(i%2 == 0):
                termPar += f[i]
            else:
                termImpar += f[i]

        I = (h/3)*(f[0] + 4*termImpar + 2*termPar + f[-1])
        return I

    def simpson_3_81(self,f,x):
        h = x[1] - x[0]
        I = ((3*h)/8)*(f[0] + 3*f[1] + 3*f[2] + f[3])
        return I

    def creador(self):
        showinfo(message="Santiago Gomez - Github: SantiagoGM19 \nAlejandro Durango - Github: AlejandroDurango ", title="Creadores")
