from pydantic import BaseModel# ayuda a garantizar que los datos que se almacenen sean del tipo de valor
from conexion_bd import create_connection
import json

class Psicologo(BaseModel):
    titulo: str
    nombre: str
    universidad: str
    ciudad: str
    email: str
    tel: int

# Conexión a la base de datos
connection = create_connection()

def create_psicologo(psicologo: Psicologo):
    cursor=connection.cursor()#cursor
    cursor.execute("INSERT INTO Psicologo (Nombre, Universidad, Email, Telefono, Titulo, Ciudad) VALUES (?, ?, ?, ?, ?, ?)", (psicologo.nombre, psicologo.universidad, psicologo.email, psicologo.tel, psicologo.titulo, psicologo.ciudad))#sentencia SQL
    connection.commit()#guardar consulta
    filas = cursor.rowcount
    if filas:
        print(f"Filas afectadas: [{filas}] - | Usuario {psicologo.nombre} agregado satisfactoriamente")
    else:
        print("Error al registrar el Psicólogo")
    return filas

def read_psicologo(id: int):
    cursor=connection.cursor()#cursor
    cursor.execute("SELECT * FROM Psicologo WHERE Id = ?", (id,))#sentencia SQL
    rows=cursor.fetchall()#guardar consulta
    if rows:
        # Convertir los resultados a una lista de diccionarios
        columns = [desc[0] for desc in cursor.description]
        results_as_dict = [dict(zip(columns, row)) for row in rows]
        # Convertir a formato JSON
        json_result = json.dumps(results_as_dict, ensure_ascii=False).encode('utf-8').decode('utf-8')
        print(json_result)
    else:
        print("Psicólogo no encontrado")
    return json_result

def read_psicologos():
    cursor=connection.cursor()#cursor
    cursor.execute("SELECT * FROM Psicologo")#sentencia SQL
    rows=cursor.fetchall()#guardar consulta
    for row in rows:#recorrer consulta
        print(row)#imprimir valores por cada ciclo
    # Convertir los resultados a una lista de diccionarios
    columns = [desc[0] for desc in cursor.description]
    results_as_dict = [dict(zip(columns, row)) for row in rows]
    # Convertir a formato JSON
    json_result = json.dumps(results_as_dict, ensure_ascii=False).encode('utf-8').decode('utf-8')
    return json_result

def update_psicologo(id: int, psicologo: Psicologo):
    cursor=connection.cursor()#cursor
    cursor.execute("SELECT * FROM Psicologo WHERE Id = ?", (id,))#sentencia SQL
    rows=cursor.fetchall()#guardar consulta
    if rows:
        cursor.execute("""
        UPDATE Psicologo
        SET Nombre = ?, Universidad = ?, Email = ?, 
            Telefono = ?, Titulo = ?, Ciudad = ?
        WHERE Id = ?
        """, (psicologo.nombre, psicologo.universidad, psicologo.email, psicologo.tel, psicologo.titulo, psicologo.ciudad, id))
        connection.commit()#guardar consulta
        filas = cursor.rowcount
        print(f"Filas afectadas: [{filas}] - | Usuario {psicologo.nombre} actualizado satisfactoriamente")
    else:
        print("Psicólogo no encontrado")
    contador = cursor.rowcount
    return contador

def delete_psicologo(id: int):
    cursor=connection.cursor()#cursor
    cursor.execute("SELECT * FROM Psicologo WHERE Id = ?", (id,))#sentencia SQL
    rows=cursor.fetchall()#guardar consulta
    if rows:
        cursor.execute("DELETE FROM Psicologo WHERE Id = ?", (id))#sentencia SQL
        connection.commit()#guardar consulta
        filas = cursor.rowcount
        print(f"Filas afectadas: [{filas}] - | Usuario con Id {id} eliminado satisfactoriamente")
    else:
        print("Psicólogo no encontrado")
    contador = cursor.rowcount
    return contador