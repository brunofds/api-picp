from fastapi import FastAPI
from controller.usuario_controller import router
from database.init_db import init_db


app = FastAPI()

# Inicializa todas as tabelas do banco
init_db()

# Registra as rotas
app.include_router(router)
