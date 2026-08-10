import funciones

def insert(nombre, apellido, telefono, correo, conexionDB):
    try:
        if conexionDB!=None:
            cursor=conexionDB.cursor()
            cursor.execute("insert into clientes values(null,%s, %s, %s, %s, null)",(nombre, apellido, telefono, correo))
            conexionDB.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
    
def consult(conexionDB):
    try:
        if conexionDB!=None:
            cursor=conexionDB.cursor()
            cursor.execute("select * from clientes")
            return cursor.fetchall()
        else: 
            return []
    except:
        return []
    
def search(nombre, conexionDB, apellido = None):
    try:
        if conexionDB!=None:
            cursor=conexionDB.cursor()
            if apellido is None:
                cursor.execute("select * from clientes where nombre=%s", (nombre,))
            else:
                cursor.execute("select * from clientes where nombre=%s and apellido=%s", (nombre, apellido))
            return cursor.fetchall()
        else: 
            return []
    except:
        return []

def clean(conexionDB):
    try:
        if conexionDB!=None:
            cursor=conexionDB.cursor()
            cursor.execute("truncate clientes")
            conexionDB.commit()
            return True
        else: 
            return False
    except:
        return False
    
def delete(nombre, conexionDB):
    try:
        if conexionDB!=None:
            cursor=conexionDB.cursor()
            cursor.execute("delete from clientes where nombre=%s", (nombre,))
            conexionDB.commit()
            return True
        else: 
            return False
    except:
        return False
    
def update(nombre, apellido, telefono, correo, buscarNombre, buscarApellido, conexionDB):
    try:
        if conexionDB!=None:
            cursor=conexionDB.cursor()
            cursor.execute("update clientes set nombre=%s, apellido=%s, telefono=%s, correo=%s where nombre =%s and apellido=%s", (nombre, apellido, telefono, correo, buscarNombre, buscarApellido))
            conexionDB.commit()
            return True
        else: 
            return False
    except Exception as e:
        print(e)
        return False

def asignar(idCliente, idMembresia, conexionDB):
    try:
        if conexionDB != None:
            cursor = conexionDB.cursor()
            cursor.execute("update clientes set id_membresia =%s where id=%s", (idMembresia, idCliente))
            conexionDB.commit()
            return True
        else:
            return False
    except:
        return False

    