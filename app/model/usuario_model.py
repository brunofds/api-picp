import sqlite3
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class UsuarioModel:
    db_path = "database.db"  # default

    @staticmethod
    def get_connection():
        conn = sqlite3.connect(UsuarioModel.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def criar_tabela():
        logger.info("Criando tabela 'usuario' se não existir.")
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
        logger.info(f"Adicionando usuário: nome={nome}, email={email}")
        with UsuarioModel.get_connection() as conn:
            conn.execute('INSERT INTO usuario (nome, email) VALUES (?, ?)', (nome, email))
            conn.commit()

    @staticmethod
    def listar():
        logger.info("Listando todos os usuários.")
        with UsuarioModel.get_connection() as conn:
            return conn.execute('SELECT * FROM usuario').fetchall()

    @staticmethod
    def deletar(usuario_id: int):
        logger.info(f"Tentando deletar usuário com ID {usuario_id}")
        with UsuarioModel.get_connection() as conn:
            result = conn.execute('DELETE FROM usuario WHERE id = ?', (usuario_id,))
            conn.commit()
            return result.rowcount


    @staticmethod
    def _valida_email_existente(email, usuario_id, conn):
        """
        Verifica se o email já existe na tabela de usuários, exceto para o usuário atual.
        """
        cursor = conn.execute('SELECT COUNT(*) FROM usuario WHERE email = ? AND id != ?', (email, usuario_id))
        count = cursor.fetchone()[0]
        return count > 0

    @staticmethod
    def atualizar(usuario_id: int, nome: Optional[str] = None, email: Optional[str] = None):
        """
        Atualiza apenas os campos fornecidos do usuário, mantendo os outros inalterados.
        """
        logger.info(f"Atualizando usuário ID {usuario_id} para nome={nome}, email={email}")
        with UsuarioModel.get_connection() as conn:
            # Verifica se o email já existe
            if email and UsuarioModel._valida_email_existente(email, usuario_id, conn):
                logger.warning(f"Email já cadastrado: {email}")
                raise sqlite3.IntegrityError('Email já cadastrado')
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