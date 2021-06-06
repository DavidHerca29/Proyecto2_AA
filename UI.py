import tkinter
import turtle
from random import randint
from tkinter import ttk
from PIL import EpsImagePlugin, Image
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
        self.mensajeDatos = tkinter.Label(ventana, text="Datos del árbol", font=("Times New Roman", 16), bg="lightgreen") \
            .place(x=130, y=180)
        self.mensajeIndividuo = tkinter.Label(ventana, text="Selecciona al individuo", font=("Times New Roman", 16),
                                         bg="lightgreen") \
            .place(x=10, y=90)

        self.datoNumGen = tkinter.Label(ventana, text="Generación: ", font=("Times New Roman", 14), bg="lightgreen") \
            .place(x=10, y=210)
        self.datoPadre = tkinter.Label(ventana, text="Padre: ", font=("Times New Roman", 14), bg="lightgreen") \
            .place(x=10, y=245)
        self.datoMadre = tkinter.Label(ventana, text="Madre: ", font=("Times New Roman", 14), bg="lightgreen") \
            .place(x=10, y=280)
        self.datoTronco = tkinter.Label(ventana, text="Longitud inicial: ", font=("Times New Roman", 14), bg="lightgreen") \
            .place(x=10, y=315)
        self.datoTronco = tkinter.Label(ventana, text="Grosor inicial: ", font=("Times New Roman", 14), bg="lightgreen") \
            .place(x=10, y=345)
        self.datoDecLong = tkinter.Label(ventana, text="Decremento de longitud: ", font=("Times New Roman", 14),
                                    bg="lightgreen") \
            .place(x=10, y=380)
        self.datoCantidadRamas = tkinter.Label(ventana, text="Cantidad de ramas: ", font=("Times New Roman", 14),
                                          bg="lightgreen") \
            .place(x=10, y=415)
        self.datoProfundidad = tkinter.Label(ventana, text="Profundidad: ", font=("Times New Roman", 14), bg="lightgreen") \
            .place(x=10, y=445)
        self.datoDecAncho = tkinter.Label(ventana, text="Decremento de ancho: ", font=("Times New Roman", 14),
                                     bg="lightgreen") \
            .place(x=10, y=480)
        self.datoAngulo = tkinter.Label(ventana, text="Rango de ángulos: ", font=("Times New Roman", 14), bg="lightgreen") \
            .place(x=10, y=515)
        self.datoNota = tkinter.Label(ventana, text="Nota obtenida: ", font=("Times New Roman", 14), bg="lightgreen") \
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

    def validarDatos(self, grosorTronco, longTronco, profundidad, decrementoGrosor, decrementoLong, ramificaciones, angulo,
                   esTronco):
        decrementoGrosor = sorted(decrementoGrosor)
        decrementoLong = sorted(decrementoLong)

        ramificaciones = sorted(ramificaciones)
        angulo= sorted(angulo)

        if grosorTronco>20:
            grosorTronco = 20
        elif grosorTronco<3:
            grosorTronco = 3
        if longTronco>85:
            longTronco = 85
        elif longTronco<70:
            longTronco = 70
        if profundidad>7:
            profundidad=7
        elif profundidad<3:
            profundidad=3
        if decrementoGrosor[0] < 1:
            decrementoGrosor[0] = 1
        elif decrementoGrosor[0] > 4:
            decrementoGrosor[0] = 4
        if decrementoGrosor[1] < 1:
            decrementoGrosor[1] = 1
        elif decrementoGrosor[1] > 4:
            decrementoGrosor[1] = 4
        if decrementoLong[0] < 1:
            decrementoLong[0] = 1
        elif decrementoLong[0] > 8:
            decrementoLong[0] = 8
        if decrementoLong[1] < 1:
            decrementoLong[1] = 1
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
        if angulo[0] < 15:
            angulo[0] = 15
        elif angulo[0] > 60:
            angulo[0] = 60
        if angulo[1] < 15:
            angulo[1] = 15
        elif angulo[1] > 60:
            angulo[1] = 60
        self.crearArbol(grosorTronco, longTronco, profundidad, decrementoGrosor, decrementoLong, ramificaciones, angulo,
                   esTronco)

    def crearArbol(self, grosorTronco, longTronco, profundidad, decrementoGrosor, decrementoLong, ramificaciones, angulo,
                   esTronco):
        if profundidad <= 0:
            return
        elif esTronco:
            self.maxTugo.pensize(grosorTronco * 8 // 3)
            self.maxTugo.forward(longTronco * 4 // 3)
            self.crearArbol((grosorTronco - randint(decrementoGrosor[0], decrementoGrosor[1])),
                       (longTronco - randint(decrementoLong[0], decrementoLong[1]))
                       , profundidad - 1, decrementoGrosor, decrementoLong, ramificaciones, angulo, False)
            return

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



#arbol(25, 95, 7, (3, 9), (10, 12), (2, 4), (0, 45), True)

"""
maxTugo.up()
maxTugo.forward(150)
maxTugo.down()
"""
"""
# arbol(grosorTronco, longTronco, profundidad, decrementoGrosor, decrementoLong, ramificaciones, angulo, esTronco)
#arbol(25, 95, 7, (3, 9), (10, 12), (4, 8), (0, 45), True)
def comparar(silueta, arbol):
    TAMANO = len(silueta)
    DIVISIONES = 25
    cantidadPixeles = TAMANO//DIVISIONES
    ponderado = 0

    for i in range(DIVISIONES-1):
        for j in range(DIVISIONES-1):
            fila = DIVISIONES * i
            col = DIVISIONES * j
            contador = 0
            nota = 0
            while contador <= cantidadPixeles:
                if silueta[fila][col] == arbol[fila][col] == 0:
                    nota += 5
                elif silueta[fila][col] == arbol[fila][col] == 255:
                    nota += 5
                elif silueta[fila][col] == 0 and arbol[fila][col] == 255:
                    nota -= 2
                else:
                    nota -= 2
                fila += 1
                col += 1
                contador += 1
            print(nota)
            nota *= 100
            nota /= 2880
            ponderado += nota

    ponderado /= DIVISIONES
    return ponderado
"""
"""
fileName = "imagenes\\imagen-1-1.png"
data = imagenAA.obtenerSilueta(fileName)
print(comparar(silueta2, data))
"""
"""
for row in data:
    print(' '.join('{:3}'.format(value) for value in row))
"""
"""
fileName = "imagenes\\siluetaNueva1"
#TurtleScreen.getcanvas().postscript(file=fileName + ".eps")

#img = Image.open(fileName + '.eps')
path3 = "C:\\I Semestre 2021\\AA\\Fractales_Proyecto2\\Siluetas\\silueta1.jpg"
img = Image.open(path3).convert("1")  # convert image to 8-bit grayscale
img = img.resize((600, 600))

img.save(fileName + '.png', 'png')
"""
# avance.generarImagen()
# image1 = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))
# draw = ImageDraw.Draw(image1)

