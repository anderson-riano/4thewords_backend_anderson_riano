from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Distrito(Base):
    __tablename__ = "distritos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    canton_id = Column(Integer, ForeignKey("cantones.id", ondelete="CASCADE"), nullable=False)

    canton = relationship("Canton", backref="distritos")