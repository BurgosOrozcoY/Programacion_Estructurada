pelis = {
    "nombre" : "TOY",
    "duracion" : "105 minutos",
    "genero" : "infantil"

}

import funciones
def mainMenu():
    print("\n\t\t...::: M E N U  P R I N C I P A L:::...\n")
    opcion = input("\t\n1.- Agregar\n2.- Borrar\n3.- Modificar\n4.- Mostrar\n5.- Buscar\n6.- Limpiar\n7.- Salir\n\tElegir una opción: ").strip()
    return opcion

def addPeliculas(pelis):
    print("\n\t\t...::: AGREGAR CARACTERISTICAS:::...\n")
    caracteristicas = input("Nombre de la caracteristica: ").upper().strip()
    valor = input("Nombre de la caracteristica: ").upper().strip()
    pelis = [caracteristica] = valor
    funciones.accionExitosa()

def showPeliculas(pelis):
    print("\n\t\t...::: MOSTRAR PELICULAS:::...\n")
    if len(pelis) > 0:
        print("\n\t\tCódigo\tPelícula\n")
        for i in range(0, len(pelis)):
            print(f"{i+1}\t\t{pelis[i]}")
        accionExitosa()
    else:
        print("... ¡No hay nada que mostrar, verifique! ...")

def limpiarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR TODAS LAS PELICULAS:::... \n")
    opc =  ""
    while opc != "si" and opc != "no":
        opc =  input("¿Estás seguro que deseas borrar TODAS las películas? (Si/No): ").lower().strip()
    if opc == "si":
        pelis = pelis.clear()
        funciones.accionExitosa()

def buscarPeliculas(pelis):
    print("\n\t\t\t...::: BUSCAR UNA CARACTERISTICA:::... \n")
    peli = input("Ingresar pelicula a buscar: ").lower().strip()
    noencontre = True
    for i in pelis:
        if i == peli:
            print(f"La caracteristica es: {peli} y su valor es: {pelis[peli]}")
            esperarTecla()
            noencontre = False
    if noencontre:
        input("\n\t...¡No existe la caracteristica de la pelicula, verifique!...")

def borrarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR CARACTERISTICA:::... \n")
    peli = input("Ingresar caracteristica a borrar: ").lower().strip()
    noencontre = True
    for i in pelis:
        if peli == i:
            noencontre = False
            opc = ""
            while opc != "si" and opc != "no":
                opc =  input("¿Estás seguro que deseas borrar la caracteristica de la película? (Si/No): ").lower().strip()
            if opc == "si":
                caracteristica = peli
    if noencontre:
            input("\n\t...¡No existe la pelicula, verifique!...")
    else:
        pelis.pop(caracteristica)
        accionExitosa()

def modificarPeliculas(pelis):
    print("\n\t\t\t...::: MODIFICAR VALOR DE LA CARACTERISTICA:::... \n")
    peli = input("Ingresar caracteristica a modificar: ").lower().strip()
    noencontre = True
    for i in pelis:
        if peli == i:
            noencontre = False
            print(f"La caracteristica es: {peli} y su valor es {pelis[peli]}")
            opc = ""
            while opc != "si" and opc != "no":
                opc =  input("¿Estás seguro que deseas modificar la caracteristica de la película? (Si/No): ").lower().strip()
            if opc == "si":
                pelis[peli] = input("Ingresar el nuevo valor de la caracteristica").upper().strip()
                accionExitosa()
    if noencontre:
            input("\n\t...¡No existe la caracteristica, verifique!...")
