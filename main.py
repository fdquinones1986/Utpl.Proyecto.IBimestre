"""
API REST básica con FastAPI
Este es un esqueleto de API para enseñar a estudiantes
"""

from fastapi import FastAPI, HTTPException
from modelos.persona_dto import Persona
from db.supabase import create_supabase_client

dbPersona = []
#Crear el cliente de Supabase
supabase = create_supabase_client()

# Crear la instancia de FastAPI
app = FastAPI(
    title="API de Ejemplo UTPL - fdquinones@utpl.edu.ec",
    description="API REST básica para aprender FastAPI en Interoperabilidad de Sistemas",
    version="1.0.0"
)


@app.get("/")
def root():
    """
    Endpoint raíz - Hola Mundo
    """
    return {"mensaje": "¡Hola Mundo desde FastAPI por Felipe!"}


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
    
@app.post("/personas", response_model=Persona, tags=["Personas"])
def crear_persona(persona: Persona):
    """
    Endpoint para crear una nueva persona
    """
    data = supabase.table("personas").insert({
        "nombre": persona.nombre,
        "apellido": persona.apellido,
        "email": persona.email,
        "edad": persona.edad,
        "direccion": persona.direccion,
        "telefono": persona.telefono,
        "identificacion": persona.identificacion
        }).execute()
    return persona

@app.get("/personas", response_model=list[Persona], tags=["Personas"])
def obtener_personas():
    """
    Endpoint para crear una nueva persona
    """
    data = supabase.table("personas").select("*").execute()
    return data.data


@app.get("/personas/{identificacion}", response_model=Persona, tags=["Personas"])
def obtener_persona_por_identificacion(identificacion: str):
    """Buscar una persona por su identificación."""
    data = supabase.table("personas").select("*").eq("identificacion", identificacion).execute()
    if data.data:
        return data.data[0]
    raise HTTPException(status_code=404, detail="Persona no encontrada")


@app.put("/personas/{identificacion}", response_model=Persona, tags=["Personas"])
def actualizar_persona(identificacion: str, persona_actualizada: Persona):
    """Actualizar una persona existente por su identificación.

    La identificación de la ruta debe coincidir con la del cuerpo.
    """
    if identificacion != persona_actualizada.identificacion:
        raise HTTPException(status_code=400, detail="La identificación en la ruta y el cuerpo no coinciden")
    data = supabase.table("personas").update({
        "nombre": persona_actualizada.nombre,   
        "apellido": persona_actualizada.apellido,
        "email": persona_actualizada.email,
        "edad": persona_actualizada.edad,
        "direccion": persona_actualizada.direccion,
        "telefono": persona_actualizada.telefono,
        }).eq("identificacion", identificacion).execute()
    if data.data:
        return persona_actualizada
    raise HTTPException(status_code=404, detail="Persona no encontrada")


@app.delete("/personas/{identificacion}", response_model=Persona, tags=["Personas"])
def eliminar_persona(identificacion: str):
    """Eliminar una persona por su identificación.

    Retorna la persona eliminada o 404 si no existe.
    """
    data = supabase.table("personas").delete().eq("identificacion", identificacion).execute()
    if data.data:
        return data.data[0]
    raise HTTPException(status_code=404, detail="Persona no encontrada")

