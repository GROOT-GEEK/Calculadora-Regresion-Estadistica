from distutils.core import setup 
import py2exe
import math, tkinter,numpy,sympy,tkinter.font,tkinter.messagebox,matplotlib.pyplot


setup(
    name= "Calculadora Metodos Numericos",
    icon="Src/Icono.ico",
    version="1.0",
    windows=[{'script':"Interfaz.py",
    "icon_resources":[(1, "Icono.ico")]}],
)