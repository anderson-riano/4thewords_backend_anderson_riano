from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.provincia import Provincia
from app.schemas.provincia import ProvinciaListResponse

router = APIRouter()

@router.get("/provincias/", response_model=ProvinciaListResponse)
def get_provincias(db: Session = Depends(get_db)):
    provincias = db.query(Provincia).all()
    return ProvinciaListResponse(success=True, data=provincias)