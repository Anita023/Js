from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, list 

class TraineeBase(BaseModel):
    tipo_doc : str = Field(..., description = "Tipo de documento del aprendiz (CC, TI, CE)",pattern = "^(CC|TI|CE)$", example = "CC" )
    documento : str = Field(..., description = "Número de documento del aprendiz", min_length = 6, max_length = 10, pattern="^[0-9]+$", example = 1234567890)
    nombre : str = Field(..., description = "Nombre del aprendiz",min_length = 2, max_length = 100, example = "Juan Pérez")
    ficha : str = Field(..., description = "Número de ficha del aprendiz", min_length = 6, max_length = 7, pattern = "^[0-9]+$", example = "1234567")
    programa : str = Field(..., description = " Nombre del programa de formación del aprendiz", min_length = 2, max_length = 4, example = "ADSO")
    email : EmailStr = Field(..., description = "Correo electronico del aprendiz", example = "juan.perez@sena.edu.co")



class TraineeCreate(TraineeBase):
    pass 



class TraineeUpdate(BaseModel):
    tipo_doc : Optional[str] = Field(None, pattern = "^(CC|TI|CE)$" )
    nombre : Optional [str] = Field(None, min_length = 3)
    ficha : Optional [str] = Field(None,pattern = "^[0-9]+$")
    programa : Optional [str] = Field(None, min_length = 2)
    email : Optional [EmailStr] = None



class TraineeResponse(TraineeBase):
    data : Optional[List[TraineeBase]] = None  # Datos consumidos de la API Rick & Morty
