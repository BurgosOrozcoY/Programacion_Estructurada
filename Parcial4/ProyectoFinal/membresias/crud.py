import funciones

def insert(nombre, precio, duracion, conexionDB):
    try:
        if conexionDB!=None:
            cursor=conexionDB.cursor()
            cursor.execute("insert into membresias values(null,%s, %s, %s)",(nombre, precio, duracion))
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
            cursor.execute("select * from membresias")
            return cursor.fetchall()
        else: 
            return []
    except:
        return []
    
def search(nombre, conexionDB):
    try:
        if conexionDB!=None:
            cursor=conexionDB.cursor()
            cursor.execute("select * from membresias where nombre=%s", (nombre,))
            return cursor.fetchall()
        else: 
            return []
    except:
        return []

def clean(conexionDB):
    try:
        if conexionDB!=None:
            cursor=conexionDB.cursor()
            cursor.execute("truncate membresias")
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
            cursor.execute("delete from membresias where nombre=%s", (nombre,))
            conexionDB.commit()
            return True
        else: 
            return False
    except:
        return False
    
def update(nombre, precio, duracion, buscarNombre, conexionDB):
    try:
        if conexionDB!=None:
            cursor=conexionDB.cursor()
            cursor.execute("update membresias set nombre=%s, precio=%s, duracion=%s where nombre =%s", (nombre, precio, duracion, buscarNombre))
            conexionDB.commit()
            return True
        else: 
            return False
    except Exception as e:
        print(e)
        return False

def searchId(idMembresia, conexionDB):
    try:
        if conexionDB != None:
            cursor = conexionDB.cursor()
            cursor.execute("select * from membresias where id=%s", (idMembresia,))
            return cursor.fetchone()
        else:
            return None
    except:
        return None