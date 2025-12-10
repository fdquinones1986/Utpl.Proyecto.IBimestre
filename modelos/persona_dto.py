from pydantic import BaseModel, EmailStr, Field, model_validator

class Persona(BaseModel):
    nombre: str = Field(..., min_length=4, max_length=100, description="Nombre de la persona", examples =["Juan", "María"])
    apellido: str = Field(..., min_length=4, max_length=100, description="Apellido de la persona", examples =["Pérez", "González"])
    email: EmailStr = Field(..., description="Correo electrónico de la persona", examples =["juan.perez@example.com", "maria.gonzalez@example.com"])
    edad: int = Field(..., ge=10, le=120, description="Edad de la persona", examples =[25, 40])
    direccion: str = Field(..., min_length=10, max_length=200, description="Dirección de la persona", examples =["Calle Falsa 123", "Avenida Siempre Viva 742"])
    telefono: str = Field(..., min_length=7, max_length=15, description="Número de teléfono de la persona", examples =["+1234567890", "+0987654321"])
    identificacion: str = Field(..., min_length=5, max_length=20, description="Identificación de la persona", examples =["123456789", "987654321"])