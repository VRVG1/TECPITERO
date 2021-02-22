import areli
    
def scan(bit, array, inicial):
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
    for i in entry[n:len(entry)-1]:
      cActual.append(i)
      cSolicitado.append(entry[entry.index(i)+1])
      desplazamiento.append(abs(cActual[n]-cSolicitado[n]))  
      tiempo.append(tiempo[n-1]+desplazamiento[n-1])  
      n = n + 1
  return [cActual, cSolicitado, tiempo, desplazamiento]   


	
	
A = [37,0,14,65,67,98,122,124,183]

scan(0,A,53)




