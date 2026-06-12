
# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).
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

 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom, ape):
    borrarPantalla()
    nombre = nom
    apellidos = ape
    return nombre, apellidos
