import sqlite3
from typing import Optional

class UsuarioModel:
    @staticmethod
    def get_connection():
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def criar_tabela():
        with UsuarioModel.get_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                )
            ''')
            conn.commit()

    @staticmethod
    def adicionar(nome: str, email: str):
        with UsuarioModel.get_connection() as conn:
            conn.execute('INSERT INTO usuario (nome, email) VALUES (?, ?)', (nome, email))
            conn.commit()

    @staticmethod
    def listar():
        with UsuarioModel.get_connection() as conn:
            return conn.execute('SELECT * FROM usuario').fetchall()

    @staticmethod
    def deletar(usuario_id: int):
        with UsuarioModel.get_connection() as conn:
            result = conn.execute('DELETE FROM usuario WHERE id = ?', (usuario_id,))
            conn.commit()
            return result.rowcount


    @staticmethod    
    def atualizar(usuario_id: int, nome: Optional[str] = None, email: Optional[str] = None):
        """
        Atualiza apenas os campos fornecidos do usuário, mantendo os outros inalterados.
        """
        with UsuarioModel.get_connection() as conn:
            query = 'UPDATE usuario SET '
            params = []
            if nome is not None:
                query += 'nome = ?, '
                params.append(nome)
            if email is not None:
                query += 'email = ?, '
                params.append(email)
            query = query.rstrip(', ') + ' WHERE id = ?'
            params.append(usuario_id)
            result = conn.execute(query, tuple(params))
            conn.commit()
            return result.rowcount