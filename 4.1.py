from random import randint

def genArray():
    array = [0] * 10
    for i in range(0, len(array)):
        array[i] = randint(1, 10)
    return array

def printArray(array):
    for i in range(0, len(array)):
        print(array[i])


array = genArray()
printArray(array)