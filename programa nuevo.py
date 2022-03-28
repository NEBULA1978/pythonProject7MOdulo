import time

t = 10

while True:
    print(t)
    if t == 0:
        break
    t -= 1
    time.sleep(1)
print('Hecho')

import math

radio = float(input("radio -> "))


print('Hecho')
area= math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"El area es: {area:.2f}")



print(f"La longitud de la circunferencia es: {longitud:.2f}")

nombre = "Alejandro"

edad = 22

print("Hola {} tienes {} años".format(nombre,edad))

print(f"Hola {nombre} tienes {edad} años")
print(f"Hola {nombre} tienes {edad} años")

nombre = input("Digite su nombre: ")

print(f"Hola {nombre}")

numero = input("Digite su numero: ")
print(f"El numero es {numero}")

import math

radio = float(input("radio -> "))

area = math.pi * radio ** 2
longitud = 2 * math.pi * radio

print(f"El area es: {area:.2f}")
print(f"La longitud de la circunferencia es: {longitud:.2f}")

nombre = "Alejandro"

edad = 22

print("Hola {} tienes {} años".format(nombre, edad))

print(f"Hola {nombre} tienes {edad} años")
print(f"Hola {nombre} tienes {edad} años")

nombre = input("Digite su nombre: ")

print(f"Hola {nombre}")

numero = float(input("Digite su numero: "))
print(f"El numero es {numero}")

numero = float(input("Digite su numero: "))
print(f"El numero es {numero + 1}")

nombres = input("nombres")

print(f"Hola {nombres}")
