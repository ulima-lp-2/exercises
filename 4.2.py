from random import randint

def genArray():
    array = [0] * 10
    for i in range(0, len(array)):
        array[i] = randint(1, 10)
    return array

def printArray(array):
    for i in range(0, len(array)):
        print(array[i], end='\t')
    print('\n')

def removeDuplicates(array):
    l = len(array)
    r = array[:]
    for i in range(0, l):
        for j in range(i + 1, l):
            print(i, j, r[i], r[j])
            if r[i] == r[j]:
                for k in range(j + 1, l):
                    r[k - 1] = r[k]
                r[l - 1] = 0
    return r

array = genArray()
printArray(array)
array = removeDuplicates(array)
printArray(array)