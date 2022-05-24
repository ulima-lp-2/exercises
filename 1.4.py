palabra = (input("palabra:"))
letra = (input("letra:"))

for i in range(0, len(palabra)):
    if (palabra[i] == letra):
        print("Indice",i,": se encontro la letra")
        break
    else:
        print("Indice",i,": no se encontro la letra")