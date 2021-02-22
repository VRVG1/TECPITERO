#Puro pendejo revisa este codigo
#EL RETURN ESTA EN COMENTARIO PARA QUE LO CAMBIES PADRE XDDDD

def LOOK(secuencia,inicial,tam):
#INICIA CHAMBA*-----------------------------------------------------
    print('\nLOOK**************************************\n')
    izq = []
    der = []
    cActual = []
    tEspera = []
    desp = []
    aux = 0

    for i in range(tam):
        if secuencia[i]<inicial:
            izq.append(secuencia[i])
        else:
            der.append(secuencia[i])
        pass

    izq.sort()
    izq.reverse()
    der.sort()

    cActual.append(inicial)
    tEspera.append(0)

    for i in range(len(izq)):
        cActual.append(izq[i])
        desp.append(cActual[i]-izq[i])
        tEspera.append(tEspera[i]+desp[i])
        pass

    for i in range(len(der)):
        cActual.append(der[i])
        desp.append(der[i]-cActual[i+len(izq)])
        tEspera.append(tEspera[i+len(izq)]+desp[i+len(izq)])
        pass

    cActual.pop()
    tEspera.pop()

    #print('CILINDRO ACTUAL: ',cActual)
    #print('CILINDRO SOLICITADO: ',secuencia)
    #print('TIEMPO DE ESPERA: ',tEspera)
    #print('DESPLAZAMIENTO: ',desp)
    return [cActual, secuencia, tEspera, desp]

def CSCAN(secuencia,inicial,tam):
#INICIA CHAMBA*-----------------------------------------------------
    print('\nC-SCAN**************************************\n')
    izq = []
    der = []
    cActual = []
    tEspera = []
    desp = []

    for i in range(tam):
        if secuencia[i]<inicial:
            izq.append(secuencia[i])
        else:
            der.append(secuencia[i])
        pass

    izq.append(0)
    izq.sort()
    izq.reverse()
    der.append(199)
    der.sort()
    der.reverse()
    aux = []
    aux = izq + der

    cActual.append(inicial)
    tEspera.append(0)

    for i in range(len(izq)):
        cActual.append(izq[i])
        desp.append(cActual[i]-izq[i])
        tEspera.append(tEspera[i]+desp[i])
        pass

    for i in range(len(der)):
        cActual.append(der[i])
        desp.append(abs(cActual[i+len(izq)]-der[i]))
        tEspera.append(tEspera[i+len(izq)]+desp[i+len(izq)])
        pass

    cActual.pop()
    tEspera.pop()

    #print('CILINDRO ACTUAL: ',cActual)
    #print('CILINDRO SOLICITADO: ',aux)
    #print('TIEMPO DE ESPERA: ',tEspera)
    #print('DESPLAZAMIENTO: ',desp)
    return [cActual, aux, tEspera, desp]


def datos():
    global secuencia
    secuencia = []
    global inicial
    inicial = 0
    flag = True
    while flag==True:
        print("Ingrese el tamano de su secuencia: ")
        global tam
        tam = 0
        try:
            tam=int(input('- '))
            flag=False
        except ValueError:
            print('Solo se aceptan numeros enteros')
    pass
    flag=True

    print('Ingrese su secuencia: ')
    cont = 0

    while cont<tam:
        num = 0
        try:
            num=int(input('- '))
            secuencia.append(num)
            cont = cont+1
        except ValueError:
            print('Solo se aceptan numeros enteros')
    pass

    while flag==True:
        print('Ingrese el valor inicial: ')
        try:
            inicial=int(input('- '))
            flag=False
        except ValueError:
            print('Solo se aceptan numeros enteros')
    pass

#datos()
#LOOK(secuencia,inicial,tam)
#CSCAN(secuencia,inicial,tam)

#DOSCIENTAS POSICIONES MAX EN TAM
#INICIAL LA MISMA RESTRICCION
