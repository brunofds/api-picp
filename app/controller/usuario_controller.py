from fastapi import APIRouter, HTTPException
from typing import List
from model.usuario_schema import Usuario, UsuarioOut, UsuarioUpdate
from model.usuario_model import UsuarioModel
import sqlite3

router = APIRouter()

@router.post('/usuarios', response_model=dict)
def add_usuario(usuario: Usuario):
    try:
        UsuarioModel.adicionar(usuario.nome, usuario.email)
        return {'message': 'Usuário adicionado com sucesso'}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail='Email já cadastrado')

@router.get('/usuarios', response_model=List[UsuarioOut])
def get_usuarios():
    usuarios = UsuarioModel.listar()
    return [{'id': u['id'], 'nome': u['nome'], 'email': u['email']} for u in usuarios]

@router.delete('/usuarios/{usuario_id}', response_model=dict)
def delete_usuario(usuario_id: int):
    if UsuarioModel.deletar(usuario_id) == 0:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return {'message': 'Usuário deletado com sucesso'}

@router.put('/usuarios/{usuario_id}', response_model=dict)
def update_usuario(usuario_id: int, usuario: UsuarioUpdate):
    if UsuarioModel.atualizar(usuario_id, usuario.nome, usuario.email) == 0:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return {'message': 'Usuário atualizado com sucesso'}
