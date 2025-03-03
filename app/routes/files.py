from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.base import ResponseModel
import os
import shutil
import uuid

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload_image", response_model=ResponseModel)
async def upload_image(imagen: UploadFile = File(...)):
    
    unique_filename = f"{uuid.uuid4().hex}_{imagen.filename}"
    file_location = os.path.join(UPLOAD_DIR, unique_filename)
    try:
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(imagen.file, file_object)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {e}")
    
    image_url = f"http://localhost:8080/{UPLOAD_DIR}/{unique_filename}"
    return ResponseModel(success=True, data={"imagen_url": image_url})
