'''
Se tiene dos arreglos A y B, ambos de longitud n. 
Crear un algoritmo que calcule e imprima A + C; 
donde C posee los mismo valores de B pero en orden invertido.
	Caso de prueba:
		Entrada: n = 6; A = [1, 3 ,9, 10, 25, -6]; 
        B = [-2, 81, 4, 0, -1, 3] 
		Salida: [4, 2, 9, 14, 106, -8]
'''
A = [1, 3 ,9, 10, 25, -6]
B = [-2, 81, 4, 0, -1, 3]
#C = B invertido

n = len(A)

D = [0] * n
for i in range(0, n):
    # C = B invertido
    # D[i] = A + C
    c = B[n - 1 - i]
    D[i] = A[i] + c
    print(i, A[i], B[i], c)
print(D)

