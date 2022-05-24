from random import randint

# Tema 4 Ejercicio 1
def crearArregloAzar():
    arreglo = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0, 10):
        arreglo[i] = randint(1, 10)
    return arreglo

def imprimirOcurrencias(arr):
    longitud = len(arr)
    for i in range(0, longitud):
        print(arr[i])

def tema4Ejercicio1():
    arreglo = crearArregloAzar()
    imprimirOcurrencias(arreglo)

# Tema 4 Ejercicio 2
def eliminarRepetidos(arr):
    longitud = len(arr)
    for i in range(0, longitud):
        for j in range(i+1, longitud):
            if (arr[i] == arr[j]):
                for k in range(j+1, longitud):
                    arr[k-1] = arr[k]
                arr[longitud-1] = 0
    return arr

def tema4Ejercicio2():
    arreglo = crearArregloAzar()
    arregloSinDuplicados = eliminarRepetidos(arreglo.copy())
    print(arreglo, arregloSinDuplicados)
    
# Tema 4 Ejercicio 3
def estaOrdenado(arr):
    longitud = len(arr)
    ordenadoMenorAMayor = True
    ordenadoMayorAMenor = True
    for i in range(1, longitud):
        if (arr[i-1] > arr[i]):
            ordenadoMenorAMayor = False
        elif (arr[i-1] < arr[i]):
            ordenadoMayorAMenor = False
        if (not(ordenadoMenorAMayor or ordenadoMayorAMenor)):
            return False
    return True

def tema4Ejercicio3():
    arregloNoOrdenado = [1,2,4,1,2,4,5,10,23,10]
    arregloOrdenadoMayorAMenor = [10,9,8,7,6,5,4,3,2,1]
    arregloOrdenadoMenorAMayor = [1,2,3,4,5,6,7,8,9,10]
    print(estaOrdenado(arregloNoOrdenado), estaOrdenado(arregloOrdenadoMayorAMenor), estaOrdenado(arregloOrdenadoMenorAMayor))

#Ejecucion
tema4Ejercicio1()
tema4Ejercicio2()
tema4Ejercicio3()
