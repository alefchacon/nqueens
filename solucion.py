import random
import numpy as np


class Solucion:
  def __init__(self, matriz, coordenadas):
    self.aptitud      = 0
    self.matriz       = matriz
    self.coordenadas  = coordenadas
  
  def setCoordenadas(self, coordenadas):
     self.limpiarMatriz()
     self.coordenadas = random.sample(self.posiblesCoordenadas, 8)
     for coordenada in coordenadas:
        self.matriz[coordenada[0]][coordenada[1]] = 1
  
  def generarMatrizCorrecta(self):
    return np.array([
      [0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0],
      [1, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1],
      [0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0] ,
      [0, 0, 1, 0, 0, 0, 0, 0]
    ])
  

  
  def limpiarMatriz(self):
    self.matriz = np.array([
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                  ])

  def imprimir(self):
      print(self.matriz)
      print("APTITUD: "+self.aptitud.__str__())