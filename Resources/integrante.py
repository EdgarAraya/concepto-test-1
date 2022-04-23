from typing import List

from starlette.routing import request_response
from schemes.integrante import IntegranteScheme
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from bd import get_db
from crud.integrante import *
from fastapi import  Request
router = APIRouter()  

@router.get('/integrantes')
def get_obtener_integrantes(db: Session = Depends(get_db)):
    return get_integrantes(db)

@router.post('/integrante')
def post_anadir_integrante(new_integrante:IntegranteScheme, db:Session = Depends(get_db)):
    insert_integrante (db, new_integrante.id,new_integrante.nombre,new_integrante.cargo,new_integrante.foto)
    
    return {"message:" f"Complete, insertado= id:{new_integrante.id},nombre:{new_integrante.nombre}"
    }

@router.get("/app")
def read_main(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}

@router.get('/')
def get_obtener_integrantes(db: Session = Depends(get_db)):
   return {"message:" "En api"}