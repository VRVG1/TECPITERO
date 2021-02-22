import areli


def SSTF(input_array, inicial):
    entry = areli.quickSort(input_array)    # entry es el arreglo de datos ordenados de menor a mayor
    pointer = inicial

    actual = []         # Columna : Cilindro actual
    solicitado = []     # Columna : Cilindro solicitado / siguiente
    tiempo_espera = []  # Columna : Cilindro tiempo de espera
    desplazamiento = [] # Columna : Desplazamiento

    for i in range(len(entry)):
        actual.append(pointer)

        if(i == 0):
            tiempo_espera.append(0)
        else:
            tiempo_espera.append(tiempo_espera[i-1] + desplazamiento[i-1])

        # Retorna los valores a la izquierda y derecha del valor puntero
        izq, der = areli.puntoMedio(entry, pointer)
        # Retorna el cilindro siguiente y el desplazamiento que va a realizar
        next_cil, mov = shortest_pointer(pointer, izq, der)

        solicitado.append(next_cil)
        desplazamiento.append(mov)

        # Se elimina del arreglo el cilindro que ya ha sido procesado
        entry.pop(entry.index(next_cil))

        pointer = next_cil
        pass
    return [actual, solicitado, tiempo_espera, desplazamiento]
    pass

def shortest_pointer(pointer, izq, der):
    # Se valida si el izquierdo es nulo, si lo es, se verifica que derecho no sea nulo,
    # si derecho es nulo se retornan valores nulos
    if(izq == None):
        if(der != None):
            return der, (der - pointer)
        else:
            return None, None
    # se valida si el derecho es nulo, si lo es, se verifica que izquierdo no sea nulo,
    # si izquierdo es nulo se retornan valores nulos
    if(der == None):
        if(izq != None):
            return izq, (pointer - izq)
        else:
            return None, None

    # Si ambos no son nulos se procede a restar
    dif_point_izq = pointer - izq   # El izquierdo es menor que el puntero, por ello,
                                    # para obtener un valor positivo se puso a la derecha el izquierdo
    dif_point_der = der - pointer   # El puntero es menor al derecho, por ello,
                                    # para obtener un valor positivo se puso a la izquierda el puntero

    if(dif_point_izq < dif_point_der):
        return izq, dif_point_izq

    return der, dif_point_der
    pass

"""
arreglo = [98,183,37,122,14,124,65,67]
tableau = SSTF(arreglo,53)
print("Cilindro actual : \t\t", tableau[0])
print("Cilindro solicitado : \t\t", tableau[1])
print("Tiempo de espera : \t\t", tableau[2])
print("Desplazamiento : \t\t", tableau[3])
"""