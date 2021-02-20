import areli
    
def scan(bit, array, inicial):
  array.append(inicial)
  array = areli.quickSort(array)
  n = 0
  cActual = []
  cSolicitado = []
  tiempo = []
  desplazamiento = []
  if (bit == 0):
    for i in range(array.index(inicial),-1,-1):
      if (i != 0):
        cActual.append(array[i])
        cSolicitado.append(array[i-1])
        desplazamiento.append(cActual[n]-cSolicitado[n])  
        if (len(tiempo) == 0):
          tiempo.append(0)
        else:
          tiempo.append(tiempo[n-1]+desplazamiento[n-1])
      else:	
        cActual.append(array[i])
        cSolicitado.append(array[array.index(inicial)+1])
        desplazamiento.append(abs(cActual[n]-cSolicitado[n]))
        if (len(tiempo) == 0):
          tiempo.append(0)
        else:
          tiempo.append(tiempo[n-1]+desplazamiento[n-1])	
      n = n + 1
    for i in array[n:len(array)-1]:
      cActual.append(i)
      cSolicitado.append(array[array.index(i)+1])  
      desplazamiento.append(abs(cActual[n]-cSolicitado[n]))  
      tiempo.append(tiempo[n-1]+desplazamiento[n-1])  
      n = n + 1
  else:
    n = 0
    for i in array[n:len(array)-1]:
      cActual.append(i)
      cSolicitado.append(array[array.index(i)+1])  
      desplazamiento.append(abs(cActual[n]-cSolicitado[n]))  
      tiempo.append(tiempo[n-1]+desplazamiento[n-1])  
      n = n + 1
  return [cActual, cSolicitado, tiempo, desplazamiento]   


	
	
A = [37,0,14,65,67,98,122,124,183]

scan(0,A,53)




