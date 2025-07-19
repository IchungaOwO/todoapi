# ToDo API

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

---

## Descripción General

**ToDo API DIP** es una API RESTful desarrollada en **Python** usando el framework **FastAPI**. Este proyecto fue creado como parte del Diplomado Full Stack Web Developer en URBE, y está pensado para servir de backend robusto, escalable y didáctico para la gestión de tareas (ToDo) en aplicaciones web modernas. El objetivo es que estudiantes comprendan tanto los principios de las APIs REST como la integración con bases de datos reales y la estructuración profesional de proyectos.

---

## Tabla de Contenidos

- [Características Principales](#características-principales)
- [Arquitectura del Proyecto](#arquitectura-del-proyecto)
- [Instalación y Puesta en Marcha](#instalación-y-puesta-en-marcha)
- [Uso Básico de la API](#uso-básico-de-la-api)
- [Estructura de Carpetas](#estructura-de-carpetas)
- [Tecnologías y Herramientas](#tecnologías-y-herramientas)
- [Notas para Estudiantes](#notas-para-estudiantes)
- [Tarea Evaluativa: Sistema de Etiquetas (Tags)](#tarea-evaluativa-sistema-de-etiquetas-tags)

---

## Características Principales

- Crear tareas con título y descripción.
- Consultar todas las tareas creadas.
- Almacenar las tareas en una base de datos PostgreSQL.
- Validación de datos usando Pydantic.
- Arquitectura modular para facilitar la escalabilidad y el mantenimiento.
- Migraciones de base de datos profesionales usando Alembic.
- Documentación automática de la API con Swagger y Redoc.
- Control de CORS para acceso seguro desde el frontend.

---

## Arquitectura del Proyecto

El proyecto está estructurado de forma modular siguiendo buenas prácticas para aplicaciones profesionales en Python y FastAPI:

- **app.py**: Punto de entrada principal de la aplicación. Aquí se inicializa FastAPI, se configuran middlewares (como CORS), y se incluyen las rutas principales de la API.
- **routes/**: Carpeta donde se encuentran los routers que gestionan las rutas relacionadas a tareas y usuarios.
- **database.py**: Archivo de configuración para la conexión a la base de datos y definición del motor SQLAlchemy.
- **models/**: Definición de los modelos de datos (ORM) utilizados para mapear la base de datos.
- **schemas/**: Definición de los esquemas de validación de entrada/salida (usando Pydantic).
- **alembic/**: Gestión de migraciones de la base de datos.

---

## Instalación y Puesta en Marcha

Sigue estos pasos para levantar el proyecto en tu entorno local:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/itsronalds/todo-api-dip.git
   cd todo-api-dip
   ```

2. **Crea un entorno virtual e instala las dependencias:**

   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Unix/Mac:
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configura la base de datos PostgreSQL:**

   - Crea una base de datos (por ejemplo, `todo_db`).
   - Crea un archivo `.env` con tus credenciales de conexión, por ejemplo:
     ```
     DB_USER=
     DB_PASSWORD=
     DB_HOST=
     DB_NAME=
     TOKEN_KEY=
     TOKEN_ALGORITHM=HS256
     ```

4. **Ejecuta las migraciones con Alembic:**

   ```bash
   alembic upgrade head
   ```

5. **Inicia la aplicación:**

   ```bash
   uvicorn app:app --reload
   ```

6. **Accede a la documentación interactiva:**
   - [Swagger UI (localhost:8000/docs)](http://localhost:8000/docs)
   - [ReDoc (localhost:8000/redoc)](http://localhost:8000/redoc)

---

## Uso Básico de la API

Una vez tengas la aplicación corriendo, puedes interactuar fácilmente con la API a través de su documentación interactiva.

### ¿Cómo probar los endpoints?

1. **Abre tu navegador web y accede a:**  
   [http://localhost:8000/docs](http://localhost:8000/docs)

2. Ahí verás una interfaz llamada **Swagger UI** donde se listan todos los endpoints disponibles.  
   Desde esa interfaz puedes probar cada funcionalidad de la API de forma gráfica, viendo ejemplos de entradas y salidas, y ejecutando peticiones directamente.

3. Si deseas ver una documentación más detallada, puedes visitar:  
   [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Ejemplo de flujo básico

- **Crear una tarea:**  
  En Swagger UI, busca el endpoint para crear tareas (usualmente `POST /tasks/create`), haz clic en "Try it out", rellena los campos requeridos (por ejemplo, título y descripción) y ejecuta la petición.
- **Ver todas las tareas:**  
  Busca el endpoint para listar tareas (`GET /tasks`), haz clic en "Try it out" y luego "Execute" para ver la respuesta.

---

## Estructura de Carpetas

```
todo-api-dip/
│
├── app.py
├── database.py
├── requirements.txt
├── .env.example
├── routes/
│   ├── task.py
│   └── user.py
├── models/
│   └── task.py
│   └── user.py
├── schemas/
│   └── task.py
│   └── user.py
└── alembic/
    └── ...
```

---

## Tecnologías y Herramientas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [PostgreSQL](https://www.postgresql.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [JSON Web Token](https://pypi.org/project/jsonwebtoken/)

---

## Tarea Evaluativa: Sistema de Etiquetas (Tags)

### **Descripción del Reto**

El objetivo de esta tarea es que extiendas la funcionalidad de la ToDo API para que las tareas puedan tener etiquetas asociadas. Las etiquetas (o "tags") son palabras clave o categorías que ayudan a organizar y clasificar las tareas. Este sistema es muy útil en aplicaciones reales, ya que permite filtrar, buscar y agrupar tareas de manera eficiente y flexible.

### **¿Qué aprenderás con este reto?**

- Cómo crear relaciones muchos a muchos en bases de datos relacionales usando SQLAlchemy y Alembic.
- Cómo diseñar nuevos modelos y migraciones para expandir tu base de datos.
- Cómo crear y documentar nuevos endpoints RESTful en FastAPI.
- Cómo trabajar con filtros y consultas más avanzadas en tus endpoints.

### **Requisitos de la tarea**

1. **Modelo de Etiquetas**

   - Crea un nuevo modelo llamado `Tag` (o `Etiqueta`).
   - Este modelo debe tener, al menos, un campo `nombre` (name) que sea único.
   - Implementa una relación “muchos a muchos” entre tareas y etiquetas: una tarea puede tener varias etiquetas y una etiqueta puede ser utilizada por varias tareas.
   - Deberás crear una tabla intermedia (de asociación) para esta relación.

2. **Migraciones**

   - Genera las migraciones necesarias usando Alembic para crear las nuevas tablas en la base de datos.

3. **Endpoints CRUD de Etiquetas**

   - Crea endpoints para crear, listar, actualizar y eliminar etiquetas.
   - Permite que los usuarios asocien y desasocien etiquetas a las tareas existentes mediante endpoints apropiados (puede ser al crear/editar una tarea o mediante endpoints específicos).
   - Asegúrate de que los nombres de las etiquetas sean únicos; no debe haber dos etiquetas con el mismo nombre.

4. **Filtrado de Tareas por Etiqueta**

   - Modifica el endpoint que lista las tareas para que acepte un parámetro opcional que permita filtrar las tareas por una o más etiquetas (por ejemplo, mostrando solo las tareas que tengan la etiqueta “urgente”).
   - Puedes hacerlo mediante parámetros en la URL, como `GET /tasks?tags=urgente,trabajo`.

5. **Documentación**
   - Actualiza la documentación interactiva (Swagger UI) para que los usuarios puedan ver y probar los nuevos endpoints relacionados con etiquetas y la funcionalidad de filtrado por etiquetas.
   - Incluye ejemplos claros de cómo asociar etiquetas a tareas y cómo filtrar usando etiquetas.

### **Guía de implementación**

- **Paso 1:** Crea el modelo `Tag` en el archivo correspondiente dentro de la carpeta `models/`.
- **Paso 2:** Define la relación muchos a muchos entre tareas y etiquetas (posiblemente con una tabla intermedia).
- **Paso 3:** Genera y aplica la migración con Alembic para reflejar estos cambios en la base de datos.
- **Paso 4:** Crea los esquemas Pydantic necesarios en la carpeta `schemas/`.
- **Paso 5:** Implementa los endpoints CRUD de etiquetas y la lógica para asociar/desasociar etiquetas en los archivos de rutas correspondientes.
- **Paso 6:** Modifica el endpoint de listado de tareas para incluir el filtrado por etiquetas.
- **Paso 7:** Actualiza la documentación y verifica que los cambios funcionen desde Swagger UI.

### **Bonus (opcional)**

- Permite que los usuarios creen etiquetas nuevas directamente al crear o editar una tarea.
- Implementa validaciones adicionales para evitar etiquetas vacías o muy largas.
- Permite eliminar una etiqueta solamente si no está asociada a ninguna tarea.

### **Aspectos a evaluar**

- Correcta implementación de la relación muchos a muchos en la base de datos.
- Endpoints funcionales y seguros.
- Migraciones limpias y consistentes.
- Documentación clara y comprensible.
- Código bien estructurado y siguiendo el estilo del proyecto.

---
