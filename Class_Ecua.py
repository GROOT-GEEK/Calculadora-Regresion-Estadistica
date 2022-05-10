import matplotlib.pyplot as plt
import math
import tkinter as tk
import tkinter.font as TkFont
import numpy as np
from tkinter import ttk
from sympy import *
from tkinter.messagebox import *
from tkinter import *

icono = "Src/Icono.ico"
tamano_default = '800x600'
color_fondo ="#FEF5ED"


class Ecuaciones:
    def __init__(self):
        self.vecuaciones = Toplevel()
        self.vecuaciones.geometry(tamano_default)
        self.vecuaciones.resizable(width=0, height=0)
        self.vecuaciones.iconbitmap(icono)
        self.vecuaciones.title('Calculadora Ecuaciones Diferenciales')
        self.vecuaciones.configure(bg=color_fondo)

        self.img_title=tk.PhotoImage(file="Src/tecuaciones.png")
        self.titulo= tk.Button(self.vecuaciones,image=self.img_title, border=0,command= self.creador)
        self.titulo.pack(side=TOP)

        self.Fdatos = tk.Frame(self.vecuaciones, bg=color_fondo)
        self.Fdatos2 = tk.Frame(self.vecuaciones, bg=color_fondo)


        def visualizarframe1 ():
            self.Fdatos2.pack_forget()
            self.Fdatos.pack(expand=True, fill='both')
            self.vecuaciones.geometry("800x700")


        def visualizarframe2 ():
            self.Fdatos.pack_forget()
            self.Fdatos2.pack(expand=True, fill='both')
            self.vecuaciones.geometry(tamano_default)

        self.img_title2=tk.PhotoImage(file="Src/OpEcua2.png")
        self.titulo2= tk.Button(self.vecuaciones,image=self.img_title2, border=0,command=visualizarframe1)
        self.titulo2.pack(side=TOP)

        self.img_title3=tk.PhotoImage(file="Src/OpEcua1.png")
        self.titulo3= tk.Button(self.vecuaciones,image=self.img_title3, border=0,command=visualizarframe2)
        self.titulo3.pack(side=TOP)

        self.x = Symbol('x')
        self.y = Symbol('y')
        self.y1 = Symbol('y1')
        self.y2 = Symbol('y2')
        self.fun = vars(math)

        # FS --> FontStyle
        self.FStitulos = TkFont.Font(family='Segoe Print', size=18)
        self.FStexto = TkFont.Font(family='Segoe Print', size=12)

#FRAME 1
        self.lblTipo = ttk.Label(self.Fdatos, text='ECUACIONES DIFERENCIALES 2X2', font=self.FStitulos)
        self.lblTipo.configure(background=color_fondo)
        self.lblTipo.pack(side=TOP)

        self.lblCondInicialx = ttk.Label(self.Fdatos, text='Condición Inicial X1: ', font=self.FStexto)
        self.lblCondInicialx.configure(background=color_fondo)
        self.lblCondInicialx.place(x=70, y=50)

        self.inputCondInicialx = ttk.Entry(self.Fdatos, background='white')
        self.inputCondInicialx.configure(width=40)
        self.inputCondInicialx.place(x=450, y=55)

        self.lblCondInicial1x = ttk.Label(self.Fdatos, text='Condición Inicial X2: ', font=self.FStexto)
        self.lblCondInicial1x.configure(background=color_fondo)
        self.lblCondInicial1x.place(x=70, y=80)

        self.inputCondInicial1x = ttk.Entry(self.Fdatos, background='white')
        self.inputCondInicial1x.configure(width=40)
        self.inputCondInicial1x.place(x=450, y=85)

        self.lblCondInicialy = ttk.Label(self.Fdatos, text='Condición Inicial Y1: ', font=self.FStexto)
        self.lblCondInicialy.configure(background=color_fondo)
        self.lblCondInicialy.place(x=70, y=110)

        self.inputCondInicialY= ttk.Entry(self.Fdatos, background='white')
        self.inputCondInicialY.configure(width=40)
        self.inputCondInicialY.place(x=450, y=115)

        self.lblCondInicial1y = ttk.Label(self.Fdatos, text='Condición Inicial Y2: ', font=self.FStexto)
        self.lblCondInicial1y.configure(background=color_fondo)
        self.lblCondInicial1y.place(x=70, y=140)

        self.inputCondInicial1Y= ttk.Entry(self.Fdatos, background='white')
        self.inputCondInicial1Y.configure(width=40)
        self.inputCondInicial1Y.place(x=450, y=145)

        self.lblEcua1 = ttk.Label(self.Fdatos, text='Ecuación Diferencial 1: ', font=self.FStexto)
        self.lblEcua1.configure(background=color_fondo)
        self.lblEcua1.place(x=70, y=170)

        self.inputEcua1 = ttk.Entry(self.Fdatos, background='white')
        self.inputEcua1.configure(width=40)
        self.inputEcua1.place(x=450, y=175)

        self.lblEcua2 = ttk.Label(self.Fdatos, text='Ecuación Diferencial 2: ', font=self.FStexto)
        self.lblEcua2.configure(background=color_fondo)
        self.lblEcua2.place(x=70, y=200)

        self.inputEcua2 = ttk.Entry(self.Fdatos, background='white')
        self.inputEcua2.configure(width=40)
        self.inputEcua2.place(x=450, y=205)

        self.lblDistanciah = ttk.Label(self.Fdatos, text='Distancia h: ', font=self.FStexto)
        self.lblDistanciah.configure(background=color_fondo)
        self.lblDistanciah.place(x=70, y=230)

        self.inputDistanciah = ttk.Entry(self.Fdatos, background='white')
        self.inputDistanciah.configure(width=40)
        self.inputDistanciah.place(x=450, y=235)

        self.lblPuntoIni = ttk.Label(self.Fdatos, text='Punto Inicial: ', font=self.FStexto)
        self.lblPuntoIni.configure(background=color_fondo)
        self.lblPuntoIni.place(x=70, y=260)

        self.inputPuntoIni = ttk.Entry(self.Fdatos, background='white')
        self.inputPuntoIni.configure(width=40)
        self.inputPuntoIni.place(x=450, y=265)

        self.lblPuntofinal = ttk.Label(self.Fdatos, text='Punto Final: ', font=self.FStexto)
        self.lblPuntofinal.configure(background=color_fondo)
        self.lblPuntofinal.place(x=70, y=290)

        self.inputPuntofinal = ttk.Entry(self.Fdatos, background='white')
        self.inputPuntofinal.configure(width=40)
        self.inputPuntofinal.place(x=450, y=295)

        self.imgbtn = tk.PhotoImage(file="Src/btn.png")
        self.btnCalcular= tk.Button(self.Fdatos, image=self.imgbtn,command=self.calcular)
        self.btnCalcular.place(x=70, y=375)

        self.lblResultadoX = ttk.Label( self.Fdatos, font=self.FStexto)
        self.lblResultadoX.configure(background='#D3E4CD', width=20)
        self.lblResultadoX.place(x=210, y=335)

        self.lblResultadoY1 = ttk.Label( self.Fdatos, font=self.FStexto)
        self.lblResultadoY1.configure(background='#D3E4CD', width=20)
        self.lblResultadoY1.place(x=210, y=375)

        self.lblResultadoY21 = ttk.Label( self.Fdatos, font=self.FStexto)
        self.lblResultadoY21.configure(background='#D3E4CD', width=20)
        self.lblResultadoY21.place(x=210, y=415)

        self.textXsol1 = Text(self.lblResultadoX, width=50, height=1, wrap='none',state='disable')
        self.textY1sol1 = Text(self.lblResultadoY1, width=50,height=1, wrap='none',state='disable')
        self.textY2sol1 = Text(self.lblResultadoY21, width=50,height=1, wrap='none', state='disable')

        self.textXsol1.grid(row=0, column=1)
        self.textY1sol1.grid(row=0, column=1)
        self.textY2sol1.grid(row=0, column=1)

        self.scrollx1 = Scrollbar(self.lblResultadoX, orient='horizontal')
        self.scrollx1.config(command=self.textXsol1.xview)
        self.scrollx1.grid(row=0, column=0)

        self.scrolly_11 = Scrollbar(self.lblResultadoY1, orient='horizontal')
        self.scrolly_11.config(command=self.textY1sol1.xview)
        self.scrolly_11.grid(row=0, column=0)

        self.scrolly_21 = Scrollbar(self.lblResultadoY21, orient='horizontal')
        self.scrolly_21.config(command=self.textY2sol1.xview)
        self.scrolly_21.grid(row=0, column=0)

        self.textXsol1.config(xscrollcommand=self.scrollx1.set)
        self.textY1sol1.config(xscrollcommand=self.scrolly_11.set)
        self.textY2sol1.config(xscrollcommand=self.scrolly_21.set)

#FRAME 2
        self.lblTipo2 = ttk.Label(self.Fdatos2, text='ECUACIÓN DIFERENCIAL RUNGE-KUTTA', font=self.FStitulos)
        self.lblTipo2.configure(background=color_fondo)
        self.lblTipo2.pack(side=TOP)

        self.lblCondInicialx2 = ttk.Label(self.Fdatos2, text='Condición Inicial X: ', font=self.FStexto)
        self.lblCondInicialx2.configure(background=color_fondo)
        self.lblCondInicialx2.place(x=70, y=50)

        self.inputCondInicialx2 = ttk.Entry(self.Fdatos2, background='white')
        self.inputCondInicialx2.configure(width=40)
        self.inputCondInicialx2.place(x=450, y=55)

        self.lblCondInicialy2 = ttk.Label(self.Fdatos2, text='Condición Inicial Y: ', font=self.FStexto)
        self.lblCondInicialy2.configure(background=color_fondo)
        self.lblCondInicialy2.place(x=70, y=90)

        self.inputCondInicialY2= ttk.Entry(self.Fdatos2, background='white')
        self.inputCondInicialY2.configure(width=40)
        self.inputCondInicialY2.place(x=450, y=95)

        self.lblEcua12 = ttk.Label(self.Fdatos2, text='Ecuación Diferencial: ', font=self.FStexto)
        self.lblEcua12.configure(background=color_fondo)
        self.lblEcua12.place(x=70, y=130)

        self.inputEcua12 = ttk.Entry(self.Fdatos2, background='white')
        self.inputEcua12.configure(width=40)
        self.inputEcua12.place(x=450, y=135)

        self.lblDistanciah2 = ttk.Label(self.Fdatos2, text='Distancia h: ', font=self.FStexto)
        self.lblDistanciah2.configure(background=color_fondo)
        self.lblDistanciah2.place(x=70, y=170)

        self.inputDistanciah2 = ttk.Entry(self.Fdatos2, background='white')
        self.inputDistanciah2.configure(width=40)
        self.inputDistanciah2.place(x=450, y=175)

        self.lblPuntoIni2 = ttk.Label(self.Fdatos2, text='Punto Inicial: ', font=self.FStexto)
        self.lblPuntoIni2.configure(background=color_fondo)
        self.lblPuntoIni2.place(x=70, y=210)

        self.inputPuntoIni2 = ttk.Entry(self.Fdatos2, background='white')
        self.inputPuntoIni2.configure(width=40)
        self.inputPuntoIni2.place(x=450, y=215)

        self.lblPuntofinal2 = ttk.Label(self.Fdatos2, text='Punto Final: ', font=self.FStexto)
        self.lblPuntofinal2.configure(background=color_fondo)
        self.lblPuntofinal2.place(x=70, y=250)

        self.inputPuntofinal2 = ttk.Entry(self.Fdatos2, background='white')
        self.inputPuntofinal2.configure(width=40)
        self.inputPuntofinal2.place(x=450, y=255)

        self.imgbtn2 = tk.PhotoImage(file="Src/btn.png")
        self.btnCalcular2= tk.Button(self.Fdatos2, image=self.imgbtn2,command=self.calcular2)
        self.btnCalcular2.place(x=70, y=300)

        self.lblResultadoX2 = ttk.Label( self.Fdatos2, font=self.FStexto)
        self.lblResultadoX2.configure(background='#D3E4CD', width=20)
        self.lblResultadoX2.place(x=210, y=295)

        self.lblResultadoY2 = ttk.Label( self.Fdatos2, font=self.FStexto)
        self.lblResultadoY2.configure(background='#D3E4CD', width=20)
        self.lblResultadoY2.place(x=210, y=335)

        self.textXsol = Text(self.lblResultadoX2, width=60,height=1, wrap='none', state='disable')
        self.textYsol = Text(self.lblResultadoY2, width=60,height=1, wrap='none', state='disable')

        self.textXsol.grid(row=0, column=1)
        self.textYsol.grid(row=0, column=1)

        self.scrollx = Scrollbar(self.lblResultadoX2, orient='horizontal')
        self.scrollx.config(command=self.textXsol.xview)
        self.scrollx.grid(row=0, column=0)

        self.scrolly = Scrollbar(self.lblResultadoY2, orient='horizontal')
        self.scrolly.config(command=self.textYsol.xview)
        self.scrolly.grid(row=0, column=0)

        self.textXsol.config(xscrollcommand=self.scrollx.set)
        self.textYsol.config(xscrollcommand=self.scrolly.set)

#METODO 1
    def calcular(self):
        condicionIncialx_1 = float(self.inputCondInicialx.get())
        condicionInicialy_1 = float(self.inputCondInicialY.get())
        condicionIncialx_2 = float(self.inputCondInicial1x.get())
        condicionInicialy_2 = float(self.inputCondInicial1Y.get())
        ecuacionDiferencial1 = self.inputEcua1.get()
        ecuacionDiferencial2 = self.inputEcua2.get()
        distanciah = float(self.inputDistanciah.get())
        puntoInicial = float(self.inputPuntoIni.get())
        puntoFinal = float(self.inputPuntofinal.get())
        condicionInicial= [(condicionIncialx_1,condicionInicialy_1), (condicionIncialx_2,condicionInicialy_2)]
        funciones = [ecuacionDiferencial1, ecuacionDiferencial2]

        x_sol, y1_sol, y2_sol = self.sol_SistemaEDOs_RK1(condicionInicial ,funciones, distanciah, puntoInicial, puntoFinal)

        xsol = ",".join([str(_) for _ in x_sol])
        y1sol = ",".join([str(_) for _ in y1_sol])
        y2sol = ",".join([str(_) for _ in y2_sol])

        self.textXsol1.config(state='normal')
        self.textXsol1.delete('1.0',tk.END)
        self.textXsol1.insert(tk.END, xsol)
        self.textXsol1.config(state='disable')

        self.textY1sol1.config(state='normal')
        self.textY1sol1.delete('1.0',tk.END)
        self.textY1sol1.insert(tk.END, y1sol)
        self.textY1sol1.config(state='disable')

        self.textY2sol1.config(state='normal')
        self.textY2sol1.delete('1.0',tk.END)
        self.textY2sol1.insert(tk.END, y2sol)
        self.textY2sol1.config(state='disable')

        self.grafica = Toplevel()
        self.grafica.geometry("800x500")
        self.grafica.title("Grafica")
        self.grafica.resizable(width=0, height=0)
        plt.plot(x_sol,y1_sol)
        plt.plot(x_sol,y2_sol)
        plt.savefig("grafico.png")
        self.img_fra=tk.PhotoImage(file="grafico.png")
        plt.clf()
        self.graficaI= tk.Button(self.grafica,image=self.img_fra, border=0)
        self.graficaI.pack(side=TOP)

    def sol_SistemaEDOs_RK1(self, ci, funciones, h, xi, xf):
        n = int((xf-xi)/h)
        xsol = [ci[0][0]]
        y1sol = [ci[0][1]]
        y2sol = [ci[1][1]]

        f1 = funciones[0]
        f2 = funciones[1]

        for i in range(n):
            #solucion euler
            # eval(dydx, self.fun, {'x': x+h, 'y': y+k3*h})
            # k11 = f1(xsol[i],y1sol[i], y2sol[i])
            k11 = eval(f1,self.fun,{'x': xsol[i], 'y1': y1sol[i], 'y2': y2sol[i]})
            # k12 = f2(xsol[i],y1sol[i], y2sol[i])
            k12 = eval(f2,self.fun,{'x':xsol[i],'y1':y1sol[i],'y2':y2sol[i]})
            ym1 = y1sol[i] + k11*(h/2)
            ym2 = y2sol[i] + k12*(h/2)

            # k21 = f1(xsol[i]+(1/2)*h, ym1, ym2)
            k21 = eval(f1,self.fun,{'x':xsol[i]+(1/2)*h,'y1':ym1,'y2':ym2})
            # k22 = f2(xsol[i]+(1/2)*h, ym1, ym2)
            k22 = eval(f2,self.fun,{'x':xsol[i]+(1/2)*h,'y1':ym1,'y2':ym2})
            ym1 = y1sol[i] + k21*(h/2)
            ym2 = y2sol[i] + k22*(h/2)

            # k31 = f1(xsol[i]+(1/2)*h, ym1, ym2)
            k31 = eval(f1,self.fun,{'x':xsol[i]+(1/2)*h,'y1':ym1,'y2':ym2})
            # k32 = f2(xsol[i]+(1/2)*h, ym1, ym2)
            k32 = eval(f2,self.fun,{'x':xsol[i]+(1/2)*h,'y1':ym1,'y2':ym2})
            ym1 = y1sol[i] + k31*h
            ym2 = y2sol[i] + k32*h

            # k41 = f1(xsol[i] + h, ym1, ym2)
            k41 = eval(f1,self.fun,{'x':xsol[i] + h,'y1':ym1,'y2':ym2})
            # k42 = f2(xsol[i] + h, ym1, ym2)
            k42 = eval(f2,self.fun,{'x':xsol[i] + h,'y1':ym1,'y2':ym2})

            yn1 = y1sol[i] + (1/6)*(k11 + 2*k21 + 2*k31 + k41)*h
            y1sol.append(yn1)

            yn2 = y2sol[i] + (1/6)*(k12 + 2*k22 + 2*k32 + k42)*h
            y2sol.append(yn2)

            xsol.append(xsol[i] + h)

        return xsol, y1sol, y2sol

#METODO 2

    def calcular2(self):
        condicionIncial = float(self.inputCondInicialx2.get())
        condicionFinal = float(self.inputCondInicialY2.get())
        ecuacionDiferencial = self.inputEcua12.get()
        distanciah = float(self.inputDistanciah2.get())
        puntoInicial = float(self.inputPuntoIni2.get())
        puntoFinal = float(self.inputPuntofinal2.get())

        x_sol, y_sol = self.RK_cuartoOrden1(condicionIncial, condicionFinal,
        ecuacionDiferencial, distanciah, puntoInicial, puntoFinal)

        xsol = ",".join([str(_) for _ in x_sol])
        ysol = ",".join([str(_) for _ in y_sol])
        self.textXsol.config(state='normal')
        self.textXsol.delete('1.0',tk.END)
        self.textXsol.insert(tk.END, xsol)
        self.textXsol.config(state='disable')

        self.textYsol.config(state='normal')
        self.textYsol.delete('1.0',tk.END)
        self.textYsol.insert(tk.END, ysol)
        self.textYsol.config(state='disable')

        self.grafica2 = Toplevel()
        self.grafica2.geometry("800x500")
        self.grafica2.title("Grafica")
        self.grafica2.resizable(width=0, height=0)
        plt.plot(x_sol,y_sol)
        plt.savefig("grafico2.png")
        self.img_fra2=tk.PhotoImage(file="grafico2.png")
        plt.clf()
        self.graficaII= tk.Button(self.grafica2,image=self.img_fra2, border=0)
        self.graficaII.pack(side=TOP)

    def RK_cuartoOrden1(self, x, y, dydx, h, xi, xf):
            xsol = [x]
            ysol = [y]
            n = int((xf-xi)/h)

            for i in range(n):
                # k1 = dydx(x,y)
                k1 = eval(dydx, self.fun, {'x': x, 'y': y})
                # k2 = dydx(x+(1/2)*h, y+(1/2)*k1*h)
                k2 = eval(dydx, self.fun, {'x': x+(1/2)*h, 'y': y+(1/2)*k1*h})
                # k3 = dydx(x+(1/2)*h, y + (1/2)*k2*h)
                k3 = eval(dydx, self.fun, {'x': x+(1/2)*h, 'y': y + (1/2)*k2*h})
                # k4 = dydx(x + h, y + k3*h)
                k4 = eval(dydx, self.fun, {'x': x+h, 'y': y+k3*h})

                yn = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*h
                ysol.append(yn)
                y = yn

                xn = x + h
                xsol.append(xn)
                x = xn

            return xsol, ysol

    def creador(self):
        showinfo(message="Santiago Gomez - Github: SantiagoGM19 \nAlejandro Durango - Github: AlejandroDurango ", title="Creadores")

