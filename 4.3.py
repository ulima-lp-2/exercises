arregloNoOrdenado = [1,2,4,1,2,4,5,10,23,10]
arregloOrdenadoMayorAMenor = [10,9,8,7,6,5,4,3,2,1]
arregloOrdenadoMenorAMayor = [1,2,3,4,5,6,7,8,9,10]

def isSorted(array):
    l = len(array)
    sortAsc = True
    sortDesc = True
    for i in range(0, l - 1):
        if array[i] > array[i + 1]:
            sortAsc = False
        elif array[i] < array[i + 1]:
            sortDesc = False
        if not(sortAsc or sortDesc):
            return False
    return True

print(isSorted(arregloNoOrdenado))
print(isSorted(arregloOrdenadoMayorAMenor))
print(isSorted(arregloOrdenadoMenorAMayor))
