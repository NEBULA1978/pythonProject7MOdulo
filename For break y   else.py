for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'es igual a', x, '*', n/x)
            break
        else:
            #dige el bucle sin encontrar un factor
            print(n, 'es un numero primo')

for num in range(2, 10) :
    if num % 2 == 0:
        print("Encontre un numero par", num)
        continue

    print("Encontre un numero", num)

mi_lista = ['Juan', 'Antonia', 'Pedro', 'Herminio']
for nombre in mi_lista:
    print(nombre)