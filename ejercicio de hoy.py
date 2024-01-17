"""
Pedir una cantidad indeterminada de números entre el -30 y el 150 hasta que el usuario ingrese el número 0.

PASO 1
Almacenar los números en una lista

PASO 2
Calcular y mostrar los resultados de lo siguiente
- Promedio de los números pares
- Cantidad de múltiplos de 7
- Cantidad de divisores de 4
- El mayor de los números negativos
- El mayor de los numeros positivos
- Promedio de los múltiplos de 5
- Cantidad de números negativos
- Promedio de todos los números
- Promedio de los números impares

"""

LIM_INF = -30
LIM_SUP = 150
DIVISOR_DE_4 = 4
suma_pares = 0
cont_pares = 0
cantidad_multiplo_de_7 = 0
cantidad_divisor_de_4 = 0
mayor_numero_negativo = None
mayor_numero_positivo = None
suma_multiplos_de_5 = 0
cont_multiplos_de_5 = 0
cont_negativos = 0
suma_numeros = 0
cont_numeros = 0
suma_impares = 0
cont_impares = 0
numero = 1
contador = 0
lista_numeros = []


while numero != 0:
    numero = -33
    while not LIM_INF <= numero <= LIM_SUP:
        numero = int(input(f"Introduzca el {contador+1}° número: "))
    contador += 1

    if numero != 0:
        lista_numeros.append(numero)

for i in range(len(lista_numeros)):
    # si trabajo con más de una condicion: ej: si es primo y si es mayor o menor. primero agarro la condicion primo y luego si es mayor o menor
    if lista_numeros[i] < 0:
        if mayor_numero_negativo is None:
            mayor_numero_negativo = lista_numeros[i]
        elif lista_numeros[i] > mayor_numero_negativo:
            mayor_numero_negativo = lista_numeros[i]
    if lista_numeros[i] > 0:
        if mayor_numero_positivo is None:
            mayor_numero_positivo = lista_numeros[i]
        elif lista_numeros[i] > mayor_numero_positivo:
            mayor_numero_positivo = lista_numeros[i]
    if lista_numeros[i] % 2 == 0:
        suma_pares += lista_numeros[i]
        cont_pares += 1
    if lista_numeros[i] % 7 == 0:
        cantidad_multiplo_de_7 += 1
    if DIVISOR_DE_4 % lista_numeros[i] == 0:
        cantidad_divisor_de_4 += 1
    if lista_numeros[i] % 5 == 0:
        suma_multiplos_de_5 += lista_numeros[i]
        cont_multiplos_de_5 += 1
    if lista_numeros[i] < 0:
        cont_negativos += 1
    if lista_numeros[i] % 2 != 0:
        suma_impares += lista_numeros[i]
        cont_impares += 1
    suma_numeros += numero
    cont_numeros += 1

if cont_pares > 0:
    print(f"El promedio de los números pares es de: {suma_pares/cont_pares}")
else:
    print("No se han ingresado números pares")
if cantidad_multiplo_de_7 > 0:
    print(f"La cantidad de los números multiplos de 7 es de: {cantidad_multiplo_de_7}")
else:
    print("No se han ingresado números multiplos de 7")
if cantidad_divisor_de_4 > 0:
    print(f"La cantidad de los divisores de {DIVISOR_DE_4} es de: {cantidad_divisor_de_4}")
else:
    print(f"No se han ingresado números que sean divisibles por {DIVISOR_DE_4}")
if cont_multiplos_de_5 > 0:
    print(f"El promedio de los números multiplos de 5 es de: {suma_multiplos_de_5/cont_multiplos_de_5}")
else:
    print(f"No se han ingresado números multiplos de 5")
if cont_negativos > 0:
    print(f"existen {cont_negativos} números negativos")
if mayor_numero_negativo is None:
    print("No se ha ingresado ningún número negativo")
else:
    print(f"El mayor número negativo es el: {mayor_numero_negativo}")
if mayor_numero_positivo is None:
    print("No se ha ingresado ningún número positivo")
else:
    print(f"El mayor número positivo es el: {mayor_numero_positivo}")
if cont_impares > 0:
    print(f"El promedio de los números impares es de: {suma_impares/cont_impares}")
print(f" el promedio de todos los números es de: {suma_numeros/cont_numeros}")
