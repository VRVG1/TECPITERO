import areli

def scan(bit, array, inicial):
  h = 0
  entry = array.copy()
  entry.append(inicial)
  entry = areli.quickSort(entry)
  n = 0
  cActual = []
  cSolicitado = []
  tiempo = []
  desplazamiento = []
  if (bit == 0):
    for i in range(entry.index(inicial),-1,-1):
      if (i != 0):
        cActual.append(entry[i])
        cSolicitado.append(entry[i-1])
        desplazamiento.append(cActual[n]-cSolicitado[n])
        if (len(tiempo) == 0):
          tiempo.append(0)
        else:
          tiempo.append(tiempo[n-1]+desplazamiento[n-1])
      else:
        cActual.append(entry[i])
        cSolicitado.append(entry[entry.index(inicial)+1])
        desplazamiento.append(abs(cActual[n]-cSolicitado[n]))
        if (len(tiempo) == 0):
          tiempo.append(0)
        else:
          tiempo.append(tiempo[n-1]+desplazamiento[n-1])
      n = n + 1
    for i in entry[n:len(entry)-1]:
      cActual.append(i)
      cSolicitado.append(entry[entry.index(i)+1])
      desplazamiento.append(abs(cActual[n]-cSolicitado[n]))
      tiempo.append(tiempo[n-1]+desplazamiento[n-1])
      n = n + 1
  else:
    n = 0
    try:
      if (entry.index(199)):
        h = h + 1
    except:
        entry.append(199)
    c = entry.index(inicial)
    for i in entry[entry.index(inicial):len(entry)-1]:
      if( c < len(entry)-1):
        cActual.append(i)
        cSolicitado.append(entry[entry.index(i)+1])
        desplazamiento.append(abs(cActual[n]-cSolicitado[n]))
        if (len(tiempo) == 0):
          tiempo.append(0)
        else:
          tiempo.append(tiempo[n-1]+desplazamiento[n-1])
      c = c + 1
      n = n + 1
    cActual.append(199)
    cSolicitado.append(entry[entry.index(inicial)-1])
    desplazamiento.append(abs(cActual[n]-cSolicitado[n]))
    tiempo.append(tiempo[n-1]+desplazamiento[n-1])
    n = n + 1

    for i in range((entry.index(inicial))-1,-1,-1):
      if(i != 0):
        cActual.append(entry[i])
        cSolicitado.append(entry[i-1])
        desplazamiento.append(cActual[n]-cSolicitado[n])
        tiempo.append(tiempo[n-1]+desplazamiento[n-1])
        n = n + 1


  return [cActual, cSolicitado, tiempo, desplazamiento]
