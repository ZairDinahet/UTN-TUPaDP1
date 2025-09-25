# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas = [7, 8, 5, 9, 10, 6, 4, 8, 9, 7]  # Lista fija de notas de 10 estudiantes

# Mostrar todas las notas
print("Notas:", notas)

# Calcular promedio sumando y dividiendo por la cantidad de elementos
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")

# Mostrar el máximo y el mínimo
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))


# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente.
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []
for i in range(5):  # Bucle de 5 repeticiones
    prod = input(f"Ingrese el producto {i+1}: ").strip()
    productos.append(prod)  # Agregamos a la lista

# Ordenar y mostrar los productos alfabéticamente
print("\nProductos ordenados:")
for p in sorted(productos, key=str.lower):  # sorted() no modifica la lista original
    print("-", p)

# Eliminar un producto específico si existe
eliminar = input("\nIngrese el producto a eliminar: ").strip()
if eliminar in productos:
    productos.remove(eliminar)
    print(f"'{eliminar}' eliminado.")
else:
    print("Ese producto no está en la lista.")

# Mostrar la lista final actualizada
print("\nLista final:")
for p in productos:
    print("-", p)


# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

# Generamos lista con 15 números al azar
numeros = [random.randint(1, 100) for _ in range(15)]

# Clasificamos pares e impares
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("\nNúmeros generados:", numeros)
print("Pares:", pares, f"(Cantidad: {len(pares)})")
print("Impares:", impares, f"(Cantidad: {len(impares)})")


# 4) Dada una lista con valores repetidos, crear una nueva lista sin elementos repetidos.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_duplicados = []

# Recorremos la lista y agregamos sólo si no está ya en la nueva
for d in datos:
    if d not in sin_duplicados:
        sin_duplicados.append(d)

print("\nLista original:", datos)
print("Sin duplicados:", sin_duplicados)


# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar si se quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final.

asistencia = ["Ana", "Juan", "Pedro", "Lucía", "María", "José", "Sofía", "Martín"]

print("\nAsistencia actual:")
for a in asistencia:
    print("-", a)

# Preguntamos al usuario la acción
opcion = input("\n¿Desea agregar (A) o eliminar (E) un estudiante?: ").strip().upper()

if opcion == "A":
    nuevo = input("Ingrese el nombre a agregar: ").strip()
    asistencia.append(nuevo)  # Agregar estudiante
elif opcion == "E":
    eliminar = input("Ingrese el nombre a eliminar: ").strip()
    if eliminar in asistencia:
        asistencia.remove(eliminar)  # Eliminar estudiante
    else:
        print("Ese estudiante no estaba en la lista.")

print("\nLista final:")
for a in asistencia:
    print("-", a)


# 6) Dada una lista con 7 números, rotar todos los elementos una posición a la derecha.
numeros = [1, 2, 3, 4, 5, 6, 7]
print("\nLista original:", numeros)

# pop() extrae el último y lo insertamos al inicio
ultimo = numeros.pop()
numeros.insert(0, ultimo)

print("Lista rotada:", numeros)


# 7) Crear una matriz de 7x2 con temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de mínimas y máximas.
# • Mostrar el día con mayor amplitud térmica.

temperaturas = [
    [10, 20],
    [12, 22],
    [8, 18],
    [15, 25],
    [11, 19],
    [9, 17],
    [13, 23]
]

# Separamos mínimas y máximas usando comprensión de listas
minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]

print("\nPromedio mínimas:", sum(minimas) / len(minimas))
print("Promedio máximas:", sum(maximas) / len(maximas))

# Amplitud = max - min, buscamos el día con mayor diferencia
amplitudes = [fila[1] - fila[0] for fila in temperaturas]
dia_max = amplitudes.index(max(amplitudes)) + 1
print("Día con mayor amplitud térmica:", dia_max)


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [
    [7, 8, 9],
    [6, 5, 7],
    [8, 9, 10],
    [5, 6, 5],
    [9, 8, 7]
]

print("\nNotas de estudiantes:")
for fila in notas:
    print(fila)

# Promedio por estudiante
for i, fila in enumerate(notas, start=1):
    print(f"Promedio estudiante {i}: {sum(fila)/len(fila):.2f}")

# Promedio por materia (recorremos columnas)
for j in range(3):
    suma = sum(notas[i][j] for i in range(5))
    print(f"Promedio materia {j+1}: {suma/5:.2f}")


# 9) Representar un tablero de Ta-Te-Ti como lista de listas (3x3).
# • Inicializar con guiones "-".
# • Permitir que los jugadores ingresen posiciones.
# • Mostrar el tablero después de cada jugada.

tablero = [["-"] * 3 for _ in range(3)]  # Creamos tablero 3x3

for turno in range(5):  # máximo 5 jugadas
    print("\nTablero actual:")
    for fila in tablero:
        print(" ".join(fila))  # Mostrar tablero como matriz

    jugador = "X" if turno % 2 == 0 else "O"  # Alternamos jugadores
    print(f"Turno de {jugador}")
    fila = int(input("Fila (0-2): "))
    col = int(input("Columna (0-2): "))

    # Validamos si la casilla está libre
    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador
    else:
        print("Esa casilla ya está ocupada.")

print("\nTablero final:")
for fila in tablero:
    print(" ".join(fila))


# 10) Registrar las ventas de 4 productos durante 7 días en una matriz 4x7.
# • Mostrar el total vendido por producto.
# • Mostrar el día con mayores ventas.
# • Indicar el producto más vendido.

ventas = [
    [10, 12, 11, 15, 14, 9, 13],
    [8, 9, 10, 12, 7, 11, 10],
    [14, 13, 15, 16, 12, 14, 13],
    [7, 8, 9, 6, 10, 11, 9]
]

print("\nVentas (productos x días):")
for fila in ventas:
    print(fila)

# Totales por producto (sumamos cada fila)
for i, fila in enumerate(ventas, start=1):
    print(f"Producto {i} total: {sum(fila)}")

# Totales por día (sumamos columnas)
totales_dia = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
dia_max = totales_dia.index(max(totales_dia)) + 1
print("Día con mayores ventas:", dia_max)

# Producto más vendido (el de mayor total)
totales_prod = [sum(fila) for fila in ventas]
prod_max = totales_prod.index(max(totales_prod)) + 1
print("Producto más vendido:", prod_max)
