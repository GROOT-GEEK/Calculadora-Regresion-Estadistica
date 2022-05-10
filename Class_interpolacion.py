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

class VentanaInterpolacion():
    def __init__(self):
        self.raizInterpolacion = Toplevel()
        self.raizInterpolacion.geometry(tamano_default)
        self.raizInterpolacion.resizable(width=0, height=0)
        self.raizInterpolacion.iconbitmap(icono)
        self.raizInterpolacion.title('Interpolacion')
        self.raizInterpolacion.configure(bg=color_fondo)
        self.canvas = tk.Canvas(self.raizInterpolacion)
        self.textoResultado = 'Resultado'
        self.img_title=tk.PhotoImage(file="Src/TInterpolacion.png")
        self.lblTipo = tk.Button(self.raizInterpolacion,image=self.img_title, border=0,command=self.creador)
        self.lblTipo.pack(side=TOP)

        # FS --> FontStyle
        self.FStitulos = TkFont.Font(family='Segoe Print', size=18)
        self.FStexto = TkFont.Font(family='Segoe Print', size=12)

#FRAME 1
        self.Fdatos = tk.Frame(self.raizInterpolacion, bg='#FEF5ED')
        self.Fdatos.pack(expand=True, fill='both')

        self.lblTipo = ttk.Label(self.Fdatos, text='METODO INTERPOLACIÓN NEWTON', font=self.FStitulos)
        self.lblTipo.configure(background='#FEF5ED')
        self.lblTipo.pack(side=TOP)

        self.lblDatosX = ttk.Label(self.Fdatos, text='Valores de X separados por comas: ', font=self.FStexto)
        self.lblDatosX.configure(background='#FEF5ED')
        self.lblDatosX.place(x=70, y=70)

        self.inputX = ttk.Entry(self.Fdatos, background='white')
        self.inputX.configure(width=40)
        self.inputX.place(x=450, y=75)

        self.lblDatosY = ttk.Label(
        self.Fdatos, text='Valores de Y separados por comas: ', font=self.FStexto)
        self.lblDatosY.configure(background='#FEF5ED')
        self.lblDatosY.place(x=70, y=140)

        self.inputY = ttk.Entry(self.Fdatos, background='white')
        self.inputY.configure(width=40)
        self.inputY.place(x=450, y=145)

        self.lblGrado = ttk.Label(
        self.Fdatos, text='Grado que quiere para el polinomio \ninterpolador: ', font=self.FStexto)
        self.lblGrado.configure(background='#FEF5ED')
        self.lblGrado.place(x=70, y=210)

        self.inputGrado = ttk.Entry(self.Fdatos, background='white')
        self.inputGrado.configure(width=40)
        self.inputGrado.place(x=450, y=220)

        self.lblValor = ttk.Label(
        self.Fdatos, text='Valor que desea interpolar: ', font=self.FStexto)
        self.lblValor.configure(background='#FEF5ED')
        self.lblValor.place(x=70, y=280)

        self.inputValor = ttk.Entry(self.Fdatos, background='white')
        self.inputValor.configure(width=40)
        self.inputValor.place(x=450, y=285)

        self.imgbtn = tk.PhotoImage(file="Src/btn.png")
        self.btnCalcular= tk.Button(self.Fdatos, image=self.imgbtn,command=self.calcular)
        self.btnCalcular.place(x=200, y=360)

        self.lblResultado = ttk.Label(
        self.Fdatos, text=self.textoResultado, font=self.FStexto)
        self.lblResultado.configure(background='#D3E4CD', width=30)
        self.lblResultado.place(x=350, y=365)

# METODOS
    def calcular(self):
        valoresx = self.inputX.get().split(',')
        valores_x = list(map(float, valoresx))

        valoresy = self.inputY.get().split(',')
        valores_y = list(map(float, valoresy))

        grado = int(self.inputGrado.get())

        valor = float(self.inputValor.get())

        resultado = self.interpolacionNewton(valor, grado, valores_x, valores_y)

        self.lblResultado.config(text = str(resultado))

    def interpolacionNewton(self, valor, grado, valores_x, f_x):
        '''
        recibe:
        -valor: valor a interpolar
        -grado: grado del polinomio interpolador
        -valores_x: conjunto de datos del dominio
        -f_x: conjunto de datos del rango
        retorna:
        -polinomio: el valor interpolado
        '''
        polinomio = f_x[0]
        cont = 1
        matrizDiferencias = self.diferenciaDividida(f_x, valores_x, grado, 1, [], 1)
        for i in range(grado):
            productos = 1
            for j in range(cont):
                productos *= (valor - valores_x[j])
            polinomio += matrizDiferencias[cont-1][0]*productos
            cont += 1
        return polinomio


    def diferenciaDividida(self, f_x, valores_x, grado, columna, matriz, paso):
        '''
        recibe:
            -f_x: conjunto de datos del rango
            -valores_x: conjunto de datos del dominio
            -grado: grado del polinomio interpolador
            -columna: contador de columnas
            -matriz: matriz de diferencias divididas
            -paso: saltos que se hacen entre las x para las diferencias divididas
        retorna matrizTotal: matriz con todas las diferencias divididas resueltas 
        '''
        if(len(matriz) == 0):
            matriz.append(valores_x)
            matriz.append(f_x)
        diferencias = []
        for i in range(len(matriz[columna])):
            if(len(matriz[columna])-i == 1):
                break
            f2 = matriz[columna][i+1]
            f1 = matriz[columna][i]
            x2 = matriz[0][i+paso]
            x1 = matriz[0][i]
            diferencia = self.dividirDiferencias(f2, f1, x2, x1)
            diferencias.append(diferencia)
        matriz.append(diferencias)
        if(len(matriz)-2 == grado):
            matrizTotal = matriz[2:]
            return matrizTotal
        else:
            return self.diferenciaDividida(f_x, valores_x, grado, columna+1, matriz, paso+1)


    def dividirDiferencias(self, f2, f1, x2, x1):
        return ((f2-f1)/(x2-x1))

    def creador(self):
       showinfo(message="Santiago Gomez - Github: SantiagoGM19 \nAlejandro Durango - Github: AlejandroDurango ", title="Creadores")

