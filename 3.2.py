M = [
    [23, 12, 9, 14],
    [-2, -71, 12, 5],
    [97, 11, -91, 0]
    ]
N = [
    [0, 192, -96, -3],
    [18, 1, 56, 5],
    [7, 90, -9, 3]
    ]
R = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] #[[0] * 4] * 3 # TODO
filas = len(M)
columnas = len(M[0])

for f in range(0, filas):
    for c in range(0, columnas):        
        R[f][c] = M[f][c] - N[f][c]
        print(f, c, R[f][c])
print(R)