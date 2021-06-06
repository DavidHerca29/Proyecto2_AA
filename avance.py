import tkinter
from random import randint, sample, random

from PIL import Image
import UI as ui
import imagenAA
from Arbol import Arbol


def fitness(listaIndividuos):
    respuestas = []
    notaMayor = 0
    ponderado = 0
    for i in gui.matrizGlobal[-1]:
        evaluar(i)

    cont = 1
    indice = 0
    for i in gui.matrizGlobal[-1]:
        ponderado += i.nota
        if i.nota > notaMayor:
            notaMayor = i.nota
            indice = cont
        cont += 1

    respuestas.append(round((ponderado / 10), 4))
    respuestas.append(notaMayor)
    respuestas.append(indice)
    return respuestas


def evaluar(arbol):
    filename = imagenAA.pathFitness + str(arbol.generacion) + "-" + str(arbol.numIndividuo) + ".png"
    matrizArbol = imagenAA.obtenerSilueta(filename)
    matrizSilueta = gui.silueta2  # AQUI SE CAMBIA LA MATRIZ QUE SE VA A USAR DE SILUETA
    # matrizSilueta = ui.silueta2
    # LOGICA DEL FITNESSS
    arbol.setNota(comparar(matrizSilueta, matrizArbol))


def comparar(silueta, arbol):
    TAMANO = len(silueta)
    DIVISIONES = 25
    cantidadPixeles = TAMANO // DIVISIONES
    ponderado = 0

    for i in range(DIVISIONES - 1):
        for j in range(DIVISIONES - 1):
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
                    nota -= 3
                else:
                    nota -= 3
                fila += 1
                col += 1
                contador += 1
            #print(nota)
            nota *= 100
            nota /= 2880
            ponderado += nota

    ponderado /= DIVISIONES
    return ponderado


def generarImagen(numGen, numIndividuo):
    fileName = "imagenes\\imagen-" + str(numGen) + "-" + str(numIndividuo)
    gui.TurtleScreen.getcanvas().postscript(file=fileName + ".eps")
    img = Image.open(fileName + '.eps')
    img.save(fileName + '.png', 'png')
    gui.iniciarPantalla()


def poblacionInicial():
    ramificaciones = (3, 6)
    angle = (15, 60)
    profundidad = (3, 7)  # 10
    grosorTronco = (3, 20)
    longitudTronco = (70, 85)
    decrementoLongitud = (1, 8)
    decrementoAncho = (1, 4)
    i = 0
    arrayArbol = []
    while i < 10:
        madre = 0
        padre = 0
        pgrosorTronco = randint(grosorTronco[0], grosorTronco[1])
        pprofundidad = randint(profundidad[0], profundidad[1])
        plongTronco = randint(longitudTronco[0], longitudTronco[1])
        pdecAncho = sorted(
            (randint(decrementoAncho[0], decrementoAncho[1]), randint(decrementoAncho[0], decrementoAncho[1])))
        pdeclong = sorted((randint(decrementoLongitud[0], decrementoLongitud[1]),
                           randint(decrementoLongitud[0], decrementoLongitud[1])))
        pramificaciones = sorted(
            (randint(ramificaciones[0], ramificaciones[1]), randint(ramificaciones[0], ramificaciones[1])))
        pangulo = sorted((randint(angle[0], angle[1]), randint(angle[0], angle[1])))
        pgeneracion = 1
        pnumIndividuo = i+1
        arbol = Arbol(0, 0, pgrosorTronco, pprofundidad, plongTronco, pdecAncho, pdeclong,
                      pramificaciones, pangulo, pgeneracion, pnumIndividuo)
        arrayArbol.append(arbol)
        gui.validarDatos(pgrosorTronco, plongTronco, pprofundidad, pdecAncho, pdeclong, pramificaciones, pangulo, True)
        #gui.TurtleScreen.update()
        #gui.ventana.mainloop()
        # funcion guardar imagen(0,i+1)
        generarImagen(1, i + 1)
        #gui.TurtleScreen.update()
        #gui.ventana.mainloop()
        i += 1
    gui.matrizGlobal.append(arrayArbol)  # cambiar nombre matriz global
    gui.totalGeneraciones.append(len(gui.matrizGlobal))
    return arrayArbol


def sacarHijos(primerInd, segundoInd):
    particion = randint(1, len(primerInd) - 2)
    primerPart1 = primerInd[:particion]
    segundaPart1 = primerInd[particion:]
    primerPart2 = segundoInd[:particion]
    segundaPart2 = segundoInd[particion:]
    primerHijo = primerPart1 + segundaPart2
    segundoHijo = primerPart2 + segundaPart1
    return (primerHijo, segundoHijo)


# aG es el array de la ultima generación

def sacarCromosomas(aG, aparicionesLista):
    grosorTronco = 4
    profundidad = 3
    largotronco = 7
    decrementoAncho = 1, 3
    decrementoLongitud = 1, 3
    ramificaciones = 3, 4  #
    angulos = 4, 7
    contador = sorted(list(set(aparicionesLista)))
    for i in contador:
        cromosomas = bin(aG[i].grosorTronco)[2:].zfill(5) + bin(aG[i].profundidad)[2:].zfill(3) + bin(
            aG[i].longitudTronco)[2:].zfill(7) + \
                     bin(aG[i].decrementoGrosor[0])[2:].zfill(3) + bin(aG[i].decrementoGrosor[1])[2:].zfill(3) + \
                     bin(aG[i].decrementoLongitud[0])[2:].zfill(4) + bin(aG[i].decrementoLongitud[1])[2:].zfill(4) + \
                     bin(aG[i].ramificaciones[0])[2:].zfill(3) + bin(aG[i].ramificaciones[1])[2:].zfill(3) + \
                     bin(aG[i].angulo[0])[2:].zfill(6) + bin(aG[i].angulo[1])[2:].zfill(6)
        aG[i].cromosomas = cromosomas


def seleccion(aG):  # arraygeneracion):
    i = 0
    valores = []
    for i in aG:
        valores.append(i.nota)
    normalizado = [round((float(i) / sum(valores) * 100)) for i in valores]

    suma = 0
    for i in range(10):
        temp = normalizado[i]
        normalizado[i] = normalizado[i]+suma
        suma += temp

    lista = range(0, 100)
    listaRandom = sample(lista, k=10)
    listaApariciones = []
    for i in listaRandom:
        for j in range(10):
            if j == 0:
                if i <= normalizado[0]:
                    listaApariciones.append(j)
                    break
            else:
                if normalizado[j - 1] < i <= normalizado[j]:
                    listaApariciones.append(j)
                    break
    return listaApariciones


def cruce(aG, listaApariciones):
    sacarCromosomas(aG, listaApariciones)
    hijos = []
    i = 0
    while i < 10:
        primerInd = aG[listaApariciones[i]].cromosomas
        segundoInd = aG[listaApariciones[i + 1]].cromosomas
        nuevosHijos = sacarHijos(primerInd, segundoInd)
        hijos.append(nuevosHijos[0])
        hijos.append(nuevosHijos[1])
        i += 2
    return hijos


def mutacion(hijos):
    prob = randint(0, 100)
    if prob < 15:
        indiceMutacion = randint(8, 14)
        largo = len(hijos[0]) - 1
        matriz = []
        for i in hijos:
            matriz.append(list(i))
        print(matriz)
        i=0
        while i < indiceMutacion:
            x = randint(0, 9)
            y = randint(0, largo)
            matriz[x][y] = "1" if hijos[x][y] == "0" else "0"
            i+=1
        nuevosHijos = []
        for i in matriz:
            listToStr = ''.join(map(str,i))
            nuevosHijos.append(listToStr)
        return nuevosHijos
    return hijos


def nuevaGeneracion(generacion, hijos, listaApariciones):
    print("nuevaGeneracion")
    arrayArbol = []
    j = 0
    k = 1
    cont = 1
    for i in hijos:
        grosor = int(i[0:5], 2)
        profundidad = int(i[5:8], 2)
        longitudTronco = int(i[8:15], 2)
        decrementoAncho = (int(i[15:18], 2), int(i[18:21], 2))
        decrementoLongitud = (int(i[21:25], 2), int(i[25:29], 2))
        ramificaciones = (int(i[29:32], 2), int(i[32:35], 2))
        angulo = (int(i[35:41], 2), int(i[41:], 2))
        arbol = Arbol(generacion[listaApariciones[j]], generacion[listaApariciones[j + 1]], grosor, profundidad,
                      longitudTronco, decrementoAncho, decrementoLongitud, ramificaciones, angulo,
                      len(gui.matrizGlobal) + 1,
                      cont)
        # (self, ppadre, pmadre, pgosorTronco, pprofundidad, plongTronco, pdecrementoGrosor, pdeclong, pramificaciones, pangulo, pgeneracion, pnumIndividuo):
        gui.validarDatos(grosor, longitudTronco, profundidad, decrementoAncho, decrementoLongitud, ramificaciones, angulo, True)

        #gui.TurtleScreen.update()
        #gui.ventana.mainloop()
        # guardar imagenes(len(matrizGlobal+1),cont)
        generarImagen(len(gui.matrizGlobal) + 1, cont)
        #ggui.TurtleScreen.update()
        #ggui.ventana.mainloop()
        arrayArbol.append(arbol)
        if k == 2:
            j += 2
            k = 0
        k += 1
        cont += 1
    gui.matrizGlobal.append(arrayArbol)  # cambiar nombre matriz global
    gui.totalGeneraciones.append(len(gui.matrizGlobal)+1)
    return arrayArbol

def main():
    print("inicia")
    temp = poblacionInicial()  # se guardan las imagenes de la primera generacion
    # generarImagen(gui.matrizGlobal[-1], )
    ponderadoGenActual = 5
    ponderadoGenAnterior = 0
    mayorActual = 0
    indiceMayor = 0
    print("se inicia")
    while abs(ponderadoGenActual - ponderadoGenAnterior) > 1 and mayorActual < 66:
        print("New")
        ponderadoGenAnterior = ponderadoGenActual
        notas = fitness(temp)  # devuelve un array del ponderado de toda la generacion y del individuo con nota mas baja
        ponderadoGenActual = notas[0]
        mayorActual = notas[1]
        indiceMayor = notas[2]
        print(indiceMayor)
        print(mayorActual)
        print(ponderadoGenAnterior)
        print(ponderadoGenActual)
        listaApariciones = seleccion(temp)
        hijos = cruce(temp, listaApariciones)
        hijosFinales = mutacion(hijos)
        temp = nuevaGeneracion(temp, hijosFinales, listaApariciones)
    print("FINSIH")
    print(indiceMayor)
    print(mayorActual)
    print(ponderadoGenAnterior)
    print(ponderadoGenActual)
    gui.actualizarGeneraciones()


if __name__ == '__main__':
    # _________ INICIALZACION DE TKINTER
    ventanaPrincipal = tkinter.Tk()
    gui = ui.Interfaz(ventanaPrincipal)
    #main()
    gui.crearArbol(15, 85, 6, (3, 9), (10, 12), (4, 8), (15, 45), True)
    ventanaPrincipal.mainloop()