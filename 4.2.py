from random import randint

def genArray():
    array = [0] * 10
    for i in range(0, len(array)):
        array[i] = randint(1, 10)
    return array

def printArray(array):
    for i in range(0, len(array)):
        print(array[i], end=' ')
    print('\n')

def removeDuplicates(array):
    print(array)
    l = len(array)
    r = array[:]
    i = 0
    while i < l:
        j = i + 1
        while j < l:
            #print(i, ':', r[i], '-', j, ':', r[j] )
            if r[i] == r[j]:
                for k in range(j, l - 1):
                    r[k] = r[k + 1]
                r[l - 1] = 0
                j = i + 1 #fix consecutive repeated numbers
                print(r)
            if r[i] == 0 and r[j] == 0:
                break
            j += 1
        i = i + 1
    return r

array = [4, 9, 3, 5, 3, 3, 10, 10, 5, 2] 
array = genArray()
printArray(array)
array = removeDuplicates(array)
printArray(array)