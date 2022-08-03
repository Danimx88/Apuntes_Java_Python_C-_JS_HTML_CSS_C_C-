import random
cities = ["Nuevo leon", "Chihuahua", "Baja California","Oaxaca", "Estado de México", "CDMX", "Puebla",
          "Sinaloa", "San Luis Potosi", "Coahuila"]
for calle in cities:
    #print(calle)
    print("Estado de " + calle)
    print(calle[0])
n = 1
x = int(input("ingrese valor de bucle: "))
p = int(input("ingrese valor de fin de bucle: "))
while n < x+1:

    print(f"valor = {n}")
    n+=p
