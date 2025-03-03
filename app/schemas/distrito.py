from pydantic import BaseModel
from app.schemas.base import ResponseModel

class DistritoBase(BaseModel):
    nombre: str
    canton_id: int

class DistritoResponse(DistritoBase):
    id: int

    class Config:
        from_attributes = True
        
class DistritoListResponse(ResponseModel[list[DistritoResponse]]):
    pass