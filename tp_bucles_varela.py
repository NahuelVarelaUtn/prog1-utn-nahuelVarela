import random

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (0, 100+1):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

num = int(input("Ingresa un numero entero: "))
num_absoluto = abs(num)
digitos= 0

if num_absoluto == 0:
    digitos = 1
else: 
    digitos = 0

while num_absoluto > 0 :
    num_absoluto //= 10
    digitos+=1

print(f"El numero tiene {digitos} digitos ")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores. 

num2 = int(input("Ingrese el primer numero para ver la suma de sus valores : "))
num3 = int(input("Ingrese otro numero :"))
sumatoria = 0

if num2 > num3 : 
    num2,num3 = num3, num2

for i in range (num2 + 2, num3):
    sumatoria += i
    print(sumatoria)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0. 


num_total = 0
num_ingresado = None  

while num_ingresado != 0:
    num_ingresado = int(input("Ingresa un número (0 para terminar): "))
    if num_ingresado != 0:
        num_total += num_ingresado
        print("Acumulado hasta ahora:", num_total)

print("La suma total es =", num_total)


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 


secreto= random.randint(1,9)
intentos = 0
respuesta = None

while secreto != respuesta : 
    respuesta = int(input("Ingresa un numero entre 0-9 :"))

    if secreto == respuesta :
        print(f"Adivinaste con exito!  En {intentos} intentos ")
    else:
        print("Vuelve a intentar")
        intentos +=1


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente. 

for i in range (100,0, -1):

    if i % 2 == 0 :
        print(i)
    else:
        continue


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario. 

n_ingresado = int(input("Ingrese un numero positivo "))
n_final = 0

if n_ingresado > 0 :
    for i in range (0, n_ingresado+1):
        n_final = n_final + i 
        print(n_final)
else:
    print("Ingrese un numero valido")



#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

num5 = 100
suma = 0
contador = 0
num = None

while contador < num5 and num != 0:
    num = int(input(f"Ingrese el número {contador+1} (0 para salir): "))
    if num != 0:
        suma += num
        contador += 1

if contador > 0:
    media = suma / contador
    print("La media de los números es:", media)
else:
    print("No se ingresaron números válidos.")



#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor). 

num5 = 100
suma = 0
contador = 0
num = None

while contador < num5 and num != 0:
    num = int(input(f"Ingrese el número {contador+1} (0 para salir): "))
    if num != 0:
        suma += num
        contador += 1

if contador > 0:
    media = suma / contador
    print("La media de los números es:", media)
else:
    print("No se ingresaron números válidos.")




#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    num //= 10

print("Número invertido:", invertido)

