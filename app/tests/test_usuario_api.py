import pytest
from fastapi.testclient import TestClient
from main import app
import os
from model.usuario_model import UsuarioModel

client = TestClient(app)

# Configuração do banco de dados para testes
# O caminho do banco de dados de teste é definido aqui
# e a tabela é criada antes de cada teste
# e removida após cada teste
# Isso garante que cada teste comece com um banco de dados limpo
# e não afete os outros testes
@pytest.fixture(autouse=True)
def setup_and_teardown():
    UsuarioModel.db_path = "test_database.db"
    if os.path.exists(UsuarioModel.db_path):
        os.remove(UsuarioModel.db_path)
    from database.init_db import init_db
    init_db()
    yield
    if os.path.exists(UsuarioModel.db_path):
        os.remove(UsuarioModel.db_path)


def test_criar_usuario():
    response = client.post("/users", json={"nome": "João", "email": "joao@email.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "Usuário adicionado com sucesso"}


def test_email_duplicado():
    client.post("/users", json={"nome": "João", "email": "joao@email.com"})
    response = client.post("/users", json={"nome": "Outro", "email": "joao@email.com"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Email já cadastrado"


def test_listar_usuarios():
    client.post("/users", json={"nome": "Maria", "email": "maria@email.com"})
    client.post("/users", json={"nome": "Carlos", "email": "carlos@email.com"})
    response = client.get("/users")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]["nome"] == "Maria"
    assert data[1]["nome"] == "Carlos"


def test_atualizar_usuario():
    client.post("/users", json={"nome": "Ana", "email": "ana@email.com"})
    response = client.put("/users/1", json={"nome": "Ana Paula", "email": "anapaula@email.com"})
    assert response.status_code == 200
    assert response.json()["message"] == "Usuário atualizado com sucesso"

    usuarios = client.get("/users").json()
    assert usuarios[0]["nome"] == "Ana Paula"


def test_deletar_usuario():
    client.post("/users", json={"nome": "Lucas", "email": "lucas@email.com"})
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Usuário deletado com sucesso"

    usuarios = client.get("/users").json()
    assert len(usuarios) == 0


def test_deletar_usuario_inexistente():
    response = client.delete("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário não encontrado"
