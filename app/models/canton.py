from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Canton(Base):
    __tablename__ = "cantones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    provincia_id = Column(Integer, ForeignKey("provincias.id", ondelete="CASCADE"), nullable=False)

    provincia = relationship("Provincia", backref="cantones")