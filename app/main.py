import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.core.exception_handler import http_exception_handler, global_exception_handler
from app.routes import provincia, canton, distrito, leyenda, files
from fastapi.responses import JSONResponse
from app.schemas.base import ResponseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="4thewords API")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    
    allow_credentials=True,
    allow_methods=["*"],      
    allow_headers=["*"],      
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content=ResponseModel[list](
            success=False,
            message="Error de validación",
            data=exc.errors()
        ).model_dump(),
    )

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(provincia.router)
app.include_router(canton.router)
app.include_router(distrito.router)
app.include_router(leyenda.router)
app.include_router(files.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)
