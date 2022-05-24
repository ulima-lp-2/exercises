#Tema 2, Ejercicio 1
# Subject data = [weight_kg, height_m]
subject1 = [80, 1.62]
subject2 = [69, 1.53]
subject3 = [80, 1.66]
subject4 = [80, 1.79]

def calcularBMI(subject):
    return int(subject[0] / subject[1]**2)
def imprimirBMI(bmi_subject, nombre):
    print("bmi {} = {}".format(nombre, bmi_subject))
def tema2Ejercicio1():
    print("Tema 2, ejercicio 1:")
    bmi_subject1 = calcularBMI(subject1)
    imprimirBMI(bmi_subject1, 'subject1')
    
    bmi_subject2 = calcularBMI(subject2)
    imprimirBMI(bmi_subject2, 'subject2')
    
    bmi_subject3 = calcularBMI(subject3)
    imprimirBMI(bmi_subject3, 'subject3')
    
    bmi_subject4 = calcularBMI(subject4)
    imprimirBMI(bmi_subject4, 'subject4')

tema2Ejercicio1()

#Tema 2, Ejercicio 2
import random

def getRandom():
    r = random.randint(1,9)
    # print(r)
    return r

def main():
    numero = getRandom()
    print("Tema 2, ejercicio 2:",numero)

main()

#Tema 2, Ejercicio 3
import time

def imprimirSegundos(segundoInicial):
    print('\r' + str(segundoInicial), end='', flush=True)
    segundoInicial = segundoInicial + 1
    time.sleep(1)
    if (segundoInicial <= 10):
        imprimirSegundos(segundoInicial)

seconds = 0
print("Tema 2, ejercicio 3:")
imprimirSegundos(seconds)
print(".")

#Tema 2, Ejercicio 4
def sumarCincoNumeros(cantSumados):
    if (cantSumados == 5):
        return 0
    else:
        return getRandom() + sumarCincoNumeros(cantSumados+1)
suma = sumarCincoNumeros(0)
print("Tema 2, ejercicio 4:", suma)
