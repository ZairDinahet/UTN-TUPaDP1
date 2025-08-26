
# __________________________________________________________________________________________

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# __________________________________________________________________________________________

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.


nombre = input("Por favor, ingrese su nombre: ")
print(f"Hola {nombre}!")

# __________________________________________________________________________________________

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Por favor, ingrese su nombre: ")

apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar_de_residencia = input("Por favor, ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")

# __________________________________________________________________________________________

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

import math

radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))

area_circulo = math.pi * (radio_circulo)**2

perimetro_circulo = 2 * math.pi * radio_circulo

print(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.")

# __________________________________________________________________________________________

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

cantidad_segundos = float(input("Por favor, ingrese la cantidad de segundos a convertir: "))

cantidad_horas = round(cantidad_segundos / 3600, 2)

print(f"El equivalente a {cantidad_segundos} segundos son {cantidad_horas} horas.")


# __________________________________________________________________________________________

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

n = int(input("Por favor, ingrese un número entero: "))

numero_por_0 = n * 0
numero_por_1 = n * 1
numero_por_2 = n * 2
numero_por_3 = n * 3
numero_por_4 = n * 4
numero_por_5 = n * 5
numero_por_6 = n * 6
numero_por_7 = n * 7
numero_por_8 = n * 8
numero_por_9 = n * 9
numero_por_10 = n * 10


print(f"""
  {n} x 0 = {numero_por_0}
  {n} x 1 = {numero_por_1}
  {n} x 2 = {numero_por_2}
  {n} x 3 = {numero_por_3}
  {n} x 4 = {numero_por_4}
  {n} x 5 = {numero_por_5}
  {n} x 6 = {numero_por_6}
  {n} x 7 = {numero_por_7}
  {n} x 8 = {numero_por_8}
  {n} x 9 = {numero_por_9}
  {n} x 10 = {numero_por_10}
      """)

# __________________________________________________________________________________________

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero_a = float(input("Por favor, ingrese un número distinto de 0: "))
numero_b = float(input("Por favor, ingrese otro número distinto de 0: "))

suma_a_b = numero_a + numero_b
division_a_b = round(numero_a / numero_b, 2)
multiplicacion_a_b = numero_a * numero_b
resta_a_b = numero_a - numero_b

print(f"""
  Resultado de la suma: {suma_a_b}
  Resultado de la división: {division_a_b}
  Resultado de la multiplicación: {multiplicacion_a_b}
  Resultado de la resta: {resta_a_b}
      """)

# __________________________________________________________________________________________

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:

peso = float(input("Por favor, ingrese su peso en kilogramos: "))
altura = float(input("Por favor, ingrese su altura en metros: "))

imc = round(peso / altura**2, 2)

print(f"Su IMC es de: {imc}.")

# __________________________________________________________________________________________


# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:


temperatura_celsius = float(input("Por favor, una temperatura en °C: "))

temperatura_fahrenheit = round((9/5)*temperatura_celsius+32, 2)

print(f"{temperatura_celsius} °C equivalen a {temperatura_fahrenheit} °F.")


# __________________________________________________________________________________________

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.


numero_a = float(input("Por favor, ingrese el primer número: "))
numero_b = float(input("Por favor, ingrese el segundo número: "))
numero_c = float(input("Por favor, ingrese el tercer número: "))

suma_a_b_c = numero_a + numero_b + numero_c

promedio_a_b_c = round(suma_a_b_c/3, 2)

print(f"El promedio de los números ingresados es {promedio_a_b_c}.")