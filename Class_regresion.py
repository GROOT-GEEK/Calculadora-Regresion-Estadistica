from tkinter import *
import tkinter as tk
from tkinter import filedialog
import tkinter.font as TkFont
from tkinter import ttk
from sympy import *
import numpy as np
import math
from tkinter.messagebox import *
import matplotlib.pyplot as plt
import pandas as pd
import os



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
        self.Fdatos2 = tk.Frame(self.vregresion, bg=color_fondo)
        self.ruta =""
        self.lectura= pd.DataFrame()
        
        def visualizarframe1 ():
            self.Fdatos2.pack_forget()
            self.Fdatos.pack(expand=True, fill='both')
            
            
        def visualizarframe2 ():
            try:
                self.Fdatos.pack_forget()
                self.ruta=abrir_archivo()
                self.lectura = pd.read_csv(self.ruta,sep = ';')            
                showinfo(message="Cargando archivo")
                path = self.ruta
                extension = os.path.splitext(path)
                if(extension[1] == ".csv" and self.lectura.size>0):
                    self.btnCalcular2.configure(state="active")
                    self.imgok=tk.PhotoImage(file="Src/archivook.png")
                    self.imagenok= tk.Button(self.Fdatos2,image=self.imgok, border=0)
                    self.imagenok.place(x=250, y=70)
                    self.Fdatos2.pack(expand=True, fill='both')
            except:
                self.btnCalcular2.configure(state="disabled")
                self.imgoerror=tk.PhotoImage(file="Src/errorarchivo.png")
                self.imagenerror= tk.Button(self.Fdatos2,image=self.imgoerror, border=0)
                self.imagenerror.place(x=250, y=70)
                self.Fdatos2.pack(expand=True, fill='both')
                showinfo(message="Error cargando archivo, \nIntenta nuevamente \nVerifica el tipo de archivo o datos")
                pass
                
        
        def abrir_archivo():
            archivo_abierto=filedialog.askopenfilename(initialdir = "/",
            title = "Seleccione archivo",filetypes = (("csv files","*.csv"),("all files","*.*")))
            return archivo_abierto
        
        self.img_title2=tk.PhotoImage(file="Src/Opregre1.png")
        self.titulo2= tk.Button(self.vregresion,image=self.img_title2, border=0,command=visualizarframe1)
        self.titulo2.pack(side=TOP)

        self.img_title3=tk.PhotoImage(file="Src/Opregre2.png")
        self.titulo3= tk.Button(self.vregresion,image=self.img_title3, border=0,command=visualizarframe2)
        self.titulo3.pack(side=TOP)

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
      
#FRAME 2        
        self.imgbtn2 = tk.PhotoImage(file="Src/btn.png")
        self.btnCalcular2= tk.Button(self.Fdatos2, image=self.imgbtn2,command=self.calcular1)
        self.btnCalcular2.place(x=100, y=220)

        self.lblLineaRegresion2 = ttk.Label(self.Fdatos2, text='Linea de regresión', font=self.FStexto)
        self.lblLineaRegresion2.configure(background='#D3E4CD', width=45)
        self.lblLineaRegresion2.place(x=250, y=225)

        self.lblCoeficienteDeterminacion2 = ttk.Label(self.Fdatos2, text='Coeficiente de determinación', font=self.FStexto)
        self.lblCoeficienteDeterminacion2.configure(background='#D3E4CD', width=45)
        self.lblCoeficienteDeterminacion2.place(x=250, y=265)

        self.lblCoeficienteCorrelacion2 = ttk.Label(self.Fdatos2, text='Coeficiente de correlación', font=self.FStexto)
        self.lblCoeficienteCorrelacion2.configure(background='#D3E4CD', width=45)
        self.lblCoeficienteCorrelacion2.place(x=250, y=305)
        
#METODOS OPCIÓN 1
    def calcular(self):
        valoresx = self.inputDatosX.get().split(',')
        valoresx2 = list(map(float, valoresx))
        valores_x = np.array(valoresx2)

        valoresy = self.inputDatosY.get().split(',')
        valoresy2 = list(map(float, valoresy))
        valores_y = np.array(valoresy2)

        yest,linea, coeficienteDeterminacion, coeficienteCorrelacion = self.regresion_lineal(
            valores_x, valores_y)

        self.lblLineaRegresion.config(text=linea)
        self.lblCoeficienteDeterminacion.config(text=coeficienteDeterminacion)
        self.lblCoeficienteCorrelacion.config(text=coeficienteCorrelacion)
        
        self.grafica = Toplevel()
        self.grafica.geometry("800x500")
        self.grafica.title("Grafica")
        self.grafica.resizable(width=0, height=0)
        plt.style.use('seaborn-whitegrid')
        plt.scatter(valores_x,valores_y)
        plt.plot(valores_x,yest)
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
        
        return yest, linea, coeDeterminacion, coeCorrelacion
    
#METODOS OPCION 2

    def calcular1(self):
        valores_x=[]
        valores_y=[]
        for i in range(len(self.lectura)):  
            valores_x.append(self.lectura.iloc[i,0])
            valores_y.append(self.lectura.iloc[i,1])
    
        valoresx = list(map(float, valores_x))
        valoresy = list(map(float, valores_y))

        valores_x = np.array(valoresx)
        valores_y = np.array(valoresy)
        
        yest,linea, coeficienteDeterminacion, coeficienteCorrelacion = self.regresion_lineal(
            valores_x, valores_y)

        self.lblLineaRegresion2.config(text=linea)
        self.lblCoeficienteDeterminacion2.config(text=coeficienteDeterminacion)
        self.lblCoeficienteCorrelacion2.config(text=coeficienteCorrelacion)
        
        self.grafica = Toplevel()
        self.grafica.geometry("800x500")
        self.grafica.title("Grafica")
        self.grafica.resizable(width=0, height=0)
        plt.style.use('seaborn-whitegrid')
        plt.scatter(valores_x,valores_y)
        plt.plot(valores_x,yest)
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
        
        return yest, linea, coeDeterminacion, coeCorrelacion


    def creador(self):
            showinfo(message="Jessica Bilbao - Github BilbaoJ \nSantiago Gomez - Github: SantiagoGM19 \nAlejandro Durango - Github: GROOT-GEEK ",
                title="Creadores")