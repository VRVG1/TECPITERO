import areli

def c_look(array, inicial):
  cActual = [inicial]
  cSolicitado = []
  desplazamiento = []
  tiempo = [0]
  array = areli.quickSort(array)
  izq, der = areli.puntoMedio(array, inicial)
  puntero = array.index(der)
  aux = 0
  for i in range(len(array)):
    if aux != 0 :
      cActual.append(cSolicitado[aux - 1])
      tiempo.append(tiempo[aux - 1] + desplazamiento[aux - 1])
    cSolicitado.append(array[puntero])
    desplazamiento.append(abs(cActual[aux] - cSolicitado[aux]))
    puntero = puntero + 1
    if puntero >= len(array):
      puntero = 0
    aux = aux + 1
  return [cActual,cSolicitado,tiempo,desplazamiento]




