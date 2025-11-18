#) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
numero = int(input("Ingrese un número entero positivo: "))
for i in range(1, numero + 1):
    print(f"El factorial de {i} es {factorial(i)}")


#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique. 

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
posicion = int(input("Ingrese la posición hasta la cual quieras ver la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(posicion):
    print(fibonacci(i), end=" ")
    

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
#algoritmo general. 

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero no negativo): "))
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto. 
#Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
#unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este 
#procedimiento: 
#1. Dividir el número por 2. 
#2. Guardar el resto (0 o 1). 
#3. Repetir el proceso con el cociente hasta que llegue a 0. 
#4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario. 

#Convertir el número 10 a binario: 
#10 ÷ 2 = 5     resto: 0   
# 5 ÷ 2 = 2     resto: 1   
# 2 ÷ 2 = 1     resto: 0   
# 1 ÷ 2 = 0     resto: 1   
#Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010". 


def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
numero_decimal = int(input("Ingrese un número entero positivo en base decimal: "))
if numero_decimal == 0:
    print("La representación binaria de 0 es 0")
else:
    binario = decimal_a_binario(numero_decimal)
    print(f"La representación binaria de {numero_decimal} es {binario}")

#Entrego hasta acá profe porque me quede trabado en el siguiente punto, y no quiero dejar sin entregrar, lo voy a terminar a la brevedad.
