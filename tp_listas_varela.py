#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
#range. 

multiplos_de_4 = list(range(4, 101, 4))

print(multiplos_de_4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

mis_favoritos = ["Play 5", "Café", "Counter", "Futbol", "BOCA"]


print("El penúltimo elemento es:", mis_favoritos[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
#ejemplo: 

vacia = []

vacia.append("Programar")
vacia.append("Café")
vacia.append("Futbol")

print("La lista resultante es:", vacia)


#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
#respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
#en los videos o bien investigar cómo funciona el indexing con números negativos! 
#animales = ["perro", "gato", "conejo", "pez"] 

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"
print(animales)


#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 

numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

#Lo que entiendo es que la funcion "remove", elimina un elemento de la lista, y que la funcion  "max", toma el elemento de mayor valor, eliminando el mismo


#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
#pantalla los dos primeros. 

lista_5 = list(range(10,31,5))
print(f"lista completa f{lista_5}")
print("Lista cortada con slicing", lista_5[:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
#cualesquiera. 

autos = ["sedan", "polo", "suran", "gol"] 
autos[1:3]= ["GLH", "TWISTER" ]
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
#directamente. Imprimir la lista resultante por pantalla. 

dobles : list =[]

for i in range(5,16,5):
    dobles.append(i*2)
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
#diferentes clientes: 

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 

#a) Agregar "jugo" a la lista del tercer cliente usando append. 

compras[2].append("jugo")

#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 

compras[1][1]= "tallarines"

#c) Eliminar "pan" de la lista del primer cliente.  
#del compras[0][0] #modo usando ambos indices
compras[0].remove("pan") #otro metodo buscando en el indice,dandole un valor que sea buscado en el subindice, y eliminado si es encontrado

#d) Imprimir la lista resultante por pantalla 

print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 

lista_anidada = []
#● Posición lista_anidada[0]: 15 
lista_anidada.append([15])
#● Posición lista_anidada[1]: True 
lista_anidada.append([True])
#● Posición lista_anidada[2][0]: 25.5 
lista_anidada.append([25.5])
#● Posición lista_anidada[2][1]: 57.9 
lista_anidada[2].append(57.9)
#● Posición lista_anidada[2][2]: 30.6 
lista_anidada[2].append(30.6)
#● Posición lista_anidada[3]: False 
lista_anidada.append([False])
#Imprimir la lista resultante por pantalla. 
print(lista_anidada)