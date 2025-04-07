from fastapi import FastAPI
from app.router import router  # Importa o roteador centralizado
from database.init_db import init_db
import logging

# Configuração de logging com saída em console e em arquivo
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("/tmp/app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI()

# Inicializa todas as tabelas do banco
init_db()

# Registra as rotas
app.include_router(router)
