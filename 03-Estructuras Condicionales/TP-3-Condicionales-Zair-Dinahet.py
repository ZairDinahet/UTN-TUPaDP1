# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Solicito la edad
edad = int(input('Ingrese su edad: '))

# Pregunto si la edad es mayor a 18
if (edad >= 18):

    # Muestro por pantalla que es mayor de edad
    print(f'Es mayor de edad.')


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”. 

# Solicito la nota al usuario
nota = float(input('Ingrese su nota: '))

# Pregunto si la nota es mayor o igual a 6
if (nota >= 6):

    # Muestro por pantalla que está aprobado
    print(f'Aprobado')
else:

    # Muestro por pantalla que está aprobado
    print(f'Desaprobado')

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 

# Solicito un número par
numero = int(input('Ingrese un número par: '))

# Verifico que sea un número par con el operador módulo
if (numero % 2 == 0):

    # Si el residuo es 0, entonces efectivamente ingresó un número par
    print(f'Ha ingresado un número par')
else:

    # De caso contrario le pido que ingrese un número par
    print(f'Por favor, ingrese un número par')

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

# Solicito la edad del usuario
edad = int(input('Ingrese su edad: '))

# Verifico la edad del usuario para cada categoria
if (edad < 12):
    print(f'Niño/a')
elif (18 > edad >= 12):
    print(f'Adolescente')
elif (30 > edad >= 18):
    print(f'Adulto/a joven')
elif (edad >= 30):
    print(f'Adulto/a')

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

# Solicito una contraseña
password = input('Ingrese su contraseña:' )

# Verifico si la contraseña está dentro del rango
if (14 >= len(password) >= 8):
    print(f'Ha ingresado una contraseña correcta')
else:
    print(f'Por favor, ingrese una contraseña de entre 8 y 14 caracteres')

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
# siguiente: 
# from statistics import mode, median, mean 
# mi_lista = [1,2,5,5,3] 
# mean(mi_lista) 
# En la documentación oficial se puede encontrar más información sobre este paquete: 
# https://docs.python.org/es/3.8/library/statistics.html.  
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
# mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
# la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
# Definir la lista numeros_aleatorios de la siguiente forma: 
# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
# forma aleatoria.

# Importo las librerias necesarias
import random
from statistics import mode, median, mean

# Defino la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculo la media, la mediana y la moda de la lista
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Para tener por seguro los resultados luego imprimo la lista y cada resultado
print(f'Lista de números: {numeros_aleatorios}')
print(f'Media: {media}')
print(f'Mediana: {mediana}')
print(f'Moda: {moda}')

# Determino el sesgo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla.

# Solicito una frase o palabra
frase = input('Ingrese una frase: ')

# Tomo el último caracter de la frase y lo paso a minúscula para hacer el condicional más corto
ultimoCaracter = frase[-1].lower()

# Pregunto si el último caracter es vocal
if ((ultimoCaracter == 'a') or (ultimoCaracter == 'e') or (ultimoCaracter == 'i') or (ultimoCaracter == 'o') or (ultimoCaracter == 'u')):

    # Imprimo la frase más un signo de exlamación al final
    print(f'{frase + '!'}')
else:

    # Imprimo la frase normal
    print(f'{frase}')

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Solicito el nombre al usuario
nombre = input("Ingrese su nombre: ")

# Solicito la opción al usuario
print("Elija una opción:")
print("1. Mostrar el nombre en MAYÚSCULAS")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra en mayúscula")

opcion = input("Ingrese 1, 2 o 3: ")

# Transformo el nombre según la opción elegida
if opcion == "1":
    resultado = nombre.upper()
elif opcion == "2":
    resultado = nombre.lower()
elif opcion == "3":
    resultado = nombre.title()


# Muestro el resultado
print("Resultado:", resultado)

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

# Solicito la magnitud del terremoto
magnitud = int(input('Ingrese la magnitud del terremoto: '))

# Clasifico el terremoto según la escala De Richter
if (magnitud < 3):
    print("Muy leve (imperceptible)")
elif (4 > magnitud >= 3):
    print("Leve (ligeramente perceptible)")
elif (5 > magnitud >= 4):
    print("Moderado ((sentido por personas, pero generalmente no causa daños)")
elif (6 > magnitud >= 5):
    print("Fuerte (puede causar daños en estructuras débiles)")
elif (7 > magnitud >= 6):
    print("Muy fuerte (puede causar daños significativos)")
elif (magnitud >= 7):
    print("Extremo ((puede causar graves daños a gran escala)")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano. 

# Solicito el hemisferio, el mes y el dia al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ")
mes = input("¿Qué mes es? (por ejemplo: marzo): ")
dia = int(input("¿Qué día del mes es? (número): "))

# Paso todo a minúsculas por si el usuario escribe con mayúsculas
hemisferio = hemisferio.upper()
mes = mes.lower()

# Determino la estación según mes, día y hemisferio
if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia <= 20):
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"

elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia <= 20):
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"

elif (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 20):
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"

elif (mes == "septiembre" and dia >= 21) or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre" and dia <= 20):
    if hemisferio == "N":
        estacion = "Otoño"
    else:
        estacion = "Primavera"

# Muestro el resultado
print("Estás en la estación:", estacion)
