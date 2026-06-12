"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

print("\033c")
#Funciones más comunes en las listas
paises=["México","Canada", "EUA", "México", "Brasil"]
numeros=[23, 45, 8, 24]
varios=[33, 3.1416, "hola", False]
vacio=[]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacio)
print(paises[1])


#Recorrer la lista 
#1er forma 
for i in paises:
    print(i)

 #2do forma 
for i in range(0, 5):
    print(paises[i])
paises=["México","Canada", "EUA", "México", "Brasil"]

for i in range(0, len(paises)): #Len es para  el tamaño de la lista
    print(paises[i])
print(paises)
#ordenar elementos de una lista
paises.sort()
print(paises)

# #dar la vuelta a una lista
paises.reverse()
print(paises)


#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("Honduras")
print(paises)

#2da forma

paises.insert(1, "Argentina")
print(paises)
paises.insert(100, "Panama")
print(paises)
paises.append(23)
paises.append(3)
print(paises)
paises.sort()
print(paises)


#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4) #Posición
print(paises) 

#2da forma 
paises.remove("EUA") #valor
print(paises)

#Buscar un elemento dentro de la lista
buscar = "Brasil" in paises
if buscar == True:
    print("True")
else:
    print("False")

#Contar el numeros de veces que aparece un elemento dentro de una lista
numeros=[23,45,24,8,23,50,23]
x = int(input("Número a contar: "))
cuantas = numeros.count(x)
print(f"El número {x} aparece: {cuantas} veces")

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
posicion = numeros.index(50)
print(f"Posicion: {posicion}")

#Unir el contenido de una lista dentro de otra lista
numeros=[23,45,24,8,23,50,23]
print(numeros)
numeros2=[100,-100]
print(numeros2)
numeros.extend(numeros2)
print(numeros)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente
numeros.sort()
numeros.reverse()
print(numeros)

