from statistics import mode,median,mean
import random

#Ejercicios de condicionales

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad: int = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota :int = int(input("Introduce tu nota: "))
if nota >= 6 : 
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero: int = int(input("Ingresa un numero par : "))

if numero % 2 == 0 : 
    print("Has ingresado un numero par")
else:
    print("Por favor, ingresa un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad : int = int(input("Ingresa tu edad por favor: "))

if edad < 12 : 
    print("Eres un niño/a")
elif edad >= 12 and edad < 18 : 
    print("Eres un adolescente")
elif edad >= 18 and edad < 30 : 
    print("Eres un adulto/a joven")
elif edad >= 30 : 
    print("Eres un adulto/a")
else:
    print("Ingresa una edad válida")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña : str = input("Ingresa una contraseña de entre 8 y 14 caracteres : ") 

if len(contraseña) >=8 and len(contraseña) <=14 :
    print ("Tu contraseña cumple con los requisitos")
else:
    print("Por favor, ingresa una contraseña de entre 8 y 14 caracteres")


#6)La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

if media > mediana and mediana > moda :
    print("Sesgo positivo o a la derecha")  
elif media < mediana and mediana < moda :
    print("Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda :
    print("Sin sesgo")
else:
    print("No se pudo determinar el sesgo")


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

frase : str = input("Ingresa una frase o palabra: ")

if frase[-1].lower() in "aeiou" :
    frase += "!"
    print(frase)
else:
    print(frase)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

input_nombre : str = input("Ingresa tu nombre: ")
opcion : int = int(input("Ingresa 1 si quieres tu nombre en mayusculas, 2 si lo quieres en minusculas o 3 si lo quieres con la primera letra en mayuscula: "))

if opcion == 1 :
    print(input_nombre.upper())
elif opcion == 2 :
    print(input_nombre.lower())
elif opcion == 3 :
    print(input_nombre.title())
else:
    print("Opcion no valida")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

input_magnitud : float = float(input("Ingresa la magnitud del terremoto: "))

if input_magnitud < 3 :
    print("Muy leve (imperceptible)")
elif input_magnitud >= 3 and input_magnitud < 4 :
    print("Leve (ligeramente perceptible)")
elif input_magnitud >= 4 and input_magnitud < 5 :
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif input_magnitud >= 5 and input_magnitud < 6 :
    print("Fuerte (puede causar daños en estructuras débiles)")
elif input_magnitud >= 6 and input_magnitud < 7 :
    print("Muy Fuerte (puede causar daños significativos)")
elif input_magnitud >= 7 :
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Ingresa una magnitud válida")

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano

hemisferio : str = input("Ingresa en que hemisferio te encuentras (N/S): ").upper()
mes : int = int(input("Ingresa el mes en numero (1-12): "))
dia : int = int(input("Ingresa el dia (1-31): "))

if hemisferio == "N" :
    if (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
        print("Estas en primavera")
    elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
        print("Estas en verano")
    elif (mes == 9 and dia >= 21) or (mes > 9 and mes < 12) or (mes == 12 and dia <= 20):
        print("Estas en otoño")
    elif (mes == 12 and dia >= 21) or (mes < 3) or (mes == 3 and dia <= 20):
        print("Estas en invierno")
    else:
        print("Ingresa una fecha válida")
elif hemisferio == "S" :
    if (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
        print("Estas en otoño")
    elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
        print("Estas en invierno")
    elif (mes == 9 and dia >= 21) or (mes > 9 and mes < 12) or (mes == 12 and dia <= 20):
        print("Estas en primavera")
    elif (mes == 12 and dia >= 21) or (mes < 3) or (mes == 3 and dia <= 20):
        print("Estas en verano")
    else:
        print("Ingresa una fecha válida")

