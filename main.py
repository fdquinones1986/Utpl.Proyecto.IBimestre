"""
API REST básica con FastAPI
Este es un esqueleto de API para enseñar a estudiantes
"""

from fastapi import FastAPI, HTTPException, status
from typing import List
from models import PersonaDTO, PersonaCreateDTO, PersonaUpdateDTO

# Crear la instancia de FastAPI
app = FastAPI(
    title="API de Ejemplo UTPL - fdquinones@utpl.edu.ec",
    description="API REST básica para aprender FastAPI en Interoperabilidad de Sistemas",
    version="1.0.0"
)

# Almacenamiento en memoria para personas
personas_db: dict[int, PersonaDTO] = {}
contador_id: int = 0


@app.get("/")
def root():
    """
    Endpoint raíz - Hola Mundo
    """
    return {"mensaje": "¡Hola Mundo desde FastAPI!"}


@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    """
    Endpoint de ejemplo con parámetro de ruta
    """
    return {"mensaje": f"¡Hola {nombre}! Bienvenido a la API"}


@app.get("/info")
def informacion():
    """
    Endpoint de información de la API
    """
    return {
        "nombre": "API de Ejemplo UTPL",
        "version": "1.0.0",
        "descripcion": "Esta es una API básica creada con FastAPI para propósitos educativos"
    }


# ========== ENDPOINTS DE PERSONA ==========

@app.get("/personas", response_model=List[PersonaDTO], tags=["Personas"])
def obtener_personas():
    """
    Obtener todas las personas
    """
    return list(personas_db.values())


@app.get("/personas/{persona_id}", response_model=PersonaDTO, tags=["Personas"])
def obtener_persona(persona_id: int):
    """
    Obtener una persona por ID
    """
    if persona_id not in personas_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Persona con ID {persona_id} no encontrada"
        )
    return personas_db[persona_id]


@app.post("/personas", response_model=PersonaDTO, status_code=status.HTTP_201_CREATED, tags=["Personas"])
def crear_persona(persona: PersonaCreateDTO):
    """
    Crear una nueva persona
    """
    global contador_id
    contador_id += 1
    
    nueva_persona = PersonaDTO(
        id=contador_id,
        **persona.model_dump()
    )
    
    personas_db[contador_id] = nueva_persona
    return nueva_persona


@app.put("/personas/{persona_id}", response_model=PersonaDTO, tags=["Personas"])
def actualizar_persona(persona_id: int, persona_actualizada: PersonaUpdateDTO):
    """
    Actualizar una persona existente
    """
    if persona_id not in personas_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Persona con ID {persona_id} no encontrada"
        )
    
    persona_actual = personas_db[persona_id]
    datos_actualizados = persona_actualizada.model_dump(exclude_unset=True)
    
    persona_actualizada_final = persona_actual.model_copy(update=datos_actualizados)
    personas_db[persona_id] = persona_actualizada_final
    
    return persona_actualizada_final


@app.delete("/personas/{persona_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Personas"])
def eliminar_persona(persona_id: int):
    """
    Eliminar una persona
    """
    if persona_id not in personas_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Persona con ID {persona_id} no encontrada"
        )
    
    del personas_db[persona_id]
    return None
