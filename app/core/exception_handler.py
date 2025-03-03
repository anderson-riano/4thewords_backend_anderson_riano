from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.base import ResponseModel

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ResponseModel[None](
            success=False,
            message=exc.detail,
            data=None
        ).model_dump(),
    )

async def global_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, SQLAlchemyError):
        message = "Error en la base de datos"
    else:
        message = "Error interno del servidor"
    
    return JSONResponse(
        status_code=500,
        content=ResponseModel[None](
            success=False,
            message=message,
            data=None
        ).model_dump(),
    )
