from sqlalchemy.orm import Session
from models.integrante import Integrante
#from schemes.integrante import IntegranteScheme

def get_integrante(db: Session, id: int):
    return db.query(Integrante).filter(Integrante.id==id).first()

def get_integrantes(db:Session):
    return db.query(Integrante).all()

def insert_integrante(db: Session, id:int, nombre:str, cargo:str,foto:str):
    new_integrante = Integrante(id=id, nombre=nombre, cargo=cargo,foto=foto)
    db.add(new_integrante)
    db.commit()

def delete_integrante(db: Session, id: int):
    db.query(Integrante).filter(Integrante.id==id).delete()
    db.commit()
