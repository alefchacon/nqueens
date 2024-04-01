import solucion
import numpy as np

def asignarAptitud(solucion: solucion.Solucion):
    solucion.aptitud = (  contar_ataques_horizontales(solucion.matriz) 
                        + contar_ataques_verticales(solucion.matriz)
                        + contar_ataques_diagonales(solucion.matriz))
    
def contar_ataques(numReinas):

    if numReinas == 0:
        return 0
    
    ataques = 0
    for index in range(1, 100):
        if index == numReinas:
            return ataques
        ataques += index

def contar_ataques_horizontales(matriz):
    totalAtaques = 0
    for fila in matriz:
        reinasEnFila = sum(fila)
        totalAtaques += contar_ataques(reinasEnFila) 
    return totalAtaques 

def contar_ataques_verticales(matriz):
    solucionRotada = list(zip(*matriz[::-1]))
    return(contar_ataques_horizontales(solucionRotada))

def contar_ataques_diagonales(matriz):
    diagonales = [matriz[::-1,:].diagonal(i) for i in range(-matriz.shape[0]+1,matriz.shape[1])]
    diagonales.extend(matriz.diagonal(i) for i in range(matriz.shape[1]-1,-matriz.shape[0],-1))
    diagonalesLista = [arreglo.tolist() for arreglo in diagonales]
    return(contar_ataques_horizontales(diagonalesLista))
