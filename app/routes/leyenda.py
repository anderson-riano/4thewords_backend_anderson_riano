from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.leyenda import Leyenda
from app.models.distrito import Distrito
from app.models.canton import Canton
from app.schemas.leyenda import LeyendaRequest, LeyendaResponse, LeyendaListResponse
from app.schemas.base import ResponseModel
from datetime import date

router = APIRouter()

@router.get("/leyendas/", response_model=LeyendaListResponse)
def get_leyendas(
    db: Session = Depends(get_db),
    nombre: str = Query(None),
    categoria: str = Query(None),
    fecha: date = Query(None),
    provincia_id: int = Query(None),
    canton_id: int = Query(None),
    distrito_id: int = Query(None)
):
    query = db.query(Leyenda)

    if nombre:
        query = query.filter(Leyenda.nombre.ilike(f"%{nombre}%"))
    if categoria:
        query = query.filter(Leyenda.categoria.ilike(f"%{categoria}%"))
    if fecha:
        query = query.filter(Leyenda.fecha == fecha)
    if distrito_id:
        query = query.filter(Leyenda.distrito_id == distrito_id)
    else:
        if canton_id:
            query = query.join(Distrito).filter(Distrito.canton_id == canton_id)
        else:
            if provincia_id:
                query = query.join(Distrito).join(Canton).filter(Canton.provincia_id == provincia_id)

    leyendas = query.all()
    
    return LeyendaListResponse(
        success=True,
        data=leyendas
    )

@router.get("/leyendas/{leyenda_id}", response_model=ResponseModel[LeyendaResponse])
def get_leyenda(leyenda_id: int, db: Session = Depends(get_db)):
    leyenda = db.query(Leyenda).filter(Leyenda.id == leyenda_id).first()
    if not leyenda:
        return ResponseModel(success=False)
    
    
    distrito = db.query(Distrito).filter(Distrito.id == leyenda.distrito_id).first()
    
    canton = db.query(Canton).filter(Canton.id == distrito.canton_id).first() if distrito else None

    data = {
        "id": leyenda.id,
        "nombre": leyenda.nombre,
        "categoria": leyenda.categoria,
        "descripcion": leyenda.descripcion,
        "fecha": leyenda.fecha,
        "imagen_url": leyenda.imagen_url,
        "distrito_id": leyenda.distrito_id,     
        "canton_id": canton.id,         
        "provincia_id": canton.provincia_id,
    }
    return ResponseModel(success=True, data=data)


@router.post("/leyendas/", response_model=ResponseModel[LeyendaResponse])
def create_leyenda(request: LeyendaRequest, db: Session = Depends(get_db)):
    nueva_leyenda = Leyenda(**request.data.dict())
    db.add(nueva_leyenda)
    db.commit()
    db.refresh(nueva_leyenda)
    return ResponseModel(success=True, data=nueva_leyenda)

@router.put("/leyendas/{leyenda_id}", response_model=ResponseModel[LeyendaResponse])
def update_leyenda(leyenda_id: int, request: LeyendaRequest, db: Session = Depends(get_db)):
    leyenda = db.query(Leyenda).filter(Leyenda.id == leyenda_id).first()
    if not leyenda:
        return ResponseModel(success=False)

    for key, value in request.data.dict().items():
        setattr(leyenda, key, value)
    
    db.commit()
    db.refresh(leyenda)
    return ResponseModel(success=True, data=leyenda)

@router.delete("/leyendas/{leyenda_id}", response_model=ResponseModel[None])
def delete_leyenda(leyenda_id: int, db: Session = Depends(get_db)):
    leyenda = db.query(Leyenda).filter(Leyenda.id == leyenda_id).first()
    if not leyenda:
        return ResponseModel(success=False)

    db.delete(leyenda)
    db.commit()
    return ResponseModel(success=True)
