from pydantic import BaseModel
from app.schemas.base import ResponseModel

class CantonBase(BaseModel):
    nombre: str
    provincia_id: int

class CantonResponse(CantonBase):
    id: int

    class Config:
        from_attributes = True
        
class CantonListResponse(ResponseModel[list[CantonResponse]]):
    pass