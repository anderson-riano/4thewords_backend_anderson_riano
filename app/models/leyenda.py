from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship

class Leyenda(Base):
    __tablename__ = "leyendas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    categoria = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    fecha = Column(Date, nullable=False)
    imagen_url = Column(String(255), nullable=False)
    distrito_id = Column(Integer, ForeignKey("distritos.id", ondelete="CASCADE"), nullable=False)

    distrito = relationship("Distrito", backref="leyendas")
