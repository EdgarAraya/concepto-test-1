import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bd import SessionLocal, engine,Base
from Resources import integrante


# Esto crea las tablas Debe ir si o si
Base.metadata.create_all(bind=engine)

# incializamos la app 
app = FastAPI(root_path="/api") 

#añadimos Cors para evitar problemas con fornt-end
app.add_middleware(CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'])
# Añadimos los recursos o rutas que se requieren
app.include_router(integrante.router)
 
 # Acá deberia implementar la conexión a la base de datos

# Este lo ocuparemos mas adelante para discriminar entre ambientes (prod/dev)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# run with command: 
#    uvicorn app:app --reload and test with postman or similar 
#    windows: python -m uvicorn app:app --reload

# UPDATE:
#       Ahora funciona con el comando : python3 app.py runserver
