import pyodbc

# Parámetros de conexión a SQL Server
server = 'NTB-BOG-144\SQLEXPRESS'  # Dirección IP del servidor SQL
database = 'db_asistencia_psicologica'  # Nombre de la base de datos
username = 'user_db_aap'  # Nombre de usuario
password = 'S3rv3r2023login'  # Contraseña

# Cadena de conexión
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def create_connection():
    try:
        # Crear y retornar la conexión a la base de datos
        connection = pyodbc.connect(connection_string)
        print('Conexión a BD Exitosa!!')
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {str(e)}")
        return None