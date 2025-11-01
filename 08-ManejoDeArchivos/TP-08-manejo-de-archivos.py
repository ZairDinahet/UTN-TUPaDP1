"""
2) Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
"""

with open('./unidad_8/productos.txt', 'r') as file:
    for line in file:
        producto, precio, cantidad = line.strip().split(',')
        print(f'Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}')




"""
3)Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.
"""

with open('./unidad_8/productos.txt', 'a') as file:
    producto = input('Ingrese el nombre del producto: ')
    precio = input('Ingrese el precio del producto: ')
    cantidad = input('Ingrese la cantidad del producto: ')
    file.write(f'{producto},{precio},{cantidad}\n')





"""
4) Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.
"""

productos = []

with open('./unidad_8/productos.txt', 'r') as file:
    for line in file:
        producto, precio, cantidad = line.strip().split(',')
        productos.append({'nombre': producto, 'precio': precio, 'cantidad': cantidad})

print(productos)



"""
5) Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.
"""

def leer_productos():
    productos = []
    with open('./unidad_8/productos.txt', 'r') as file:
        for line in file:
            producto, precio, cantidad = line.strip().split(',')
            productos.append({'nombre': producto, 'precio': precio, 'cantidad': cantidad})
    return productos

def buscar_producto(productos, nombre_producto):
    for producto in productos:
        if producto['nombre'].lower() == nombre_producto.lower():
            return producto
    return None


productos = leer_productos()
nombre_producto = input('Ingrese el nombre del producto: ')
producto = buscar_producto(productos, nombre_producto)

if producto:
    print(producto)
else:
    print('El producto no existe')




"""
6) Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.
"""

def leer_productos():
    productos = []
    with open('productos.txt', 'r') as file:
        for line in file:
            producto, precio, cantidad = line.strip().split(',')
            productos.append({'nombre': producto, 'precio': precio, 'cantidad': cantidad})
    return productos

def buscar_producto(productos, nombre_producto):
    for producto in productos:
        if producto['nombre'].lower() == nombre_producto.lower():
            return producto
    return None

def guardar_productos(productos):
    with open('productos.txt', 'w') as file:
        for producto in productos:
            file.write(f'{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n')

def agregar_producto(productos):
    nombre = input('Ingrese el nombre del producto: ')
    precio = input('Ingrese el precio del producto: ')
    cantidad = input('Ingrese la cantidad del producto: ')
    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    return productos

productos = leer_productos()
print(productos)

producto = buscar_producto(productos, 'Lapicera')
print(producto)

producto = agregar_producto(productos)
guardar_productos(productos)