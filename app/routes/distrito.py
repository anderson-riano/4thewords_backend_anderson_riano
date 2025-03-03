from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.distrito import Distrito
from app.schemas.distrito import DistritoListResponse

router = APIRouter()

@router.get("/distritos/", response_model=DistritoListResponse)
def get_distritos(db: Session = Depends(get_db)):
    distritos = db.query(Distrito).all()
    return DistritoListResponse(success=True, data=distritos)

@router.get("/distritos/{canton_id}", response_model=DistritoListResponse)
def get_distritos(canton_id: int, db: Session = Depends(get_db)):
    distritos = db.query(Distrito).filter(Distrito.canton_id == canton_id).all()
    return DistritoListResponse(success=True, data=distritos)
