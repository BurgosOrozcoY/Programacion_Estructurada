import funciones
import re 
from clientes import crud
from membresias import crud as crudMembresias

PATRON_TELEFONO = r"^\d{10}$"
PATRON_EMAIL = r"^[\w\.-]+@[\w\.-]+\.\w+$"
SIN_MEMBRESIA = {
   "Acceso a equipamiento" : "\u2714",
   "Acceso a vestidores:" : "\u2714",
   "Acceso a regaderas" : "\u2718",
   "Acceso a entrenadores" : "\u2718",
   "Beneficios exclusivos" : "\u2718"
}

def menuClientes():
    print("\n\t\t\t...::: C L I E N T E S:::... \n")
    opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Asignar membresia \n\t 8.- Regresar \n \t\tSeleccionar Opcion: ").strip()
    return opcion

def addClientes(conexionDB):
    print("\n\t\t\t...::: AGREGAR CLIENTES :::... \n")
    contadorClientes = 0
    opc="si"
    while opc=="si":
      funciones.clear()
      nombre=input("Nombre: ").upper().strip()
      apellido=input("Primer apellido: ").upper().strip()
      telefonoValido = False
      while telefonoValido == False:
        telefono=input("Número de teléfono: ").strip()
        if re.match(PATRON_TELEFONO, telefono):
         telefonoValido = True
        else:
           print("... ¡El número de teléfono debe contener exactamente 10 dígitos! ...")
      correoValido = False
      while correoValido == False:
        correo=input("Correo electrónico: ").strip()
        if re.match(PATRON_EMAIL, correo):
           correoValido = True
        else:
           print("... ¡El correo electrónico no es válido! ...")
      respuesta=crud.insert(nombre, apellido, telefono, correo, conexionDB)
      if respuesta:  
        funciones.success()
        contadorClientes +=1
      else:
        funciones.unsuccess()
      opc=""
      while opc!="si" and opc!="no":
        opc=input("¿Ingresar cliente nuevo? ").lower().strip()
    funciones.clear()
    print("Los clientes sin membresia tendrán acceso con ciertas retricciones: \n")
    for beneficio,disponible in SIN_MEMBRESIA.items():
       print(beneficio,disponible) 
    print(f"\n... ¡Se han registrado {contadorClientes} cliente(s) nuevo(s)! ...\n") 
    funciones.pause()

def showClientes(conexionDB):
    print("\n\t\t\t...::: MOSTRAR CLIENTES :::... \n")
    customers=crud.consult(conexionDB)
    print("\u2581" * 150)
    print("\n ID\t\tNombre\t\tApellido\t\tTeléfono\t\tCorreo\t\t\t\t\tMembresía\n")
    print("\u2594" * 150)
    if len(customers)>0:
       for i in customers:
           nombreMembresia = "Sin membresia"
           if i[5] != None:
              membresia = crudMembresias.searchId(i[5], conexionDB)
              if membresia != None:
                 nombreMembresia = membresia[1]
           print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t\t{i[3]}\t\t{i[4]}\t\t\t{nombreMembresia}")
    else:
         print("... ¡No hay clientes que mostrar! ... ")
    funciones.pause()
    funciones.clear()
    opc = ""
    while opc != "si" and opc != "no":
        opc = input("... ¿Desea generar un reporte de clientes (Si/No)? ...").lower().strip()
    if opc == "si":
       funciones.clear()
       opc =input("Seleccione la extención deseada: \n\n1.Reporte de clientes.TXT\n2.Reporte de clientes.DOCX\n\nSelección: ")
       if opc == "1":
          funciones.repClientes(customers)
          funciones.success()
       elif opc == "2":
          funciones.repClientesDocx(customers)
          funciones.success()
       else:
          input("... ¡No se ha generado el reporte, opcion inválida! ...\nENTER para continuar...")  

def resetClientes(conexionDB):
    print("\n\t\t\t...::: BORRAR TODOS LOS CLIENTES :::... \n")
    opc=""
    while opc!="si" and opc!="no":
        opc=input("¿Estas seguro que deseas borrar TODOS los clientes (Si/No)? ").lower().strip()
    if opc=="si":
        respuesta=crud.clean(conexionDB)
        if respuesta:  
           funciones.success()
        else:
           funciones.unsuccess()
        funciones.pause()

def searchClientes(conexionDB):
    print("\n\t\t\t...::: BUSCAR CLIENTES :::... \n")
    customer=input("Nombre del cliente: ").upper().strip()
    customers=crud.search(customer,conexionDB)
    if len(customers)>0:
       print("\n ID\t\tNombre\t\tApellido\t\tTeléfono\t\tCorreo\t\t\t\t\tMembresía\n")
       for i in customers:
           print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t\t{i[3]}\t\t{i[4]}\t\t\t{i[5]}")
    else:
         print("... ¡No hay clientes que Mostrar! ... ")
    funciones.pause()

def deleteClientes(conexionDB):
    print("\n\t\t\t...::: BORRAR CLIENTES :::... \n")
    nombre=input("Nombre del cliente: ").upper().strip()
    customers=crud.search(nombre,conexionDB)
    if len(customers)>0:
       print("\n ID\t\tNombre\t\tApellido\t\tTeléfono\t\tCorreo\t\t\t\t\tMembresía\n")
       for i in customers:
        print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t\t{i[3]}\t\t{i[4]}\t\t\t{i[5]}")
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Estas seguro que deseas borrar el/los cliente(s) (Si/No)? ").lower().strip()
        if opc=="si":
            respuesta=crud.delete(nombre,conexionDB)
            if respuesta:  
             funciones.success()
            else:
                funciones.unsuccess()
    else:
         print("... ¡No hay clientes que mostrar! ... ")
         funciones.pause()

def updateClientes(conexionDB):
    print("\n\t\t\t...::: MODIFICAR CLIENTES :::... \n")
    buscarNombre=input("Nombre del cliente: ").upper().strip()
    buscarApellido=input("Apellido del cliente: ").upper().strip()
    customers = crud.search(buscarNombre,conexionDB, buscarApellido)
    if len(customers)>0:
       print("\n ID\t\tNombre\t\tApellido\t\tTeléfono\t\tCorreo\t\t\t\t\tMembresía\n")
       for i in customers:
        print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t\t{i[3]}\t\t{i[4]}\t\t\t{i[5]}")
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Estas seguro que deseas modificar el cliente (Si/No)? ").lower().strip()
        if opc=="si":
            nombre = input("Nuevo nombre: ").upper().strip()
            apellido = input("Nuevo apellido: ").upper().strip()
            telefonoValido = False
            while telefonoValido == False:
               telefono = input("Nuevo telefono: ").strip()
               if re.match(PATRON_TELEFONO, telefono):
                  telefonoValido = True
               else:
                  print("... ¡El número de teléfono debe contener exactamente 10 dígitos! ...")
            correoValido = False
            while correoValido == False:
               correo=input("Correo electrónico: ").strip()
               if re.match(PATRON_EMAIL, correo):
                   correoValido = True
               else:
                  print("... ¡El correo electrónico no es válido! ...")
            respuesta=crud.update(nombre, apellido, telefono, correo, buscarNombre, buscarApellido, conexionDB)
            if respuesta:  
             funciones.success()
            else:
                funciones.unsuccess()
    else:
         print("... ¡No hay clientes que Mostrar! ... ")
         funciones.pause()

def asignarMembresia(conexionDB):
   print("\n\t\t\t...::: ASIGNAR MEMBRESIA :::...\n")
   nombre = input("Nombre del cliente: ").upper().strip()
   customers = crud.search(nombre,conexionDB)
   if len(customers) > 0:
      print("\u2581" * 150)
      print("\n ID\t\tNombre\t\tApellido\t\tTeléfono\t\tCorreo\t\t\t\t\tMembresía\n")
      print("\u2594" * 150)
      for i in customers:
         print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t\t{i[3]}\t\t{i[4]}\t\t\t{i[5]}")
      idCliente = input("ID del cliente: ").strip()
      idValido = False
      for i in customers:
         if str(i[0]) == idCliente:
            idValido = True
      if idValido:
         membresias = crudMembresias.consult(conexionDB)
         if len(membresias)>0:
            funciones.clear()
            print("\n\t\t\t...::: MEMBRESIAS DISPONIBLES :::...\n")
            print("\u2581" * 60)
            print("\n ID\t\tNombre\t\tPrecio\t\tDuración\n")
            print("\u2594" * 60)
            for i in membresias:
             print(f"{i[0]}\t\t{i[1]}\t\t${i[2]}\t\t{i[3]} Mes(es)") 
            idMembresia = input("\n\nID de la membresia seleccionada: ").strip()
            membresia = crudMembresias.searchId(idMembresia, conexionDB)
            if membresia != None:
                respuesta = crud.asignar(idCliente, idMembresia, conexionDB)
                if respuesta:
                    funciones.success()
                else:
                    funciones.unsuccess()
            else:
                print("... ¡El ID de la membresia es incorrecto! ...")
                funciones.pause()
         else:
            print("... ¡No hay membresias que mostrar! ...")
      else:
         print("...¡ El ID del cliente es incorrecto! ...")
         funciones.pause()
   else:
      print("... ¡No hay clientes que mostrar! ...")
      funciones.pause()   

