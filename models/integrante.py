from sqlalchemy import Column, Integer, String
from bd import Base


class Integrante(Base):
    __tablename__ = "integrante"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100),nullable=False)
    cargo = Column(String(50), nullable=False)
    foto = Column(String(500),nullable=False)