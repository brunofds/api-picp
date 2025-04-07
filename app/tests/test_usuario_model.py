import os
import pytest
import sqlite3
from model.usuario_model import UsuarioModel

@pytest.fixture(autouse=True)
def setup_teardown():
    UsuarioModel.db_path = "test_database.db"
    if os.path.exists(UsuarioModel.db_path):
        os.remove(UsuarioModel.db_path)
    UsuarioModel.criar_tabela()
    yield
    if os.path.exists(UsuarioModel.db_path):
        os.remove(UsuarioModel.db_path)


def test_adicionar_usuario():
    UsuarioModel.adicionar("Teste", "teste@email.com")
    usuarios = UsuarioModel.listar()
    assert len(usuarios) == 1
    assert usuarios[0]["nome"] == "Teste"


def test_listar_usuario_vazio():
    usuarios = UsuarioModel.listar()
    assert usuarios == []


def test_atualizar_usuario():
    UsuarioModel.adicionar("Velho Nome", "velho@email.com")
    result = UsuarioModel.atualizar(1, "Novo Nome", "novo@email.com")
    assert result == 1

    usuarios = UsuarioModel.listar()
    assert usuarios[0]["nome"] == "Novo Nome"


def test_deletar_usuario():
    UsuarioModel.adicionar("Lucas", "lucas@email.com")
    result = UsuarioModel.deletar(1)
    assert result == 1

    usuarios = UsuarioModel.listar()
    assert len(usuarios) == 0


def test_deletar_inexistente():
    result = UsuarioModel.deletar(999)
    assert result == 0
