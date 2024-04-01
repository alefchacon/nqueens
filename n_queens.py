import random
import numpy
import copy
import time
import matplotlib.pyplot as plt
from console_progressbar import ProgressBar

from itertools import product


from solucion import Solucion
import evaluador
from resultado import Resultado

aptitudesTotales = []

barraDeProgreso = ProgressBar(total=100,
                              length=30, 
                              fill='█', 
                              zfill='░')

# Inicio:
def nQueens():
    poblacion.clear()
    generarPoblacion()

    individuoMasApto = None


    numEvaluaciones = 0
    index = 0
    for index in range (0, 10000):
        #Ordenar por aptitud:
        poblacion.sort(key=lambda individuo: individuo.aptitud, reverse=False)

        seleccionar_padres()

        individuoMasApto = poblacion[0] 
        aptitudesTotales.append(individuoMasApto.aptitud)
        if individuoMasApto.aptitud == 0:
            break

        numEvaluaciones = numEvaluaciones + 1
        
        if ( (index / 100) % 10 == 0  ):
            barraDeProgreso.print_progress_bar(index/100)

    aptitudesTotales.sort(reverse=True)
    resultado = Resultado(individuoMasApto.aptitud == 0,
                            numEvaluaciones,
                            individuoMasApto)
    resultado.aptitudes = copy.deepcopy(aptitudesTotales)
    aptitudesTotales.clear()

    if individuoMasApto.aptitud != 0:
        barraDeProgreso.print_progress_bar(100)
    individuoMasApto.imprimir()
    print("Evaluaciones: " + resultado.numEvaluaciones.__str__())


    return resultado

def graficar():
    # use the plot function
    plt.plot(aptitudesTotales)

    plt.show()

def crearSolucionAleatoria(coordenadas):
    solucion = crearSolucionVacia()
    solucion.coordenadas = coordenadas
    for coordenada in solucion.coordenadas:
        solucion.matriz[coordenada[0]][coordenada[1]] = 1
    return solucion

def crearSolucionVacia():
    matriz = numpy.array([
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ])
    coordenadas = []
    return Solucion(matriz, coordenadas)

poblacion = []
def generarPoblacion():
    posiblesCoordenadas = []
    for coordenada in product([0, 1, 2, 3, 4, 5, 6, 7], repeat = 2):
        posiblesCoordenadas.append(coordenada)
    for indice in range(0, 100):

        solucion = crearSolucionAleatoria(random.sample(posiblesCoordenadas, 8))
        validar_solucion(solucion)
        evaluador.asignarAptitud(solucion)
        poblacion.append(solucion)

    poblacion.sort(key=lambda individuo: individuo.aptitud, reverse=False)


def seleccionar_padres():
    hijos = []
    for index in range(0, 10):

        hijo = None
        
        while(hijo is None):
            padresPotenciales = random.sample(poblacion, 5)

            # Se ordenan de mejor a peor, y se sacan los dos mejores
            padresPotenciales.sort(key=lambda padre: padre.aptitud, reverse=True)
            padre1 = padresPotenciales.pop(); 
            padre2 = padresPotenciales.pop(); 

            # cruzar() regresa None en caso de fallar
            hijo = cruzar(padre1, padre2)

        hijos.append(hijo)

    del poblacion[90:]
    poblacion.extend(hijos)

            
def cruzar(padre1, padre2):
    coordenadasUnicas = set()
    coordenadasAgrupadas = [*padre1.coordenadas, *padre2.coordenadas,]
    for coordenada in coordenadasAgrupadas:
        coordenadasUnicas.add(coordenada)

    # si no se obtuvieron al menos 8 coordenadas únicas, la cruza falla
    if len(coordenadasUnicas) < 8:
        return None

    coordenadasCruzadas = random.sample(list(coordenadasUnicas), 8)
    hijo = crearSolucionAleatoria(coordenadasCruzadas)

    mutar(hijo)

    validar_solucion(hijo)

    evaluador.asignarAptitud(hijo)
    return hijo


def validar_solucion(solucion):
    if solucion is None:
        return False
    if numpy.shape(solucion.matriz)[0] != 8:
        raise Exception("La matriz no tiene 8 renglones")
    if numpy.sum(solucion.matriz) != 8:
        raise Exception("La matriz no tiene 8 reinas")

    return True


def decidirOperacion():
    PROBABILIDAD_SUMA = 0.50 
    operacion = 1
    probabiliidadResta = random.random()
    if probabiliidadResta > PROBABILIDAD_SUMA:
        operacion = -1
    return operacion

operacionesPosibles = {
    2 :  1,
    1 : -1,
    0 :  0,
}
def mutarCoordenada(coordenada):
    puedeCrecer = 2 if coordenada < 7 else 0
    puedeEncoger = 1 if coordenada > 0 else 0 
    eleccion = puedeEncoger + puedeCrecer
    operacion = 0
    if (eleccion < 3) :
        operacion = operacionesPosibles[eleccion]
    else:
        decidirOperacion()
    return coordenada + operacion

def mutar(hijo: Solucion):

    PROBABILIDAD_MUTACION = 0.80 
    probabilidadDeNoMutar = random.random()

    if probabilidadDeNoMutar > PROBABILIDAD_MUTACION:
        return
    
    coordenadas = copy.copy(hijo.coordenadas)
    intentosDeMutar = 0
    INTENTOS_MAXIMOS = 10
    while intentosDeMutar != INTENTOS_MAXIMOS:

        indiceCoordenadasAMutar = random.choice(range(0, 7))
        coordenadasAMutar = coordenadas[indiceCoordenadasAMutar]

        filaMutante = mutarCoordenada(coordenadasAMutar[0])
        columnaMutante = mutarCoordenada(coordenadasAMutar[1])
        coordenadasMutantes = tuple([filaMutante, columnaMutante])

        if coordenadas.__contains__(coordenadasMutantes):
            intentosDeMutar += 1
            continue

        hijo.matriz[coordenadasAMutar[0]][coordenadasAMutar[1]] = 0
        hijo.matriz[filaMutante][columnaMutante] = 1

        coordenadas[indiceCoordenadasAMutar] = coordenadasMutantes
        break

#nQueens()