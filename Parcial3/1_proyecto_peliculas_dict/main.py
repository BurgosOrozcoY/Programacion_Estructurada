'''
Crear un proyecto que permita gestionar (administrar) peliculas.
Colocar un menú de opciones: Agregar, borrar, modificar, mostrar, buscar, limpiar una lista de peliculas.

Notas:
1.- Utilizar funciones y mandarlas a llamar desde otro modulo.
2.- Utilizar dict para almacenar los atributos (nombre, categoria)
3.- Utilizar o implementar BD relacional con MySQL para guardar la información
'''

import peliculas

pelis = []

opc = "1"

while opc != "7":
    peliculas.clear()
    opc = peliculas.mainMenu()
    match opc:
        case "1":
            peliculas.clear()
            peliculas.addPeliculas(pelis)
        case "2": 
            peliculas.clear()
            peliculas.borrarPeliculas(pelis)
        case "3": 
            peliculas.clear()
            peliculas.modificarPeliculas(pelis)
        case "4": 
            peliculas.clear()
            peliculas.showPeliculas(pelis)
        case "5": 
            peliculas.clear()
            peliculas.buscarPeliculas(pelis)
        case "6": 
            peliculas.clear()
            peliculas.limpiarPeliculas(pelis)
        case "7":
            peliculas.clear()
            peliculas.terminar()
        case _:
            peliculas.otherwise()
        