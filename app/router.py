from fastapi import APIRouter
from controller.usuario_controller import router as usuario_router
# Importe outros routers aqui conforme necessário
# from controller.produto_controller import router as produto_router

router = APIRouter()

# Inclua os routers de cada entidade
router.include_router(usuario_router, prefix="/users", tags=["Usuários"])
# router.include_router(produto_router, prefix="/products", tags=["Produtos"])
# Adicione outros routers aqui conforme necessário