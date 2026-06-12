print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[23,45,23,33,25,100,-100]
print(numeros)

lista = "["
for i in range(0, len(numeros)):
    lista += f"{numeros[i]}, "
print(f"{lista}]")

cont = len(numeros)

lista = "["
i = 0
while i<len(numeros):
    lista+= f"{numeros[i]}, "
    i+=1
print(f"{lista}]")

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=["Hola", "NBA", "Ganador", "Perdedor"]
palabra = input("Palabra a buscar: ")

#1er FORMA
if palabra in palabras:
    print(f"La palabra {palabra} existe en la lista")
else:
    print(f"la palabra {palabra} no existe en la lista")

#2DA FORMA
encontre = False
for i in palabras:
   if i == palabra:
      encontre = True 
    
if encontre :
    print(f"{palabra} está en la lista.")
else:
    print(f"{palabra} no está en la lista.")

#3er FORMA
encontre = False

i = 0
while i < len(palabras):
    if palabras [i] == palabra:
        encontre = True
    i+=1

if encontre :
    print(f"{palabra} está en la lista.")
else:
    print(f"{palabra} no está en la lista.")
    

#Ejemplo 3 Añadir elementos a la lista
lista = []
true = "S"
while true == "S":
    # valor = input("Ingresar valor de la lista: ").upper().strip()
    # lista.append(valor)
    lista.append(input("Ingresar valor de la lista: ").upper().strip())
    true = input("¿Agregar otro elemento? (S/N)").upper().strip()

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda =[
            ["Carlos", "6181234567"],
            ["Juan", "6184567891"],
            ["Tony", "6187894561"]
        ]

print(agenda) 

for i in agenda:
    print(i)

for r in range(0,3): # Controla los renglones
    for c in range(0,2): #Controla las columnas
        print(agenda [r] [c])