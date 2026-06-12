# 1er utilizar los modulos 
import modulos

modulos.borrarPantalla()
#modulos.funcion1()

nom= "Daniel"
ape = "Carreon"

nombre, apellidos = modulos.funcion4(nom, ape)
print(f"Nombre: {nombre} \nApellidos: {apellidos}")
modulos.funcion3(nom, ape)


#2da formar de utilizar modulos

from modulos import borrarPantalla, funcion4

borrarPantalla()
nombre, apellidos = funcion4(nom, ape)
print(f"Nombre: {nombre}\nApellidos: {apellidos}")

