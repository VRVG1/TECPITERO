def fcfs(array, inicial):
    cActual = [inicial]
    cSolicitado = []
    tiempo = [0]
    desplazamiento = []
    for i in range(len(array)):
        cSolicitado.append(array[i])
        desplazamiento.append(abs(cActual[i] - cSolicitado[i]))
        if i < len(array) - 1:
            cActual.append(array[i])
            tiempo.append(tiempo[i] + desplazamiento[i])
    return [cActual, cSolicitado, tiempo, desplazamiento]   
