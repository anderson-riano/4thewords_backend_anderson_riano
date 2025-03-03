from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.canton import Canton
from app.schemas.canton import CantonListResponse

router = APIRouter()

@router.get("/cantones/", response_model=CantonListResponse)
def get_cantones(db: Session = Depends(get_db)):
    cantones = db.query(Canton).all()
    return CantonListResponse(success=True, data=cantones)

@router.get("/cantones/{provincia_id}", response_model=CantonListResponse)
def get_cantones(provincia_id: int, db: Session = Depends(get_db)):
    cantones = db.query(Canton).filter(Canton.provincia_id == provincia_id).all()
    return CantonListResponse(success=True, data=cantones)
