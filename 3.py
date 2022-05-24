# Tema 3 Ejercicio 1
def tema3Ejercicio1():
    n = 6
    A = [1, 3 ,9, 10, 25, -6]
    B = [-2, 81, 4, 0, -1, 3]
    salidaT3E1 = [0, 0 ,0, 0, 0, 0]
    for i in range(0, n):
        salidaT3E1[i] = A[i] + B[n - 1 - i]
        
    print("Tema 3, ejercicio 1:", salidaT3E1)
    
# Tema 3 Ejercicio 2
def tema3Ejercicio2():
    M = [[23, 12, 9, 14],
         [-2, -71, 12, 5],
         [97, 11, -91, 0]]
    N = [[0, 192, -96, -3],
         [18, 1, 56, 5],
         [7, 90, -9, 3]]
    salidaT3E2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    cantFilas = len(M)
    cantColumnas = len(M[0])
    for i in range(0, cantFilas):
        for j in range(0, cantColumnas):
            salidaT3E2[i][j] = M[i][j] - N[i][j]
            
    print("Tema 3, ejercicio 2:", salidaT3E2)

# Tema 3 Ejercicio 3
def tema3Ejercicio3():
    #n = 8
    #arreglo =  [1, 2, 3, 4, 5, 6, 7, 8]
    n = 11
    arreglo =  [9, 2, 4, 6, 1, 2, 5, 3, 19, 10, 22]
    tempIzq = 0
    tempDer = n - 1
    tempValor = 0
    while (True):
        while (arreglo[tempIzq] % 2 != 0 and tempIzq < tempDer):
            tempIzq = tempIzq + 1
        while (arreglo[tempDer] % 2 == 0 and tempIzq < tempDer):
            tempDer = tempDer - 1
        if (tempIzq < tempDer):
            tempValor = arreglo[tempIzq]
            arreglo[tempIzq] = arreglo[tempDer]
            arreglo[tempDer] = tempValor
        else:
            break
        
    print("Tema 3, ejercicio 3:", arreglo)

def tema3Ejercicio3b():
    arreglo =  [9, 2, 4, 6, 1, 2, 5, 3, 19, 10, 22]
    #arreglo =  [1, 2, 3, 4, 5, 6, 7, 8]
    n = len(arreglo)
    p = 0
    q = len(arreglo) - 1
    even = 0
    odd = 0
    while p < n and q >= 0:
        if arreglo[p] % 2 != 0:
            p = p + 1
            even = None
        else:
            even = arreglo[p]
        if arreglo[q] % 2 == 0:
            q = q - 1
            odd = None
        else:
            odd = arreglo[q]
        if even != None and odd != None:
            arreglo[p] = odd
            arreglo[q] = even
            p = p + 1
            q = q - 1
        if p >= q:
            break    
    print("Tema 3, ejercicio 3:", arreglo)

# Tema 3 Ejercicio 4
def tema3Ejercicio4():
    #n = 6
    #arreglo =  [19, 12, 13, 11, 20, 14]
    n = 12
    arreglo = [10, 17, 9, 2, 20, 12, 6, 1, 23, 19, 12, 10]
    variacion = 0
    inicioCaida = 0
    finCaida = 0
    variacionTemp = 0
    inicioCaidaTemp = 0
    finCaidaTemp = 0
    for i in range(0, n):
        if (arreglo[i] > arreglo[inicioCaidaTemp]):
            inicioCaidaTemp = i
            finCaidaTemp = i
        elif (arreglo[i] < arreglo[finCaidaTemp]):
            finCaidaTemp = i
        variacionTemp = arreglo[inicioCaidaTemp] - arreglo[finCaidaTemp]
        if (variacionTemp > variacion):
            variacion = variacionTemp
            inicioCaida = inicioCaidaTemp + 1
            finCaida = finCaidaTemp + 1
    print("Tema 3, ejercicio 4: Intervalo con mayor caida = [",inicioCaida,",",finCaida,"];"," variacion = ", variacion)

#Ejecucion
tema3Ejercicio1()
tema3Ejercicio2()
tema3Ejercicio3()
tema3Ejercicio3b()
tema3Ejercicio4()
