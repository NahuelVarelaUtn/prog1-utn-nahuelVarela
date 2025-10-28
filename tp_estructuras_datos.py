#1) Dado el diccionario precios_frutas 
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
#1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800 

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios. 

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe. 

agenda_telefonica = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico del contacto: ")
    agenda_telefonica[nombre] = numero

nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
if nombre_consulta in agenda_telefonica:
    print(f"El número de {nombre_consulta} es: {agenda_telefonica[nombre_consulta]}")
else:
    print(f"El contacto {nombre_consulta} no existe en la agenda.")

#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra. 

frase = input("Ingrese una frase: ")

palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("Cantidad de veces que aparece cada palabra:", contador_palabras)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno. 

alumnos_notas = {}
for i in range(3):
    nombre_alumno = input("Ingrese el nombre del alumno: ")
    notas = []
    for n in range(3):
        nota = float(input(f"Ingrese la nota {n+1} de {nombre_alumno}: "))
        notas.append(nota)
    alumnos_notas[nombre_alumno] = tuple(notas)

for alumno, notas in alumnos_notas.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es: {promedio}")


#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {20, 35, 40, 55, 70}
parcial_2 = {30, 40, 55, 60, 80}

aprobados_ambos = parcial_1.intersection(parcial_2) # usé esta funcion para obtener los elementos que estan en ambos sets
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)

aprobados_solo_uno = parcial_1.symmetric_difference(parcial_2) # usé esta funcion para obtener los elementos que estan en un set o en otro pero no en ambos
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)

aprobados_al_menos_uno = parcial_1.union(parcial_2)
print("Estudiantes que aprobaron al menos un parcial:", aprobados_al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe. 


stock_productos = {}

while True:
    opcion = input("Ingrese 'consultar' para consultar stock, 'agregar' para agregar stock, 'nuevo' para agregar un nuevo producto, o 'salir' para terminar: ").lower()
    if opcion == 'consultar':
        producto = input("Ingrese el nombre del producto a consultar: ")
        if producto in stock_productos:
            print(f"El stock de {producto} es: {stock_productos[producto]}")
        else:
            print(f"El producto {producto} no existe en el stock.")
    elif opcion == 'agregar':
        producto = input("Ingrese el nombre del producto al que desea agregar stock: ")
        if producto in stock_productos:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            stock_productos[producto] += cantidad
            print(f"Nuevo stock de {producto} es: {stock_productos[producto]}")
        else:
            print(f"El producto {producto} no existe en el stock.")
    elif opcion == 'nuevo':
        producto = input("Ingrese el nombre del nuevo producto: ")
        cantidad = int(input("Ingrese la cantidad inicial de stock: "))
        stock_productos[producto] = cantidad
        print(f"Producto {producto} agregado con un stock de {cantidad}.")
    elif opcion == 'salir':
        break
    else:
        print("Opción no válida. Intente nuevamente.")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 

agenda = {}
bandera = True

while bandera == True:
    opcion = input("Ingrese 'agregar' para agregar un evento, 'consultar' para consultar un evento, o 'salir' para terminar: ").lower()
    if opcion == 'agregar':
        dia = input("Ingrese el día del evento : ")
        hora = input("Ingrese la hora del evento : ")
        evento = input("Ingrese la descripción del evento: ")
        agenda[(dia, hora)] = evento
        print(f"Evento agregado para el {dia} a las {hora}.")
    elif opcion == 'consultar':
        dia = input("Ingrese el día del evento a consultar : ")
        hora = input("Ingrese la hora del evento a consultar : ")
        clave = (dia, hora)
        if clave in agenda:
            print(f"Evento en {dia} a las {hora}: {agenda[clave]}")
        else:
            print(f"No hay eventos programados para el {dia} a las {hora}.")
    elif opcion == 'salir':
        bandera = False
    else:
        print("Opción no válida. Intente nuevamente.")


#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}

invertido = {capital: pais for pais, capital in paises.items()}

print(invertido)


        
    
    
