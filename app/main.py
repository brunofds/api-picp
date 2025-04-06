from typing import List
import sqlite3
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException



app = FastAPI()

class Usuario(BaseModel):
    nome: str
    email: str


# Modelo Pydantic para representar os dados do usuário
class UserOut(Usuario):
    id: int
    nome: str


# Função para conectar (ou criar) ao  banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Criar a tabela de usuários
with get_db_connection() as conn: 
    conn.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()


# Rota para listar usuários
@app.get('/users', response_model=List[UserOut])
def get_users():
    with get_db_connection() as conn:
        users = conn.execute('SELECT * FROM usuario').fetchall()
    return [{'id': user['id'], 'nome': user['nome'], 'email': user['email']} for user in users]


@app.get('/users/{usuario_id}', response_model=UserOut)
def get_user(usuario_id: int):
    with get_db_connection() as conn:
        user = conn.execute('SELECT * FROM usuario WHERE id = ?', (usuario_id,)).fetchone()
        if user is None:
            raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return {'id': user['id'], 'nome': user['nome'], 'email': user['email']}


# Rota para adicionar um usuário
@app.post('/users', response_model=dict)
def add_user(usuario: Usuario):
    with get_db_connection() as conn:
        try:
            conn.execute('INSERT INTO usuario (nome, email) VALUES (?, ?)', (usuario.nome, usuario.email))
            conn.commit()
        except sqlite3.IntegrityError as exc:
            raise HTTPException(status_code=400, detail='Email já cadastrado') from exc
    return {'message': 'Usuário adicionado com sucesso'}


# Rota para deletar um usuário
@app.delete('/users/{usuario_id}', response_model=dict)
def delete_usuario(usuario_id: int):
    with get_db_connection() as conn:
        result = conn.execute('DELETE FROM usuario WHERE id = ?', (usuario_id,))
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return {'message': 'Usuário deletado com sucesso'}


# Rota para atualizar um usuário
@app.put('/users/{usuario_id}', response_model=dict)
def update_usuario(usuario_id: int, usuario: Usuario):
    with get_db_connection() as conn:
        result = conn.execute('UPDATE usuario SET nome = ?, email = ? WHERE id = ?', (usuario.nome, usuario.email, usuario_id))
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return {'message': 'Usuário atualizado com sucesso'}
