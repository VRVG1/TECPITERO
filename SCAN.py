def quickSort(array):
  menor = []
  igual = []
  mayor = []
  if len(array) > 1:
    pivote = array[0]
    for i in array:
      if i < pivote:
        menor.append(i)
      elif i == pivote:
        igual.append(i)
      else:
        mayor.append(i)
    return quickSort(menor)+igual+quickSort(mayor)
  else:
    return array
    
def scan(bit, array, inicial):
  array.append(inicial)
  
  array = quickSort(array)
  print(array)
  n = 0
  cActual = []
  cSolicitado = []
  tiempo = []
  dezplazamiento = []
  if (bit == 0):
    for i in range(array.index(inicial),-1,-1):
      if (i != 0):
        cActual.append(array[i])
        cSolicitado.append(array[i-1])
        dezplazamiento.append(cActual[n]-cSolicitado[n])  
        if (len(tiempo) == 0):
          tiempo.append(0)
        else:
          tiempo.append(tiempo[n-1]+dezplazamiento[n-1])
      else:	
        cActual.append(array[i])
        cSolicitado.append(array[array.index(inicial)+1])
        dezplazamiento.append(abs(cActual[n]-cSolicitado[n]))
        if (len(tiempo) == 0):
          tiempo.append(0)
        else:
          tiempo.append(tiempo[n-1]+dezplazamiento[n-1])	
      n = n + 1
    #array.remove(inicial)
    print(array)
    for i in array[n:len(array)-1]:
      print(i)
      cActual.append(i)
      cSolicitado.append(array[array.index(i)+1])  
      dezplazamiento.append(abs(cActual[n]-cSolicitado[n]))  
      tiempo.append(tiempo[n-1]+dezplazamiento[n-1])  
      n = n + 1
      #array.index(i)-1
  else:
    n = 0
    for i in array[n:len(array)-1]:
      print(i)
      cActual.append(i)
      cSolicitado.append(array[array.index(i)+1])  
      dezplazamiento.append(abs(cActual[n]-cSolicitado[n]))  
      tiempo.append(tiempo[n-1]+dezplazamiento[n-1])  
      n = n + 1

  print(cActual)
  print(cSolicitado)
  print(tiempo)
  print(dezplazamiento)

	
	
A = [37,0,14,65,67,98,122,124,183]

scan(0,A,53)




