
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#Procedimiento que borre pantalla
def borrarPantalla():
    print("\033c")
#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    borrarPantalla()
    nombre = input("Ingresar nombre: ").strip().upper()
    apellidos = input("Ingresar apellidos: ").strip().upper()
    print(f"El nombre completo del alumno es: {nombre} {apellidos}")

#funcion1()


 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nombre, apellidos):
    borrarPantalla()
    #nombre = input("Ingresar nombre: ").strip().upper() - Ya no es necesario
    #apellidos = input("Ingresar apellidos: ").strip().upper() - Ya no es necesario
    print(f"El nombre completo del alumno es: {nombre} {apellidos}")
#funcion3("Daniel", "Fernandez")

 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    borrarPantalla()
    nombre = input("Ingresar nombre: ").strip().upper()
    apellidos = input("Ingresar apellidos: ").strip().upper()
    return nombre, apellidos

#nom, ape = funcion2()
#print(f"El nombre completo del alumno es: {nom} {ape}")
 #4.- Funcion que recibe parametros y regresa valor
def funcion4():
    borrarPantalla()
    nombre = nombre
    apellidos = ape
    return nombre, apellidos

nom, ape = funcion4("Raul", "Flores")
print(f"El nombre completo del alumno es: {nom} {ape}")

#Invocar las funciones

