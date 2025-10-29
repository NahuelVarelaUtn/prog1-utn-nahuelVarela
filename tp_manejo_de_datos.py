"""1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 
2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
formato: 
Producto: Lapicera | Precio: $120.5 | Cantidad: 30 
3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
cantidad) y lo agregue al archivo sin borrar el contenido existente. 
4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
una lista llamada productos, donde cada elemento sea un diccionario con claves: 
nombre, precio, cantidad. 

5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
no existe, mostrar un mensaje de error. 
6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
productos actualizados desde la lista. """


with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,550.0,15\n")
    archivo.write("Goma,75.0,40\n")

print("Archivo 'productos.txt' creado correctamente.\n")


productos = []  

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",") 
        nombre = datos[0]
        precio = float(datos[1])
        cantidad = int(datos[2])

        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })

print("\n--- Agregar nuevo producto ---")
nuevo_nombre = input("Nombre del producto: ").strip()
nuevo_precio = float(input("Precio: ").strip())
nueva_cantidad = int(input("Cantidad: ").strip())

productos.append({
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nueva_cantidad
})

print("\n--- Buscar producto ---")
buscado = input("Ingrese el nombre del producto a buscar: ").strip()

encontrado = False
for prod in productos:
    if prod["nombre"].lower() == buscado.lower():
        print(f"\n Producto encontrado:")
        print(f"Nombre: {prod['nombre']}")
        print(f"Precio: ${prod['precio']}")
        print(f"Cantidad: {prod['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\n Producto no encontrado.")


with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo 'productos.txt' actualizado correctamente.")
