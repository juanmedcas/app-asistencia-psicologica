# API de Gestión de Psicólogos

Esta es una API de gestión de psicólogos construida con FastAPI. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en una base de datos de psicólogos.


## Cómo Ejecutar el Proyecto en Otro Equipo

Para ejecutar el proyecto en otro equipo, sigue estos pasos:

1. **Requisitos Previos**

   Asegúrate de tener instalados los siguientes componentes en tu equipo:

   - [Python](https://www.python.org/downloads/): Debes tener Python 3.7 o una versión posterior instalada.

2. **Clonar el Repositorio**

   Abre una terminal o línea de comandos y navega al directorio donde desees clonar el repositorio. Luego, ejecuta el siguiente comando para clonar el proyecto desde tu repositorio en Git:

   ```bash
   git clone https://github.com/juanmedcas/app-asistencia-psicologica.git
   ```

3. **Crear un Entorno Virtual (Opcional pero Recomendado)**

   Es una buena práctica utilizar un entorno virtual para evitar conflictos entre las dependencias de diferentes proyectos. Para crear un entorno virtual, puedes utilizar el siguiente comando:

   ```bash
   python -m venv app-env
   ```

   Luego, activa el entorno virtual:

   - En Windows:

     ```bash
     app-env\Scripts\activate.bat
     ```

   - En macOS y Linux:

     ```bash
     source myenv/bin/activate
     ```

4. **Instalar Dependencias**

   Ve al directorio del proyecto y asegúrate de estar en la raíz del proyecto, donde se encuentra el archivo `requirements.txt`. Luego, ejecuta el siguiente comando para instalar las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar la Base de Datos (si es necesario)**

   Asegúrate de configurar la conexión a la base de datos en el archivo de configuración correspondiente, en este caso `conexion_bd.py`.

6. **Ejecutar la Aplicación con Uvicorn**

   Para ejecutar la aplicación, utiliza Uvicorn. Asegúrate de estar en el directorio raíz del proyecto y ejecuta el siguiente comando:

   ```bash
   uvicorn main:app --reload
   ```

   - `main:app` hace referencia al módulo principal de la aplicación y la variable `app` que contiene la instancia de FastAPI.
   - `--reload` habilita la recarga automática cuando realices cambios en el código.

7. **Acceder a la Aplicación**

   Una vez que el servidor se inicie correctamente, verás un mensaje que indica que la aplicación está ejecutándose. Abre un navegador web y accede a la URL [http://localhost:8000/psicologos](http://localhost:8000/psicologos) para interactuar con la API.

Ahora deberías poder ejecutar el proyecto en otro equipo siguiendo estos pasos. Asegúrate de que todas las dependencias se hayan instalado correctamente y de que la base de datos esté configurada adecuadamente si es necesario.



## Endpoints

### Listar Psicólogos

- **URL**: `/psicologos`
- **Método**: `GET`
- **Descripción**: Obtiene una lista de todos los psicólogos registrados en la base de datos.

### Obtener un Psicólogo por ID

- **URL**: `/psicologo/{id}`
- **Método**: `GET`
- **Descripción**: Obtiene un psicólogo específico de acuerdo al ID proporcionado.

### Insertar un Nuevo Psicólogo

- **URL**: `/psicologo`
- **Método**: `POST`
- **Descripción**: Permite la inserción de un nuevo psicólogo en la base de datos.

### Actualizar un Psicólogo por ID

- **URL**: `/psicologo/{id}`
- **Método**: `PUT`
- **Descripción**: Permite la actualización de un psicólogo existente según su ID.

### Eliminar un Psicólogo por ID

- **URL**: `/psicologo/{id}`
- **Método**: `DELETE`
- **Descripción**: Permite la eliminación de un psicólogo de la base de datos según su ID.

## Cómo Usar la API

Puedes utilizar cualquier cliente de API REST (como Postman o curl) para interactuar con esta API. A continuación, se muestran ejemplos de cómo usar los endpoints:

### Listar Psicólogos

```http
GET /psicologos
```

Este endpoint te proporcionará una lista de todos los psicólogos registrados en la base de datos.

### Obtener un Psicólogo por ID

```http
GET /psicologo/{id}
```

Reemplaza `{id}` con el ID del psicólogo que deseas obtener. Si el psicólogo existe, obtendrás sus detalles; de lo contrario, recibirás un error 404.

### Insertar un Nuevo Psicólogo

```http
POST /psicologo
```

Envía una solicitud POST con los datos del psicólogo en el cuerpo de la solicitud (en formato JSON). Por ejemplo:

```json
{
    "titulo": "Psicólogo Clínico",
    "nombre": "Juan Pérez",
    "universidad": "Universidad XYZ",
    "ciudad": "Bogotá",
    "email": "juan@example.com",
    "tel": 123456789
}
```

Recibirás una confirmación de que el psicólogo se ha insertado satisfactoriamente.

### Actualizar un Psicólogo por ID

```http
PUT /psicologo/{id}
```

Reemplaza `{id}` con el ID del psicólogo que deseas actualizar. Envía una solicitud PUT con los datos actualizados del psicólogo en el cuerpo de la solicitud (en formato JSON). Recibirás una confirmación de que el psicólogo se ha actualizado satisfactoriamente o un error 404 si el psicólogo no se encuentra.

### Eliminar un Psicólogo por ID

```http
DELETE /psicologo/{id}
```

Reemplaza `{id}` con el ID del psicólogo que deseas eliminar. Recibirás una confirmación de que el psicólogo se ha eliminado satisfactoriamente o un error 404 si el psicólogo no se encuentra.

## Recursos Adicionales

- [FastAPI Documentación Oficial](https://fastapi.tiangolo.com/)
- [Guía de inicio rápido de FastAPI](https://fastapi.tiangolo.com/tutorial/quickstart/)

¡Diviértete utilizando esta API para gestionar psicólogos!