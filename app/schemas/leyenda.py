from typing import Optional
from pydantic import BaseModel
from datetime import date
from app.schemas.base import RequestModel, ResponseModel

class LeyendaBase(BaseModel):
    nombre: str
    categoria: str
    descripcion: str
    fecha: date
    imagen_url: str
    distrito_id: int
    canton_id: Optional[int] = None
    provincia_id: Optional[int] = None

class LeyendaCreate(LeyendaBase):
    pass

class LeyendaResponse(LeyendaBase):
    id: int

    class Config:
        from_attributes = True

class LeyendaRequest(RequestModel[LeyendaCreate]):
    pass

class LeyendaListResponse(ResponseModel[list[LeyendaResponse]]):
    pass
