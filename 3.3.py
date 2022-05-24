arreglo =  [9, 2, 4, 6, 1, 2, 5, 3, 19, 10, 22]

n = len(arreglo)
p = 0
q = len(arreglo) - 1
even = 0 #par
odd = 0 #impar

while p < n and q >= 0:
    if arreglo[p] % 2 != 0: #impar
        p = p + 1
        even = None
    else:
        even = arreglo[p]
    if arreglo[q] % 2 == 0: #par
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

print(arreglo)