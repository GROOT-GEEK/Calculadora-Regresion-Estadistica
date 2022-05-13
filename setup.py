from distutils.core import setup 
import py2exe
import sympy.printing.gtk,math,os,pandas,tkinter,numpy,sympy,tkinter.font,tkinter.messagebox,matplotlib.pyplot,tkinter.filedialog

setup(
    name= "Calculadora Regresión",
    icon="Src/Icono.ico",
    version="1.0",
    windows=[{'script':"Interfaz.py",
    "icon_resources":[(1, "Icono.ico")]}],
)