import tkinter
import turtle

from PIL import Image, ImageDraw

import Arbol
from random import random, randint
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs9.54.0\bin\gswin64c'

# _________ INICIALZACION DE TKINTER
ventana = tkinter.Tk()
ventana.geometry("1000x600")
ventana.title("Fractal Trees")
ventana.resizable(False, False)
ventana.config(bg="lightgreen")

# __________________________ LABELS
mensajeGeneraciones = tkinter.Label(ventana, text="Selecciona una generacion", bg="lightgreen",
                                    font=("Times New Roman", 16)) \
    .place(x=10, y=10)
mensajeDatos = tkinter.Label(ventana, text="Datos del árbol", font=("Times New Roman", 16), bg="lightgreen") \
    .place(x=10, y=280)
mensajeIndividuo = tkinter.Label(ventana, text="Selecciona al individuo", font=("Times New Roman", 16), bg="lightgreen") \
    .place(x=10, y=160)

datoNumGen = tkinter.Label(ventana, text="Generación: ", font=("Times New Roman", 14), bg="lightgreen") \
    .place(x=10, y=310)
datoPadre = tkinter.Label(ventana, text="Padre: ", font=("Times New Roman", 14), bg="lightgreen") \
    .place(x=10, y=345)
datoMadre = tkinter.Label(ventana, text="Madre: ", font=("Times New Roman", 14), bg="lightgreen") \
    .place(x=10, y=380)
datoTronco = tkinter.Label(ventana, text="Tronco: ", font=("Times New Roman", 14), bg="lightgreen") \
    .place(x=10, y=415)
datoRangoDecremento = tkinter.Label(ventana, text="Decremento de tamaño: ", font=("Times New Roman", 14),
                                    bg="lightgreen") \
    .place(x=10, y=450)
datoCantidadRamas = tkinter.Label(ventana, text="Cantidad de ramas: ", font=("Times New Roman", 14), bg="lightgreen") \
    .place(x=10, y=485)
# cantidad de generaciones
cantidadGeneraciones = []

hijosPorGeneracion = []
for i in range(1, 11):
    hijosPorGeneracion.append(str(i))
historial = []
Ascendencia = ['Hola', 'Mundo']

# ----------- combobox numero de generaciones
genString = tkinter.StringVar()

generaciones = ttk.Combobox(ventana, textvariable=genString, width=30)
generaciones['values'] = cantidadGeneraciones
generaciones['state'] = 'readonly'
generaciones.place(x=10, y=50)

# ----------- combobox numero de generaicones
hijoString = tkinter.StringVar()

hijos = ttk.Combobox(ventana, textvariable=hijoString, width=30)
hijos['values'] = hijosPorGeneracion
hijos['state'] = 'readonly'
hijos.place(x=10, y=200)

# ______________ TURTLE DRAWING
HEIGHT = 600
WIDTH = 600

canvas = tkinter.Canvas(ventana)
canvas.config(width=WIDTH, height=HEIGHT)
canvas.place(x=400, y=0)

TurtleScreen = turtle.TurtleScreen(canvas)
TurtleScreen.tracer(0, 0)

# __________ INICIALIZACION DEL LAPIZ
maxTugo = turtle.RawTurtle(TurtleScreen)
maxTugo.speed(0)
maxTugo.ht()

# __________________ SE COLOCA ABAJO Y EN EL CENTRO DE LA PANTALLA
maxTugo.up()
maxTugo.left(90)
maxTugo.backward(HEIGHT * 4 / 9)
maxTugo.down()

# _________________ CARNITA
"""
historial = []
cantidadgeneraciones
cantidadHijosporGen
main {
    ponderado =0 
    mayorFitActual =0 
    mayorFitAnterior =0
    numGen = 0
    while (ponderadoGeneracion < 80 and mayorActual < 80)
        numGen ++
        if numGen ==1 :
            inicial() ==> tree() ==> fitness()
        else:
            Generacion(numGen) ==> tree() ==> fitness()
        78
        genpasada = 78
        ponderadoGeneracion
        
        mayorActual = obtenerMayorActual(numGen)
        

}
"""

def arbol(grosorTronco, longTronco, profundidad, decrementoGrosor, decrementoLong, ramificaciones, angulo, esTronco):
    if profundidad <= 0:
        return
    elif esTronco:
        maxTugo.pensize(grosorTronco*3//2)
        maxTugo.forward(longTronco*3//2)
        arbol((grosorTronco - randint(decrementoGrosor[0], decrementoGrosor[1])),
              (longTronco - randint(decrementoLong[0], decrementoLong[1]))
              , profundidad - 1, decrementoGrosor, decrementoLong, ramificaciones, angulo, False)
        return

    ramas = randint(ramificaciones[0], ramificaciones[1])
    #ramas = 1
    while ramas > 0:
        anguloreal = randint(angulo[0], angulo[1])

        direccion = randint(0, 1)
        if direccion == 1:
            maxTugo.right(anguloreal)
        else:
            maxTugo.left(anguloreal)

        grueso = grosorTronco
        if grueso < 0:
            grueso = 1
        maxTugo.pensize(grueso)

        movimiento = (longTronco)
        if movimiento < 0:
            movimiento = 1
        maxTugo.forward(movimiento)

        arbol((grosorTronco - randint(decrementoGrosor[0], decrementoGrosor[1])),
              (longTronco - randint(decrementoLong[0], decrementoLong[1]))
              , profundidad - 1, decrementoGrosor, decrementoLong, ramificaciones, angulo, False)
        maxTugo.backward(movimiento)
        if direccion == 1:
            maxTugo.left(anguloreal)
        else:
            maxTugo.right(anguloreal)
        ramas -= 1

"""maxTugo.up()
maxTugo.forward(150)
maxTugo.down()"""
# arbol(grosorTronco, longTronco, profundidad, decrementoGrosor, decrementoLong, ramificaciones, angulo, esTronco)
arbol(25, 75, 7, (7, 9), (4, 12), (4, 8), (15, 35), True)

TurtleScreen.update()

image1 = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))
draw = ImageDraw.Draw(image1)

fileName = "imagen-1-1"

TurtleScreen.getcanvas().postscript(file=fileName+".eps")
img = Image.open(fileName + '.eps')
img.save(fileName + '.png', 'png')

ventana.mainloop()
