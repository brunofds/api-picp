from fastapi import APIRouter, HTTPException
from typing import List
from model.usuario_schema import Usuario, UsuarioOut, UsuarioUpdate
from model.usuario_model import UsuarioModel
import sqlite3
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post('/usuarios', response_model=dict)
def add_usuario(usuario: Usuario):
    try:
        logger.info(f"Recebida requisição para criar usuário: {usuario}")
        UsuarioModel.adicionar(usuario.nome, usuario.email)
        return {'message': 'Usuário adicionado com sucesso'}
    except sqlite3.IntegrityError:
        logger.warning(f"Email já cadastrado: {usuario.email}")
        raise HTTPException(status_code=400, detail='Email já cadastrado')

@router.get('/usuarios', response_model=List[UsuarioOut])
def get_usuarios():
    usuarios = UsuarioModel.listar()
    logger.info(f"{len(usuarios)} usuários encontrados.")
    return [{'id': u['id'], 'nome': u['nome'], 'email': u['email']} for u in usuarios]

@router.get('/usuarios/{usuario_id}', response_model=UsuarioOut)
def get_usuario(usuario_id: int):
    usuario = UsuarioModel.listar()
    logger.info(f"Requisição para obter usuário ID {usuario_id}")
    for u in usuario:
        if u['id'] == usuario_id:
            logger.info(f"Usuário encontrado: {u}")
            return {'id': u['id'], 'nome': u['nome'], 'email': u['email']}
    raise HTTPException(status_code=404, detail='Usuário não encontrado')

@router.delete('/usuarios/{usuario_id}', response_model=dict)
def delete_usuario(usuario_id: int):
    logger.info(f"Requisição para deletar usuário ID {usuario_id}")
    if UsuarioModel.deletar(usuario_id) == 0:
        logger.warning(f"Usuário ID {usuario_id} não encontrado para deletar")
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return {'message': 'Usuário deletado com sucesso'}

@router.put('/usuarios/{usuario_id}', response_model=dict)
def update_usuario(usuario_id: int, usuario: UsuarioUpdate):
    logger.info(f"Requisição para atualizar usuário ID {usuario_id}")
    if UsuarioModel.atualizar(usuario_id, usuario.nome, usuario.email) == 0:
        logger.warning(f"Usuário ID {usuario_id} não encontrado para atualizar")
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return {'message': 'Usuário atualizado com sucesso'}
