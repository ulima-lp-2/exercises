#Tema 1, Ejercicio 1
renta = int(input("Ingresar renta: "))
print(renta)
pago = 0
if (renta < 10000):
    pago = renta*0.05
elif (renta < 20000):
    pago = renta*0.15
elif (renta < 35000):
    pago = renta*0.20
elif (renta < 60000):
    pago = renta*0.30
else:
    pago = renta*0.45
print("Tema 1, ejercicio 1:", pago)
    
#Tema 1, Ejercicio 2
numero = int(input("Ingresar numero: "))
factorial = 1
for i in range(2,numero+1):
    factorial = factorial * i
print("Tema 1, ejercicio 2:",factorial)

#Tema 1, Ejercicio 3
palabra = input("Ingresar palabra: ")
longitud = len(palabra)
print("Tema 1, ejercicio 3: ")
for i in range(0, longitud):
    print(palabra[longitud - 1 - i])
    
#Tema 1, Ejercicio 4
palabra = input("Ingresar palabra: ")
letra = input("Ingresar letra: ")
longitud = len(palabra)
print("Tema 1, ejercicio 4: ")
for i in range(0, longitud):
    if (palabra[i] == letra):
        print("Indice",i,": se encontro la letra")
        break
    else:
        print("Indice",i,": no se encontro la letra")
#Tema 1, Ejercicio 5
monto = int(input("Ingresar monto: "))
suma = 0
while (monto != 0):
    if (monto > 0):
        suma = suma + monto
    monto = int(input("Ingresar monto: "))
if (suma > 1000):
    suma = suma * 0.9
print("Tema 1, ejercicio 5: ", suma)
