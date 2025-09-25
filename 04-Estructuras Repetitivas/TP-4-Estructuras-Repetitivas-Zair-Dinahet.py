# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# Defino el rango empezando desde 0 hasta 101 con paso 1 para que este pueda empezar desde 0 hasta llegar al 100
for i in range(0, 101, 1):
    # Imprimo la linea
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# Solicito el número entero
numeroEntero = int(input('Ingrese un número entero: '))

# Guardo el número solicitado para no perderlo
numeroOriginal = numeroEntero

# Inicializo un contador para los dígitos
contador = 0

# Creo un bucle que se ejecute siempre y cuando el número entero sea mayor que 0, de esta forma voy a poder contar los dígitos
while numeroEntero > 0:    
    # Voy dividiendo el número en 10 de forma entera y sobreescribo el valor del numero para ir evaluando el siguiente digito
    numeroEntero = numeroEntero // 10

    # Aumento mi contador en 1 para indicar que hay un dígito más 
    contador += 1

# Si el contador es igual a 0 entonces por descarte hay un solo digito
if contador == 0:
    contador = 1

print(f'El número {numeroOriginal} tiene {contador} dígitos.')


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# Solicito dos valores enteros al usuario
valor1 = int(input("Ingrese el primer valor entero: "))
valor2 = int(input("Ingrese el segundo valor entero: "))

# Me aseguro de que el primer valor sea menor que el segundo
if valor1 > valor2:
    # Intercambio los valores si es necesario
    valor1, valor2 = valor2, valor1  

# Inicializo la variable para la suma
suma = 0

# Sumo los números entre los dos valores
for i in range(valor1 + 1, valor2):
    suma += i

print(f"La suma de los números entre {valor1} y {valor2} es {suma}.")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# Inicializo el total acumulado
totalAcumulado = 0

# Creo un bucle para que se puedan ingresar los números que se quieran hasta que se ingrese el 0
while True:
    numero = int(input("Ingresa un número entero (0 para detener): "))
    
    # Si el número que ingresan es 0, termino el bucle con un break
    if numero == 0:
        break
    
    # Sumo el número ingresado al total
    totalAcumulado += numero

# Imprimo el total acumulado
print(f"La suma total acumulada es: {totalAcumulado}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

# Genero un número aleatorio entre 0 y 9
numeroSecreto = random.randint(0, 9)

# Inicializo el contador de intentos
intentos = 0

# Creo un bucle para que se pueda iniciar el juego, el mismo se detendra cuando se acierte el numero secreto
while True:
    # Solicito al usuario un número
    numeroUsuario = int(input("Adivina el número entre 0 y 9: "))
    
    # Incremento el contador de intentos
    intentos += 1
    
    # Verificar si adivino el número secreto
    if numeroUsuario == numeroSecreto:
        print(f"¡Felicidades, sos un/a genio/a! Adivinaste el número en {intentos} intentos.")
        break
    elif numeroUsuario < numeroSecreto:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# Creo una bucle empezando en 100 y va restando 2 en cada iteración, esta para cuando se llegue a 0
for i in range(100, -1, -2):  
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# Solicito un número entero positivo al usuario
numero = int(input("Ingresa un número entero positivo: "))

# PLUS: Me aseguro de que el número sea positivo
if numero < 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    # Inicializo la suma en 0
    suma = 0

    # Creo un bucle para sumar todos los números entre 0 y el número ingresado
    for i in range(numero + 1):
        # Acumulamo el número en la suma
        suma += i  

    print(f"La suma de todos los números entre 0 y {numero} es: {suma}")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Inicializo los contadores para los pares, impares, positivos y negativos
pares = 0
impares = 0
positivos = 0
negativos = 0

# Creo un bucle para solicitar los 100 números
for i in range(100):
    numero = int(input(f"Ingrese el número (Esta por el #{i+1}): "))

    # Cuento los  pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Cuento los positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Imprimo los resultados
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# Inicializo la suma total en 0
sumaTotal = 0

# Creo un bucle para ingresar los 100 números
for i in range(100):
    numero = int(input(f"Ingrese el número (Esta por el #{i+1}): "))

    # Como en veces reiteradas acumulo el número en la suma total
    sumaTotal += numero

# Calculo la media o promedio
promedio = sumaTotal / 100

# Imprimo el promedio o media
print(f"\nEl promedio de los 100 números es: {promedio}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Solicito número al usuario
numero = int(input("Ingresa un número entero: "))

# Convierto el número a positivo si es negativo e identifico si es negativo
esNegativo = numero < 0
numero = abs(numero)

# Inicializo la variable que almacenará el número invertido
invertido = 0

# Creo un bucle para invertir los dígitos
while numero != 0:
    # Obtengo el último dígito del número
    digito = numero % 10

    # Multiplico el número invertido actual por 10, esto con fin de hacerle espacio a la derecha al nuevo digito, y luego le sumo el nuevo dígito extraído
    invertido = invertido * 10 + digito

    # Elimino el último dígito del número original
    numero = numero // 10

# Regreso el signo si era negativo
if esNegativo:
    invertido *= -1

# Imprimo el número invertido
print(f"Número invertido: {invertido}")

