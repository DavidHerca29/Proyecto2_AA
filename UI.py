import tkinter
import turtle
from random import randint
from tkinter import ttk
from tkinter import messagebox
from PIL import EpsImagePlugin, Image

from Arbol import Arbol
from imagenAA import obtenerSilueta, path1, path2

try:
    EpsImagePlugin.gs_windows_binary = r'C:\Program Files\gs\gs9.54.0\bin\gswin64c'
except:
    # El de Ale
    print("Fallo en el gs")
    # EpsImagePlugin.gs_windows_binary = r'C:\Program Files\gs\gs9.54.0\bin\gswin64c'


class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.geometry("1000x600")
        ventana.title("Fractal Trees")
        ventana.resizable(False, False)
        ventana.config(bg="lightgreen")

        # __________________________ LABELS
        self.mensajeGeneraciones = tkinter.Label(ventana, text="Selecciona una generacion", bg="lightgreen",
                                                 font=("Times New Roman", 16)) \
            .place(x=10, y=10)
        self.mensajeDatos = tkinter.Label(ventana, text="Datos del árbol", font=("Times New Roman", 16),
                                          bg="lightgreen") \
            .place(x=130, y=180)
        self.mensajeIndividuo = tkinter.Label(ventana, text="Selecciona al individuo", font=("Times New Roman", 16),
                                              bg="lightgreen") \
            .place(x=10, y=90)

        self.txdatoNumGen = tkinter.StringVar()
        self.txdatoNumGen.set("Generación: ")
        self.datoNumGen = tkinter.Label(ventana, textvariable=self.txdatoNumGen, font=("Times New Roman", 14), bg="lightgreen") \
            .place(x=10, y=210)

        self.txdatoPadre = tkinter.StringVar()
        self.txdatoPadre.set("Padre: ")
        self.datoPadre = tkinter.Label(ventana, textvariable=self.txdatoPadre, font=("Times New Roman", 14), bg="lightgreen") \
            .place(x=10, y=245)

        self.txdatoMadre = tkinter.StringVar()
        self.txdatoMadre.set("Madre: ")
        self.datoMadre = tkinter.Label(ventana, textvariable=self.txdatoMadre, font=("Times New Roman", 14), bg="lightgreen") \
            .place(x=10, y=280)

        self.txdatoTroncoL = tkinter.StringVar()
        self.txdatoTroncoL.set("Longitud inicial: ")
        self.datoTroncoL = tkinter.Label(ventana, textvariable=self.txdatoTroncoL, font=("Times New Roman", 14),
                                        bg="lightgreen") \
            .place(x=10, y=315)

        self.txdatoTroncoG = tkinter.StringVar()
        self.txdatoTroncoG.set("Grosor inicial: ")
        self.datoTroncoG = tkinter.Label(ventana, textvariable=self.txdatoTroncoG, font=("Times New Roman", 14), bg="lightgreen") \
            .place(x=10, y=345)

        self.txdatoDecLong = tkinter.StringVar()
        self.txdatoDecLong.set("Decremento de longitud: ")
        self.datoDecLong = tkinter.Label(ventana, textvariable=self.txdatoDecLong, font=("Times New Roman", 14),
                                         bg="lightgreen") \
            .place(x=10, y=380)

        self.txdatoCantidadRamas = tkinter.StringVar()
        self.txdatoCantidadRamas.set("Cantidad de ramas: ")
        self.datoCantidadRamas = tkinter.Label(ventana, textvariable=self.txdatoCantidadRamas, font=("Times New Roman", 14),
                                               bg="lightgreen") \
            .place(x=10, y=415)

        self.txdatoProfundidad = tkinter.StringVar()
        self.txdatoProfundidad.set("Profundidad: ")
        self.datoProfundidad = tkinter.Label(ventana, textvariable=self.txdatoProfundidad, font=("Times New Roman", 14),
                                             bg="lightgreen") \
            .place(x=10, y=445)

        self.txdatoDecAncho = tkinter.StringVar()
        self.txdatoDecAncho.set("Decremento de ancho: ")
        self.datoDecAncho = tkinter.Label(ventana, textvariable=self.txdatoDecAncho, font=("Times New Roman", 14),
                                          bg="lightgreen") \
            .place(x=10, y=480)

        self.txdatoAngulo = tkinter.StringVar()
        self.txdatoAngulo.set("Rango de ángulos: ")
        self.datoAngulo = tkinter.Label(ventana, textvariable=self.txdatoAngulo, font=("Times New Roman", 14),
                                        bg="lightgreen") \
            .place(x=10, y=515)

        self.txdatoNota = tkinter.StringVar()
        self.txdatoNota.set("Nota obtenida: ")
        self.datoNota = tkinter.Label(ventana, textvariable=self.txdatoNota, font=("Times New Roman", 14), bg="lightgreen") \
            .place(x=10, y=545)

        # ?____________________ cantidad de generaciones y PATHs de las siluetas cargadas

        self.matrizGlobal = []
        self.totalGeneraciones = []
        self.hijosPorGeneracion = []
        for i in range(1, 11):
            self.hijosPorGeneracion.append(str(i))

        self.silueta1 = obtenerSilueta(path1)
        self.silueta2 = obtenerSilueta(path2)

        # ----------- combobox numero de generaciones
        self.genString = tkinter.StringVar()
        self.generaciones = ttk.Combobox(ventana, textvariable=self.genString, width=30)
        self.generaciones['state'] = 'readonly'
        self.generaciones.place(x=10, y=50)

        # ----------- combobox numero de hijos
        self.hijoString = tkinter.StringVar()

        self.hijos = ttk.Combobox(ventana, textvariable=self.hijoString, width=30)
        self.hijos['values'] = self.hijosPorGeneracion
        self.hijos['state'] = 'readonly'
        self.hijos.place(x=10, y=120)

        # _____________ BOTON MANIPULACION COMBOBOX
        self.verinfoBT = tkinter.Button(ventana, command=self.darinfo, width=10, font=("Times New Roman", 14),
                                        bg="lightgreen", relief=tkinter.RAISED,
                                        text="Consultar").place(x=250, y=10)

        # ______________ TURTLE DRAWING
        self.HEIGHT = 600
        self.WIDTH = 600

        self.canvas = tkinter.Canvas(ventana)
        self.canvas.config(width=self.WIDTH, height=self.HEIGHT)
        self.canvas.place(x=400, y=0)

        # _________________ PANTALLA
        self.TurtleScreen = turtle.TurtleScreen(self.canvas)

        # __________ INICIALIZACION DEL LAPIZ
        self.maxTugo = turtle.RawTurtle(self.TurtleScreen)
        self.maxTugo.ht()

        self.TurtleScreen.tracer(0, 0)
        self.maxTugo.speed(0)
        self.maxTugo.up()
        self.maxTugo.seth(90)
        self.maxTugo.goto(-0.00, -266.00)
        self.maxTugo.down()

        self.ventana.update_idletasks()

    def actualizarGeneraciones(self):
        self.generaciones['values'] = self.totalGeneraciones

    def iniciarPantalla(self):
        self.TurtleScreen.clear()
        self.TurtleScreen.tracer(0, 0)
        self.maxTugo.speed(0)
        # __________________ SE COLOCA ABAJO Y EN EL CENTRO DE LA PANTALLA
        self.maxTugo.up()
        self.maxTugo.seth(90)
        self.maxTugo.goto(-0.00, -266.00)
        self.maxTugo.down()

    def validarDatos(self, grosorTronco, longTronco, profundidad, decrementoGrosor, decrementoLong, ramificaciones,
                     angulo,
                     esTronco):
        decrementoGrosor = sorted(decrementoGrosor)
        decrementoLong = sorted(decrementoLong)

        ramificaciones = sorted(ramificaciones)
        angulo = sorted(angulo)

        if grosorTronco > 18:
            grosorTronco = 18
        elif grosorTronco < 6:
            grosorTronco = 6
        if longTronco > 85:
            longTronco = 85
        elif longTronco < 60:
            longTronco = 60
        if profundidad > 6:
            profundidad = 6
        elif profundidad < 3:
            profundidad = 3
        if decrementoGrosor[0] < 1:
            decrementoGrosor[0] = 1
        elif decrementoGrosor[0] > 5:
            decrementoGrosor[0] = 5
        if decrementoGrosor[1] < 1:
            decrementoGrosor[1] = 1
        elif decrementoGrosor[1] > 5:
            decrementoGrosor[1] = 5
        if decrementoLong[0] < 3:
            decrementoLong[0] = 3
        elif decrementoLong[0] > 8:
            decrementoLong[0] = 8
        if decrementoLong[1] < 3:
            decrementoLong[1] = 3
        elif decrementoLong[1] > 8:
            decrementoLong[1] = 8
        if ramificaciones[0] < 3:
            ramificaciones[0] = 3
        elif ramificaciones[0] > 6:
            ramificaciones[0] = 6
        if ramificaciones[1] < 3:
            ramificaciones[1] = 3
        elif ramificaciones[1] > 6:
            ramificaciones[1] = 6
        if angulo[0] < 5:
            angulo[0] = 5
        elif angulo[0] > 60:
            angulo[0] = 60
        if angulo[1] < 5:
            angulo[1] = 5
        elif angulo[1] > 60:
            angulo[1] = 60
        self.crearArbol(grosorTronco, longTronco, profundidad, decrementoGrosor, decrementoLong, ramificaciones, angulo,
                        esTronco)

    def validarValores(self):
        gen = self.generaciones.get()
        num = self.hijos.get()
        if gen == "":
            gen = -1
        if num == "":
            num = -1
        return gen, num

    def colocarInfo(self, gen, num):
        arbol: Arbol = self.matrizGlobal[int(gen)-1][int(num)-1]
        self.txdatoNumGen.set("Generación: "+str(arbol.generacion))
        self.txdatoPadre.set("Padre: "+str(arbol.padre.numIndividuo))
        self.txdatoMadre.set("Madre: "+str(arbol.madre.numIndividuo))
        self.txdatoTroncoL.set("Longitud inicial: "+str(arbol.longitudTronco))
        self.txdatoTroncoG.set("Grosor inicial: "+str(arbol.grosorTronco))
        self.txdatoDecLong.set("Decremento de longitud: "+str(arbol.decrementoLongitud))
        self.txdatoCantidadRamas.set("Cantidad de ramas: "+str(arbol.ramificaciones))
        self.txdatoProfundidad.set("Profundidad: "+str(arbol.profundidad))
        self.txdatoDecAncho.set("Decremento de ancho: "+str(arbol.decrementoGrosor))
        self.txdatoAngulo.set("Rango de ángulos: "+str(arbol.angulo))
        self.txdatoNota.set("Nota obtenida: "+str(arbol.nota))

    def darinfo(self):
        generacion, numero = self.validarValores()

        if generacion == -1:
            messagebox.showinfo("Error", "Debe seleccionar tanto la generación como el individuo para ver su información")
            return
        filename = "imagenes\\imagen-"+generacion+"-"+numero+".png"
        self.TurtleScreen.bgpic(filename)
        self.colocarInfo(generacion, numero)
        self.ventana.update_idletasks()
        """
        try:
            self.TurtleScreen.bgpic(filename)
            self.colocarInfo(generacion, numero)
            self.ventana.update_idletasks()
        except:
            messagebox.showinfo("Error", "No se encontró el archivo")
            """

        return

    def crearArbol(self, grosorTronco, longTronco, profundidad, decrementoGrosor, decrementoLong, ramificaciones,
                   angulo,
                   esTronco):
        if profundidad <= 0:
            return
        elif esTronco:
            self.maxTugo.pensize(grosorTronco * 3)
            self.maxTugo.forward(longTronco * 2)
            """
            self.crearArbol((grosorTronco - randint(decrementoGrosor[0], decrementoGrosor[1])),
                       (longTronco - randint(decrementoLong[0], decrementoLong[1]))
                       , profundidad - 1, decrementoGrosor, decrementoLong, ramificaciones, angulo, False)
            return
            """
            anguloreal = randint(0, 8)

            direccion = randint(0, 1)
            if direccion == 1:
                self.maxTugo.right(anguloreal)
            else:
                self.maxTugo.left(anguloreal)

            grueso = grosorTronco
            if grueso < 0:
                grueso = 1
            self.maxTugo.pensize(grueso)

            movimiento = (longTronco * 2 // 3)
            if movimiento < 0:
                movimiento = 1
            self.maxTugo.forward(movimiento)
            ramificacion = (ramificaciones[0] // 2, ramificaciones[1] // 2)
            self.crearArbol((grosorTronco - randint(decrementoGrosor[0], decrementoGrosor[1])),
                            (longTronco - randint(decrementoLong[0], decrementoLong[1]) * 2)
                            , profundidad // 2, decrementoGrosor, decrementoLong, ramificacion, angulo, False)
            self.maxTugo.backward(movimiento)
            if direccion == 1:
                self.maxTugo.left(anguloreal)
            else:
                self.maxTugo.right(anguloreal)

        ramas = randint(ramificaciones[0], ramificaciones[1])
        while ramas > 0:
            anguloreal = randint(angulo[0], angulo[1])

            direccion = randint(0, 1)
            if direccion == 1:
                self.maxTugo.right(anguloreal)
            else:
                self.maxTugo.left(anguloreal)

            grueso = grosorTronco
            if grueso < 0:
                grueso = 1
            self.maxTugo.pensize(grueso)

            movimiento = (longTronco)
            if movimiento < 0:
                movimiento = 1
            self.maxTugo.forward(movimiento)

            self.crearArbol((grosorTronco - randint(decrementoGrosor[0], decrementoGrosor[1])),
                            (longTronco - randint(decrementoLong[0], decrementoLong[1]))
                            , profundidad - 1, decrementoGrosor, decrementoLong, ramificaciones, angulo, False)
            self.maxTugo.backward(movimiento)
            if direccion == 1:
                self.maxTugo.left(anguloreal)
            else:
                self.maxTugo.right(anguloreal)
            ramas -= 1


# TurtleScreen.update()


# arbol(25, 95, 7, (3, 9), (10, 12), (2, 4), (0, 45), True)


# avance.generarImagen()
# image1 = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))
# draw = ImageDraw.Draw(image1)
