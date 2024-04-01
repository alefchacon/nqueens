from solucion import Solucion

class Resultado:
  def __init__(self, 
               exitoso: bool, 
               numEvaluaciones: int, 
               solucion: Solucion):
    self.exitoso            = exitoso
    self.numEvaluaciones    = numEvaluaciones
    self.solucion           = solucion
    self.aptitudes          = []