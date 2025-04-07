# tests/conftest.py ou diretamente no test_usuario_model.py
import model.usuario_model as model_class
import sqlite3

def setup_module(module):
    model_class.UsuarioModel.get_connection = staticmethod(lambda: sqlite3.connect("test_database.db"))
    model_class.UsuarioModel.criar_tabela()
