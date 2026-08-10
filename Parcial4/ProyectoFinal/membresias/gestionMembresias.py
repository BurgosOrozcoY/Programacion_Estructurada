import funciones
from membresias import crud

def menuMembresias():
    print("\n\t\t\t...::: M E M B R E S I A S :::... \n")
    opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Regresar \n \t\tSeleccionar Opcion: ").strip()
    return opcion

def addMembresias(conexionDB):
    print("\n\t\t\t...::: AGREGAR MEMBRESIA :::... \n")
    acumPrecios = 0
    opc="si"
    while opc=="si":
      nombre=input("Nombre de la membresía: ").upper().strip()
      precio=input("Costo de la membresía (MXN): ").upper().strip()
      duracion=input("Duración de la membresía (Meses): ").upper().strip()
      respuesta=crud.insert(nombre, precio, duracion, conexionDB)
      if respuesta:  
        funciones.success()
        acumPrecios += float(precio)
      else:
        funciones.unsuccess()
      opc=""
      while opc!="si" and opc!="no":
        opc=input("¿Ingresar nueva membresía? ").lower().strip()
    print(f"\nValor total de las nuevas membresias: ${acumPrecios}\n") 
    funciones.pause()

def showMembresias(conexionDB):
    print("\n\t\t\t...::: MOSTRAR MEMBRESIAS :::... \n")
    membresias=crud.consult(conexionDB)
    print("\u2581" * 75)
    print("\n ID\t\tNombre\t\tPrecio\t\t\t\tDuración\n")
    print("\u2594" * 75)
    if len(membresias)>0:
       for i in membresias:
           print(f"{i[0]}\t\t{i[1]}\t\t${i[2]}\t\t\t\t{i[3]} Mes(es)\n")
    else:
         print("... ¡No hay membresias que mostrar! ... ")
    funciones.pause()

def resetMembresias(conexionDB):
    print("\n\t\t\t...::: BORRAR TODAS LAS MEMBRESIAS :::... \n")
    opc=""
    while opc!="si" and opc!="no":
        opc=input("¿Estas seguro que deseas borrar TODAS las membresias (Si/No)? ").lower().strip()
    if opc=="si":
        respuesta=crud.clean(conexionDB)
        if respuesta:  
           funciones.success()
        else:
           funciones.unsuccess()
        funciones.pause()

def searchMembresias(conexionDB):
    print("\n\t\t\t...::: BUSCAR MEMBRESIAS :::... \n")
    membresia=input("Nombre de la membresía: ").upper().strip()
    membresias=crud.search(membresia,conexionDB)
    if len(membresias)>0:
       print("\u2581" * 60)
       print("\n ID\t\tNombre\t\tPrecio\t\tDuración\n")
       print("\u2594" * 60)
       for i in membresias:
           print(f"{i[0]}\t\t{i[1]}\t\t${i[2]}\t\t{i[3]} Mes(es)")
    else:
         print("... ¡No hay membresias que mostrar! ... ")
    funciones.pause()

def deleteMembresias(conexionDB):
    print("\n\t\t\t...::: BORRAR MEMBRESIA :::... \n")
    nombre=input("Nombre del membresia: ").upper().strip()
    membresias=crud.search(nombre,conexionDB)
    if len(membresias)>0:
       print("\u2581" * 60)
       print("\n ID\t\tNombre\t\tPrecio\t\tDuración\n")
       print("\u2581" * 60)
       for i in membresias:
        print(f"{i[0]}\t\t{i[1]}\t\t${i[2]}\t\t{i[3]} Mes(es)")
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Estas seguro que deseas borrar la membresía (Si/No)? ").lower().strip()
        if opc=="si":
            respuesta=crud.delete(nombre,conexionDB)
            if respuesta:  
             funciones.success()
            else:
                funciones.unsuccess()
    else:
         print("... ¡No hay membresias que mostrar! ... ")
    funciones.pause()

def updateMembresias(conexionDB):
    print("\n\t\t\t...::: MODIFICAR MEMBRESIAS :::... \n")
    buscarNombre=input("Nombre de la membresia: ").upper().strip()
    membresias = crud.search(buscarNombre,conexionDB)
    if len(membresias)>0:
       print("\u2581" * 60)
       print("\n ID\t\tNombre\t\tPrecio\t\tDuración\n")
       print("\u2581" * 60)
       for i in membresias:
        print(f"{i[0]}\t\t{i[1]}\t\t${i[2]}\t\t{i[3]} Mes(es)")
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Estas seguro que deseas modificar esta membresía (Si/No)? ").lower().strip()
        if opc=="si":
            nombre = input("Nuevo nombre: ").upper().strip()
            precio = input("Nuevo precio: ").upper().strip()
            duracion = input("Nueva duración: ").upper().strip()
            respuesta=crud.update(nombre, precio, duracion, buscarNombre, conexionDB)
            if respuesta:  
             funciones.success()
            else:
                funciones.unsuccess()
    else:
         print("... ¡No hay membresias que Mostrar! ... ")
    funciones.pause()