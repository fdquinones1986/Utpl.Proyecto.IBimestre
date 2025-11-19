# Utpl.Proyecto.IBimestre
Repositorio base del proyecto de 1 primestre de Interoperabilidad

## Descripción
Este proyecto contiene una API REST básica desarrollada con FastAPI para propósitos educativos. El objetivo es enseñar cómo trabajar con APIs REST utilizando Python y FastAPI.

## Estructura del Proyecto
```
.
├── main.py              # Archivo principal con la aplicación FastAPI
├── models/              # Modelos y DTOs de la aplicación
│   ├── __init__.py      # Inicialización del módulo de modelos
│   └── persona_dto.py   # DTOs para la entidad Persona
├── requirements.txt     # Dependencias del proyecto
└── README.md           # Este archivo
```

## Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/fdquinones1986/Utpl.Proyecto.IBimestre.git
cd Utpl.Proyecto.IBimestre
```

### 2. Crear un entorno virtual con CodeSpace

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

## Inicializar la API

### Ejecutar el servidor de desarrollo
```bash
uvicorn main:app --reload
```

El servidor se iniciará en `http://127.0.0.1:8000`

### Opciones adicionales
- **Puerto personalizado:** `uvicorn main:app --reload --port 8080`
- **Host público:** `uvicorn main:app --reload --host 0.0.0.0`

## Endpoints Disponibles

Una vez que la API esté corriendo, puedes probar los siguientes endpoints:

### 1. Hola Mundo
```
GET http://127.0.0.1:8000/
```
Respuesta:
```json
{
  "mensaje": "¡Hola Mundo desde FastAPI!"
}
```

### 2. Saludo personalizado
```
GET http://127.0.0.1:8000/saludo/Juan
```
Respuesta:
```json
{
  "mensaje": "¡Hola Juan! Bienvenido a la API"
}
```

### 3. Información de la API
```
GET http://127.0.0.1:8000/info
```
Respuesta:
```json
{
  "nombre": "API de Ejemplo UTPL",
  "version": "1.0.0",
  "descripcion": "Esta es una API básica creada con FastAPI para propósitos educativos"
}
```

### 4. CRUD de Personas

#### Obtener todas las personas
```
GET http://127.0.0.1:8000/personas
```
Respuesta:
```json
[
  {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 30,
    "email": "juan.perez@example.com",
    "telefono": "+593987654321",
    "direccion": "Av. Principal 123, Loja"
  }
]
```

#### Obtener una persona por ID
```
GET http://127.0.0.1:8000/personas/1
```
Respuesta:
```json
{
  "id": 1,
  "nombre": "Juan",
  "apellido": "Pérez",
  "edad": 30,
  "email": "juan.perez@example.com",
  "telefono": "+593987654321",
  "direccion": "Av. Principal 123, Loja"
}
```

#### Crear una nueva persona
```
POST http://127.0.0.1:8000/personas
Content-Type: application/json

{
  "nombre": "María",
  "apellido": "García",
  "edad": 25,
  "email": "maria.garcia@example.com",
  "telefono": "+593987654322",
  "direccion": "Calle Secundaria 456, Loja"
}
```
Respuesta (201 Created):
```json
{
  "id": 2,
  "nombre": "María",
  "apellido": "García",
  "edad": 25,
  "email": "maria.garcia@example.com",
  "telefono": "+593987654322",
  "direccion": "Calle Secundaria 456, Loja"
}
```

#### Actualizar una persona
```
PUT http://127.0.0.1:8000/personas/1
Content-Type: application/json

{
  "edad": 31,
  "telefono": "+593987654999"
}
```
Respuesta:
```json
{
  "id": 1,
  "nombre": "Juan",
  "apellido": "Pérez",
  "edad": 31,
  "email": "juan.perez@example.com",
  "telefono": "+593987654999",
  "direccion": "Av. Principal 123, Loja"
}
```

#### Eliminar una persona
```
DELETE http://127.0.0.1:8000/personas/1
```
Respuesta: 204 No Content

## Documentación Interactiva

FastAPI genera automáticamente documentación interactiva para tu API:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

Estas interfaces te permiten probar los endpoints directamente desde el navegador.

## Próximos Pasos

Este es un esqueleto básico. Puedes expandir la API agregando:
- Más endpoints
- Modelos de datos con Pydantic
- Conexión a bases de datos
- Autenticación y autorización
- Manejo de errores personalizado
- Validación de datos
- CORS (Cross-Origin Resource Sharing)

## Recursos Adicionales
- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/)
- [Tutorial de FastAPI en español](https://fastapi.tiangolo.com/es/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)


