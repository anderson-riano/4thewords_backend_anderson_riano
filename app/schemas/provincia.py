from pydantic import BaseModel
from app.schemas.base import ResponseModel

class ProvinciaBase(BaseModel):
    nombre: str

class ProvinciaResponse(ProvinciaBase):
    id: int

    class Config:
        from_attributes = True
        
class ProvinciaListResponse(ResponseModel[list[ProvinciaResponse]]):
    pass
