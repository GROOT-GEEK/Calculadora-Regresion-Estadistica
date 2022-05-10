from tkinter import *
import tkinter as tk
import tkinter.font as TkFont
from tkinter import ttk
from sympy import *
import numpy as np
import math
from tkinter.messagebox import *

icono = "Src/Icono.ico"
tamano_default = '890x600'
color_fondo ="#FEF5ED"


class Regresion:
    def __init__(self):
        self.vregresion = Toplevel()
        self.vregresion.geometry(tamano_default)
        self.vregresion.resizable(width=0, height=0)
        self.vregresion.iconbitmap(icono)
        self.vregresion.title('Calculadora Regresión')
        self.vregresion.configure(bg=color_fondo)

        self.img_title=tk.PhotoImage(file="Src/Tregresion.png")
        self.titulo= tk.Button(self.vregresion,image=self.img_title, border=0,command=self.creador)
        self.titulo.pack(side=TOP)

        self.Fdatos = tk.Frame(self.vregresion, bg=color_fondo)
        self.Fdatos2 = tk.Frame(self.vregresion, bg=color_fondo)
        self.Fdatos3 = tk.Frame(self.vregresion, bg=color_fondo)

        def visualizarframe1 ():
            self.Fdatos2.pack_forget()
            self.Fdatos3.pack_forget()
            self.Fdatos.pack(expand=True, fill='both')

        def visualizarframe2 ():
            self.Fdatos.pack_forget()
            self.Fdatos3.pack_forget()
            self.Fdatos2.pack(expand=True, fill='both')

        def visualizarframe3():
            self.Fdatos.pack_forget()
            self.Fdatos2.pack_forget()
            self.Fdatos3.pack(expand=True, fill='both')

        self.img_title2=tk.PhotoImage(file="Src/Opregre1.png")
        self.titulo2= tk.Button(self.vregresion,image=self.img_title2, border=0,command=visualizarframe1)
        self.titulo2.pack(side=TOP)

        self.img_title3=tk.PhotoImage(file="Src/Opregre2.png")
        self.titulo3= tk.Button(self.vregresion,image=self.img_title3, border=0,command=visualizarframe2)
        self.titulo3.pack(side=TOP)

        self.img_title4=tk.PhotoImage(file="Src/Opregre3.png")
        self.titulo4= tk.Button(self.vregresion,image=self.img_title4, border=0,command=visualizarframe3)
        self.titulo4.pack(side=TOP)

        self.x = Symbol('x')
        self.fun = vars(math)

        # FS --> FontStyle
        self.FStitulos = TkFont.Font(family='Segoe Print', size=18)
        self.FStexto = TkFont.Font(family='Segoe Print', size=12)

#FRAME 1
        self.Fdatos = tk.Frame(self.vregresion, background=color_fondo)
        self.lblTipo = ttk.Label(self.Fdatos, text='REGRESIÓN LINEAL', font=self.FStitulos)
        self.lblTipo.configure(background=color_fondo)
        self.lblTipo.pack(side=TOP)

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

#FRAME 2
        self.Fdatos2 = tk.Frame(self.vregresion, background=color_fondo)
        self.lblTipo2 = ttk.Label(self.Fdatos2, text='REGRESIÓN POLINOMIAL', font=self.FStitulos)
        self.lblTipo2.configure(background=color_fondo)
        self.lblTipo2.pack(side=TOP)

        self.lblDatosX2 = ttk.Label(self.Fdatos2, text='Valores de X separados por comas: ', font=self.FStexto)
        self.lblDatosX2.configure(background=color_fondo)
        self.lblDatosX2.place(x=70, y=70)

        self.inputDatosX2 = ttk.Entry(self.Fdatos2, background='white')
        self.inputDatosX2.configure(width=40)
        self.inputDatosX2.place(x=450, y=75)

        self.lblDatosY2 = ttk.Label(self.Fdatos2, text='Valores de Y separados por comas: ', font=self.FStexto)
        self.lblDatosY2.configure(background=color_fondo)
        self.lblDatosY2.place(x=70, y=140)

        self.inputDatosY2 = ttk.Entry(self.Fdatos2, background='white')
        self.inputDatosY2.configure(width=40)
        self.inputDatosY2.place(x=450, y=145)

        self.imgbtn2 = tk.PhotoImage(file="Src/btn.png")
        self.btnCalcular2= tk.Button(self.Fdatos2, image=self.imgbtn2,command=self.calcular1)
        self.btnCalcular2.place(x=100, y=220)

        self.lbltiporesultado = ttk.Label(self.Fdatos2, text='Polinomio de regresión', font=self.FStexto)
        self.lbltiporesultado.configure(background='#D3E4CD', width=45)
        self.lbltiporesultado.place(x=250, y=190)

        self.lblLineaRegresion2 = ttk.Label(self.Fdatos2, font=self.FStexto)
        self.lblLineaRegresion2.configure(background='#D3E4CD', width=35)
        self.lblLineaRegresion2.place(x=250, y=245)

        self.textPolinomio = Text(self.lblLineaRegresion2, width=70,
                             height=1, wrap='none', state='disable')

        self.textPolinomio.grid(row=0, column=1)

        self.scrollPolinomio = Scrollbar(self.lblLineaRegresion2, orient='horizontal')
        self.scrollPolinomio.config(command=self.textPolinomio.xview)
        self.scrollPolinomio.grid(row=0, column=0)

#FRAME3
        self.Fdatos3 = tk.Frame(self.vregresion, background=color_fondo)
        self.lblTipo3 = ttk.Label(self.Fdatos3, text='REGRESIÓN LINEAL MÚLTIPLE', font=self.FStitulos)
        self.lblTipo3.configure(background=color_fondo)
        self.lblTipo3.pack(side=TOP)

        self.lblDatosX13 = ttk.Label(self.Fdatos3, text='Valores de X1 separados por comas: ', font=self.FStexto)
        self.lblDatosX13.configure(background=color_fondo)
        self.lblDatosX13.place(x=70, y=70)

        self.inputDatosX13 = ttk.Entry(self.Fdatos3, background='white')
        self.inputDatosX13.configure(width=40)
        self.inputDatosX13.place(x=450, y=75)

        self.lblDatosX23 = ttk.Label(self.Fdatos3, text='Valores de X2 separados por comas: ', font=self.FStexto)
        self.lblDatosX23.configure(background=color_fondo)
        self.lblDatosX23.place(x=70, y=140)

        self.inputDatosX23 = ttk.Entry(self.Fdatos3, background='white')
        self.inputDatosX23.configure(width=40)
        self.inputDatosX23.place(x=450, y=145)

        self.lblDatosY3 = ttk.Label(self.Fdatos3, text='Valores de Y separados por comas: ', font=self.FStexto)
        self.lblDatosY3.configure(background=color_fondo)
        self.lblDatosY3.place(x=70, y=210)

        self.inputDatosY3 = ttk.Entry(self.Fdatos3, background='white')
        self.inputDatosY3.configure(width=40)
        self.inputDatosY3.place(x=450, y=215)

        self.imgbtn3 = tk.PhotoImage(file="Src/btn.png")
        self.btnCalcular3= tk.Button(self.Fdatos3, image=self.imgbtn3,command=self.calcular2)
        self.btnCalcular3.place(x=100, y=290)

        self.lblLineaRegresion3 = ttk.Label(self.Fdatos3, text='Plano de regresión', font=self.FStexto)
        self.lblLineaRegresion3.configure(background='#D3E4CD', width=45)
        self.lblLineaRegresion3.place(x=250, y=295)

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

#METODOS OPCION 2

    def calcular1(self):
            valoresx = self.inputDatosX2.get().split(',')
            print(valoresx)
            valoresx2 = list(map(float, valoresx))
            valores_x = np.array(valoresx2)

            valoresy = self.inputDatosY2.get().split(',')
            valoresy2 = list(map(float, valoresy))
            valores_y = np.array(valoresy2)

            linea = self.regresion_polinomial1(valores_x, valores_y)

            self.textPolinomio.config(state='normal')
            self.textPolinomio.delete('1.0',tk.END)
            self.textPolinomio.insert(tk.END, linea)
            self.textPolinomio.config(state='disable')

    def regresion_polinomial1(self, x, y):
        """
        x e y: Tabla de valores
        """
        n = x.shape[0]

        sumax = 0
        sumax2 = 0
        sumay = 0
        sumax3 = 0
        sumaxy = 0
        sumax4 = 0
        sumax2y = 0
        for i in range(n):

            sumax += x[i]
            sumax2 += x[i]**2
            sumay += y[i]
            sumax3 += x[i]**3
            sumaxy += x[i]*y[i]
            sumax4 += x[i]**4
            sumax2y += (x[i]**2)*y[i]

        A = np.array([[n, sumax, sumax2], [sumax, sumax2,
                    sumax3], [sumax2, sumax3, sumax4]])
        b = np.array([sumay, sumaxy, sumax2y])
        a = self.cramer1(A, b)
        #yest = a[0] + a[1]*x + a[2]*x**2
        modelo = "y = " + "(" + str(a[0]) + ")" + " + " + "(" + str(a[1]) + ")" + \
            "*x + " + "(" + str(a[2]) + ")" + "*x**2"

        return modelo

    def cramer1(self, A, b):
        """
        A y b: arrays de numpy
        """
        B = A.copy()
        B[:, 1] = A[:, 2]
        detA = A[0][0]*self.determinante1(A[1:, 1:]) - A[0][1]*self.determinante1(
            B[1:, 0:2]) + A[0][2]*self.determinante1(A[1:, 0:2])
        # para x1
        Mnx1 = A.copy()
        Mnx1[:, 0] = b
        B = Mnx1.copy()
        B[:, 1] = Mnx1[:, 2]
        numx1 = Mnx1[0][0]*self.determinante1(Mnx1[1:, 1:]) - Mnx1[0][1]*self.determinante1(
            B[1:, 0:2]) + Mnx1[0][2]*self.determinante1(Mnx1[1:, 0:2])

        # para x2
        Mnx2 = A.copy()
        Mnx2[:, 1] = b
        B = Mnx2.copy()
        B[:, 1] = Mnx2[:, 2]
        numx2 = Mnx2[0][0]*self.determinante1(Mnx2[1:, 1:]) - Mnx2[0][1]*self.determinante1(
            B[1:, 0:2]) + Mnx2[0][2]*self.determinante1(Mnx2[1:, 0:2])

        # para x3
        Mnx3 = A.copy()
        Mnx3[:, 2] = b
        B = Mnx3.copy()
        B[:, 1] = Mnx3[:, 2]
        numx3 = Mnx3[0][0]*self.determinante1(Mnx3[1:, 1:]) - Mnx3[0][1]*self.determinante1(
            B[1:, 0:2]) + Mnx3[0][2]*self.determinante1(Mnx3[1:, 0:2])

        x1 = numx1/detA
        x2 = numx2/detA
        x3 = numx3/detA
        X = np.array([x1, x2, x3])
        return X

    def determinante1(self, A):
        """
        A: array numpy de [2x2]
        """
        det = A[0][0]*A[1][1] - A[1][0]*A[0][1]
        return det

#METODOS OPCION 3
    def calcular2(self):
        valoresx1 = self.inputDatosX13.get().split(',')
        valoresx1_2 = list(map(float, valoresx1))
        valores_x1 = np.array(valoresx1_2)

        valoresx2 = self.inputDatosX23.get().split(',')
        valoresx2_2 = list(map(float, valoresx2))
        valores_x2 = np.array(valoresx2_2)

        valoresy = self.inputDatosY3.get().split(',')
        valoresy_2 = list(map(float, valoresy))
        valores_y = np.array(valoresy_2)

        plano = self.regresion_lineal_multiple2(
            valores_x1, valores_x2, valores_y)

        self.lblLineaRegresion3.config(text=plano)

    def regresion_lineal_multiple2(self, x1, x2, y):
        """
        x1, x2 son las variables. Arrays de numpy
        """
        n = x1.shape[0]
        sumax1, sumax2, sumay, sumax1q, sumax1x2, sumax1y, sumax2q, sumax2y = 0, 0, 0, 0, 0, 0, 0, 0

        for i in range(n):
            sumax1 += x1[i]
            sumax2 += x2[i]
            sumay += y[i]
            sumax1q += x1[i]**2
            sumax1x2 += x1[i]*x2[i]
            sumax1y += x1[i]*y[i]
            sumax2y += x2[i]*y[i]
            sumax2q += x2[i]**2

        A = np.array([[n, sumax1, sumax2], [sumax1, sumax1q,
                     sumax1x2], [sumax2, sumax1x2, sumax2q]])
        b = np.array([sumay, sumax1y, sumax2y])

        a = self.cramer2(A, b)

        modelo = "y = " + "(" + str(a[0]) + ")" + " + " + "(" + str(a[1]) + ")" + \
            "*x1 + " + "(" + str(a[2]) + ")" + "*x2"
        return modelo

    def cramer2(self, A, b):
        """
        A y b: arrays de numpy
        """
        B = A.copy()
        B[:, 1] = A[:, 2]
        detA = A[0][0]*self.determinante2(A[1:, 1:]) - A[0][1]*self.determinante2(
            B[1:, 0:2]) + A[0][2]*self.determinante2(A[1:, 0:2])
        # para x1
        Mnx1 = A.copy()
        Mnx1[:, 0] = b
        B = Mnx1.copy()
        B[:, 1] = Mnx1[:, 2]
        numx1 = Mnx1[0][0]*self.determinante2(Mnx1[1:, 1:]) - Mnx1[0][1]*self.determinante2(
            B[1:, 0:2]) + Mnx1[0][2]*self.determinante2(Mnx1[1:, 0:2])

        # para x2
        Mnx2 = A.copy()
        Mnx2[:, 1] = b
        B = Mnx2.copy()
        B[:, 1] = Mnx2[:, 2]
        numx2 = Mnx2[0][0]*self.determinante2(Mnx2[1:, 1:]) - Mnx2[0][1]*self.determinante2(
            B[1:, 0:2]) + Mnx2[0][2]*self.determinante2(Mnx2[1:, 0:2])

        # para x3
        Mnx3 = A.copy()
        Mnx3[:, 2] = b
        B = Mnx3.copy()
        B[:, 1] = Mnx3[:, 2]
        numx3 = Mnx3[0][0]*self.determinante2(Mnx3[1:, 1:]) - Mnx3[0][1]*self.determinante2(
            B[1:, 0:2]) + Mnx3[0][2]*self.determinante2(Mnx3[1:, 0:2])

        x1 = numx1/detA
        x2 = numx2/detA
        x3 = numx3/detA
        X = np.array([x1, x2, x3])
        return X

    def determinante2(self, A):
        """
        A: array numpy de [2x2]
        """
        det = A[0][0]*A[1][1] - A[1][0]*A[0][1]
        return det

    def creador(self):
      showinfo(message="Santiago Gomez - Github: SantiagoGM19 \nAlejandro Durango - Github: AlejandroDurango ", title="Creadores")
