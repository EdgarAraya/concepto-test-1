from pydantic import BaseModel
 

class IntegranteScheme(BaseModel):
    id:int
    nombre:str
    cargo:str
    foto:str

    class Config:
	    orm_mode = True