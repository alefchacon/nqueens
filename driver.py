import n_queens
import numpy
import matplotlib.pyplot as plt

resultados = []
for index in range(0 , 30):
    print("EVALUACION " + (index+1).__str__())
    resultado = n_queens.nQueens()
    resultados.append(resultado)
    print("\n")

resultados.sort(key=lambda resultado: resultado.solucion.aptitud, reverse=True)

def getMejorResultado():
    mejores = []
    mejorAptitud = resultados[-1].solucion.aptitud
    for resultado in resultados:
        if resultado.solucion.aptitud == mejorAptitud:
            mejores.append(resultado)
    mejores.sort(key=lambda resultado: resultado.numEvaluaciones, reverse=True)
    return mejores.pop()

def getPeorResultado():
    peores = []
    peorAptitud = resultados[0].solucion.aptitud
    for resultado in resultados:
        if resultado.solucion.aptitud == peorAptitud:
            peores.append(resultado)
    peores.sort(key=lambda resultado: resultado.numEvaluaciones, reverse=True)
    return peores.pop()

mejorResultado = getMejorResultado()
peorResultado = getPeorResultado()

def imprimirResultado(mejor = True, resultado = None):
    tipo = "MEJOR" if mejor else "PEOR"
    print("\n" + tipo + " RESULTADO:")
    resultado.solucion.imprimir()
    print("numEvaluaciones: " + str(resultado.numEvaluaciones))



numResultadosExitosos = 0
numEvaluaciones = []
for resultado in resultados:
    if resultado.solucion.aptitud == 0:
        numEvaluaciones.append(resultado.numEvaluaciones)
        numResultadosExitosos = numResultadosExitosos + 1

print("RESULTADOS EXITOSOS: " + str(numResultadosExitosos))
imprimirResultado(True, mejorResultado)

print("MEDIA DE numEvaluaciones EN resultadosExitosos: " 
    + str(numpy.average(numEvaluaciones)))

numEvaluaciones.sort(reverse=True)

print("MEDIANA DE numEvaluaciones EN resultadosExitosos: " 
    + str(numpy.median(numEvaluaciones)))

print("DESVIACIÓN ESTÁNDAR DE numEvaluaciones EN resultadosExitosos: " 
    + str(numpy.std(numEvaluaciones)))


imprimirResultado(False, peorResultado)


plt.plot(peorResultado.aptitudes)
plt.show()


plt.plot(mejorResultado.aptitudes)
plt.show()
