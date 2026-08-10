import funciones
from clientes import gestionClientes
from membresias import gestionMembresias
conexionDB = funciones.connection()

opcion = ""

while opcion != "3":
    funciones.clear()
    opcion = funciones.mainMenu()
    match opcion:
        case "1":
            while opcion != "8":
                funciones.clear()
                opcion = gestionClientes.menuClientes()
                match opcion:
                    case "1":
                        funciones.clear()
                        gestionClientes.addClientes(conexionDB)
                    case "2":
                        funciones.clear()
                        gestionClientes.deleteClientes(conexionDB)
                    case "3":
                        funciones.clear()
                        gestionClientes.updateClientes(conexionDB)
                    case "4":
                        funciones.clear()
                        gestionClientes.showClientes(conexionDB) 
                    case "5":
                        funciones.clear()
                        gestionClientes.searchClientes(conexionDB)
                    case "6":
                        funciones.clear()
                        gestionClientes.resetClientes(conexionDB)
                    case "7":
                        funciones.clear()
                        gestionClientes.asignarMembresia(conexionDB)
                    case "8":
                        print("")
                    case _:
                        print("Opcion invalida.")
                        funciones.pause()
        case "2":
            while opcion != "7":
                funciones.clear()
                opcion = gestionMembresias.menuMembresias()
                match opcion:
                    case "1":
                        funciones.clear()
                        gestionMembresias.addMembresias(conexionDB)
                    case "2":
                        funciones.clear()
                        gestionMembresias.deleteMembresias(conexionDB)
                    case "3":
                        funciones.clear()
                        gestionMembresias.updateMembresias(conexionDB)
                    case "4":
                        funciones.clear()
                        gestionMembresias.showMembresias(conexionDB) 
                    case "5":
                        funciones.clear()
                        gestionMembresias.searchMembresias(conexionDB)
                    case "6":
                        funciones.clear()
                        gestionMembresias.resetMembresias(conexionDB)
                    case "7":
                        print("")
                    case _:
                        print("Opcion invalida.")
                        funciones.pause()
        case "3":
            funciones.clear()
            funciones.finish()
        case _:
            print("\n\t   ... ¡Opcion inválida! ...")
            funciones.pause()
