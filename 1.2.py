numero = int(input("numero:"))

# for i = 0 ; i < 5 ; i++:
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(factorial)