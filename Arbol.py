

class Arbol:

    padre = 0
    madre = 0
    grosorTronco = 0
    profundidad = 0
    longitudTronco = 0
    anchoTronco = 0

    decrementoAncho = ()
    decrementoLongitud = ()
    Ramificaciones = ()
    angulo = ()
    generacion = 0
    numIndividuo = 0
    nota = 0
    def __init__(self, ppadre, pmadre, pgosorTronco, pprofundidad, plongTronco, panchoTronco, pdecAncho, pdeclong, pramificaciones, pangulo, pgeneracion, pnumIndividuo):
        self.decrementoAncho = pdecAncho
        self.decrementoLongitud = pdeclong
        self.padre = ppadre
        self.numIndividuo = pnumIndividuo
        self.profundidad = pprofundidad
        self.anchoTronco = panchoTronco
        self.angulo = pangulo
        self.grosorTronco = pgosorTronco
        self.generacion = pgeneracion
        self.longitudTronco = plongTronco
        self.madre = pmadre
        self.Ramificaciones = pramificaciones

    def setNota(self, pnota):
        self.nota = pnota