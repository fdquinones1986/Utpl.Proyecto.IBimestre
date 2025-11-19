"""
DTOs (Data Transfer Objects) para la entidad Persona
"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class PersonaDTO(BaseModel):
    """
    DTO completo de Persona con ID (usado para respuestas)
    """
    id: int = Field(..., description="ID único de la persona")
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre de la persona")
    apellido: str = Field(..., min_length=1, max_length=100, description="Apellido de la persona")
    edad: int = Field(..., ge=0, le=150, description="Edad de la persona")
    email: EmailStr = Field(..., description="Email de la persona")
    telefono: Optional[str] = Field(None, max_length=20, description="Teléfono de la persona")
    direccion: Optional[str] = Field(None, max_length=200, description="Dirección de la persona")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Juan",
                "apellido": "Pérez",
                "edad": 30,
                "email": "juan.perez@example.com",
                "telefono": "+593987654321",
                "direccion": "Av. Principal 123, Loja"
            }
        }


class PersonaCreateDTO(BaseModel):
    """
    DTO para crear una nueva Persona (sin ID)
    """
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre de la persona")
    apellido: str = Field(..., min_length=1, max_length=100, description="Apellido de la persona")
    edad: int = Field(..., ge=0, le=150, description="Edad de la persona")
    email: EmailStr = Field(..., description="Email de la persona")
    telefono: Optional[str] = Field(None, max_length=20, description="Teléfono de la persona")
    direccion: Optional[str] = Field(None, max_length=200, description="Dirección de la persona")

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "María",
                "apellido": "García",
                "edad": 25,
                "email": "maria.garcia@example.com",
                "telefono": "+593987654322",
                "direccion": "Calle Secundaria 456, Loja"
            }
        }


class PersonaUpdateDTO(BaseModel):
    """
    DTO para actualizar una Persona (todos los campos opcionales)
    """
    nombre: Optional[str] = Field(None, min_length=1, max_length=100, description="Nombre de la persona")
    apellido: Optional[str] = Field(None, min_length=1, max_length=100, description="Apellido de la persona")
    edad: Optional[int] = Field(None, ge=0, le=150, description="Edad de la persona")
    email: Optional[EmailStr] = Field(None, description="Email de la persona")
    telefono: Optional[str] = Field(None, max_length=20, description="Teléfono de la persona")
    direccion: Optional[str] = Field(None, max_length=200, description="Dirección de la persona")

    class Config:
        json_schema_extra = {
            "example": {
                "edad": 31,
                "telefono": "+593987654323"
            }
        }
