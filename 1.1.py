renta = int(input("renta:"))
tasa = 0
'''
 Menos de 10000 5%
Entre 10000 y 20000 15%
Entre 20000 y 35000 20%
Entre 35000 y 60000 30%
Más de 60000 45%
'''
if renta < 10000:
   tasa = 0.1
elif renta < 20000:
   tasa = 0.15
elif renta < 35000:
   tasa = 0.2
elif renta < 60000:
   tasa = 0.3
else:
   tasa = 0.45
print("impuesto: ", tasa * renta)