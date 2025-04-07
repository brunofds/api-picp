from fastapi import FastAPI
from controller.usuario_controller import router
from model.usuario_model import UsuarioModel


app = FastAPI()

# Inicializa o banco
UsuarioModel.criar_tabela()

# Registra as rotas
app.include_router(router)
