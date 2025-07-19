Este proyecto fue hecho usando de base al proyecto modelo que se nos fue facilitado del modulo de backend, ya que al tratar de ejecutar las migraciones presentaba distintos problemas de compatibilidad,
asi que opte por crearlo de 0 usando la estructura para guiarme, en este README explicare que es el proyecto, como funciona y las herramientas necesarias, cabe aclarar que use los mismos requerimientos que el proyecto original asi que lo mas seguro es que se ejecute sin problemas.

ToDo API Personal

Tecnologías Usadas
   
   Python 3.9+

   FastAPI

   SQLAlchemy ORM

   PostgreSQL

   Alembic (migraciones)

   Pydantic (validación)

   Uvicorn (servidor ASGI)

   JSON Web Token (JWT) para autenticación

   Git para control de versiones

Descripción General

ToDo API Personal es una API RESTful desarrollada en Python usando el framework FastAPI para gestionar tareas con un sistema avanzado de etiquetas (tags). El proyecto implementa autenticación con usuarios, manejo de relaciones muchos a muchos entre tareas y etiquetas, y una arquitectura modular y escalable.

Este backend fue construido con fines educativos y como proyecto funcional para gestionar tareas con control de usuarios, etiquetas y filtrado avanzado, incluyendo migraciones con Alembic.

Tabla de Contenidos:

   Características Principales

   Arquitectura del Proyecto

   Instalación y Puesta en Marcha

   Uso de la API

   Estructura del Proyecto

   Tecnologías Usadas

   Notas


Características Principales:

   Gestión completa de usuarios con autenticación.

   CRUD para tareas: creación, consulta, edición, eliminación.

   Sistema de etiquetas con relación muchos a muchos con tareas.

   Creación y edición de tareas con asociación/desasociación de etiquetas.

   Filtrado de tareas por etiquetas (por uno o varios tags).

   Validación y serialización con Pydantic.

   Migraciones gestionadas con Alembic para mantener la base de datos sincronizada.

   Seguridad básica con manejo de tokens JWT (configurable).

   Uso de SQLAlchemy ORM para manejo de base de datos relacional PostgreSQL.


Arquitectura del Proyecto:
   
   app.py: Inicialización de la aplicación FastAPI, configuración de middlewares y registro de routers.

   database.py: Configuración y conexión a la base de datos con SQLAlchemy.

   models/: Modelos ORM para usuarios, tareas, etiquetas y tablas asociativas.

   schemas/: Definición de esquemas Pydantic para validación y serialización de datos de entrada/salida.

   routes/: Rutas y lógica de endpoints REST para tareas, etiquetas y usuarios.

   alembic/: Carpeta con migraciones automáticas para cambios en la base de datos.

   utils/: Funciones auxiliares, autenticación y dependencias.

   .env: Variables de entorno con configuración sensible (base de datos, claves JWT, etc.).

Estructura del Proyecto:
todoapi/
│
├── app.py
├── database.py
├── requirements.txt
├── .env
├── alembic/
│   └── versions/
├── models/
│   ├── task.py
│   ├── tag.py
│   ├── user.py
├── schemas/
│   ├── task.py
│   ├── tag.py
│   ├── user.py
├── routes/
│   ├── task.py
│   ├── tag.py
│   ├── user.py
├── utils/
│   └── auth.py
└── README.md


Instalación:
   
   git clone https://github.com/IchungaOwO/todoapi.git
   
   cd todoapi

Crea un entorno virtual e instala dependencias:

   python -m venv venv

   pip install -r requirements.txt

Configura la base de datos PostgreSQL y el archivo .env con tus credenciales:

   DB_USER=tu_usuario
   DB_PASSWORD=tu_password
   DB_HOST=localhost
   DB_NAME=nombre_base_de_datos
   TOKEN_KEY=clave_secreta_jwt
   TOKEN_ALGORITHM=HS256

Ejecuta migraciones para crear las tablas:
   
   alembic upgrade head

Ejecuta la aplicación:
   
   uvicorn app:app --reload

Uso de la API:
   
   Para las pruebas y usos de los endpoints, utilice Postman por temas de comodidad y manejo de errores, asi que recomiendo el uso de este mismo al momento de hacer las consultas

Endpoints principales:

   POST /users/register: Registro de nuevo usuario.

   POST /users/login: Autenticación y obtención de token JWT.

   GET /tasks: Listar tareas del usuario autenticado, opcionalmente filtradas por etiquetas.

   POST /tasks: Crear nueva tarea con opcional asociación de etiquetas.

   GET /tasks/{task_id}: Obtener tarea por ID.

   PUT /{task_id}: Actualizar tarea, incluyendo sus etiquetas.

   DELETE /{task_id}: Eliminar tarea.

   CRUD similar para etiquetas en /tags.

Ejemplo de creacion de usuario:

{
    "username": "juanperez",
    "email": "juan.perez@example.com",
    "password": "12345678"
}

los datos que deberia colocar en el login son estos:

   "username": "juanperez",
   "password": "12345678"
   
En el caso que este usando postman, no olvide colocar los siguientes datos en el apartado de header una vez reciba su token de la siguiente forma

Key: Authorization Value: Bearer <tu_token_jwt>

Ejemplo de creacion de tags:

{
    "name": "urgente"
}


Ejemplo de creación de tarea con etiquetas:

{
  "title": "Comprar libros",
  "description": "Ir a la librería y comprar libros de programación.",
  "tag_ids": [1]
}

El PUT se hace de la misma manera, no olvidar que al hacer tanto PUT como Delate solo basta que ponga el id del task que desee cambiar, no hace falta hacer /tasks/1, ya que la consulta daria error,
si eso le molesta puede ir a router, tasks, y cambiar la consulta para que se ejecute de esa manera, yo no lo hice por comodidad.

Notas
   La autenticación requiere que los endpoints protegidos usen el token JWT generado al iniciar sesión.

   Los esquemas Pydantic permiten que la API valide y documente automáticamente las entradas y salidas.

   Las etiquetas son únicas y pueden asociarse a múltiples tareas y viceversa.

   El filtrado de tareas por etiquetas es opcional y permite pasar varios IDs de etiquetas para filtrar.

Y eso es todo el proyecto, espero haber sido claro y lo mas explicativo posible, muchas gracias por leer hasta aqui, espero que no le explote al ejecutar :)

