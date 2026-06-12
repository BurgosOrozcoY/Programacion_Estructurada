'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''

num = int(input("Ingresar tabla deseada: "))

print(f"{num} x 1 = {num * 1}")
print(f"{num} x 2 = {num * 2}")
print(f"{num} x 3 = {num * 3}")
print(f"{num} x 4 = {num * 4}")
print(f"{num} x 5 = {num * 5}")
print(f"{num} x 6 = {num * 6}")
print(f"{num} x 7 = {num * 7}")
print(f"{num} x 8 = {num * 8}")
print(f"{num} x 9 = {num * 9}")
print(f"{num} x 10 = {num * 10}")

num_tabla = int(input("Número de tabla: "))

num = 1

multi = num_tabla * num
print(f"{num_tabla} x {num} = {multi}")
num +=1

multi = num_tabla * num
print(f"{num_tabla} x {num} = {multi}")
num +=1

multi = num_tabla * num
print(f"{num_tabla} x {num} = {multi}")
num +=1

multi = num_tabla * num
print(f"{num_tabla} x {num} = {multi}")
num +=1

multi = num_tabla * num
print(f"{num_tabla} x {num} = {multi}")
num +=1

multi = num_tabla * num
print(f"{num_tabla} x {num} = {multi}")
num +=1

multi = num_tabla * num
print(f"{num_tabla} x {num} = {multi}")
num +=1

multi = num_tabla * num
print(f"{num_tabla} x {num} = {multi}")
num +=1

multi = num_tabla * num
print(f"{num_tabla} x {num} = {multi}")
num +=1

multi = num_tabla * num
print(f"{num_tabla} x {num} = {multi}")
num +=1

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''

num_tabla = int(input("Numero de la tabla: "))

for num in range(1,11):
  multi = num_tabla * num
  print(f"{num_tabla} x {num} = {multi}")


num = 1
numTabla = int(input("Numero de la tabla: "))

while num < 11:
  resultado = num * numTabla
  print(f"{numTabla} x {num} = {resultado}")

  num +=1

'''
 Crear un programa que calcule e imprima cualquier tabla de multiplicar
Restricciones: 
1.- Sin estructuras de control 
2.- Con funciones
'''


def tabla(num_tabla, n):
    multi = num_tabla * n
    print(f"{num_tabla} x {n} = {multi}")
    return n

num_tabla = int(input("Número de tabla: "))
num = 1

'''
 Crear un programa que calcule e imprima cualquier tabla de multiplicar
Restricciones: 
1.- Con estructuras de control 
2.- Con funciones
'''
def tabla(num_tabla, n):
    multi = num_tabla * n
    print(f"{num_tabla} x {n} = {multi}")
    return n

num_tabla = int(input("Número de tabla: "))
num = 1

for i in range(10, 0, -1):
    tabla(num_tabla, i)
    