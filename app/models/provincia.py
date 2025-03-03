from sqlalchemy import Column, Integer, String
from app.database import Base

class Provincia(Base):
    __tablename__ = "provincias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)
