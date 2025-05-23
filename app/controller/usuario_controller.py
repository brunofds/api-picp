from fastapi import APIRouter, HTTPException
from typing import List
from model.usuario_schema import Usuario, UsuarioOut, UsuarioUpdate
from model.usuario_model import UsuarioModel
import sqlite3
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post('/', response_model=dict)
def add_usuario(usuario: Usuario):
    try:
        logger.info("Recebida requisição para criar usuário: %s", usuario)
        UsuarioModel.adicionar(usuario.nome, usuario.email)
        return {'message': 'Usuário adicionado com sucesso'}
    except sqlite3.IntegrityError:
        logger.warning(f"Email já cadastrado: {usuario.email}")
        raise HTTPException(status_code=400, detail='Email já cadastrado')

@router.get('/', response_model=List[UsuarioOut])
def get_usuarios():
    usuarios = UsuarioModel.listar()
    logger.info(f"{len(usuarios)} usuários encontrados.")
    return [{'id': u['id'], 'nome': u['nome'], 'email': u['email']} for u in usuarios]

@router.get('/{id}', response_model=UsuarioOut)
def get_usuario(id: int):
    usuario = UsuarioModel.listar()
    logger.info(f"Requisição para obter usuário ID {id}")
    for u in usuario:
        if u['id'] == id:
            logger.info("Usuário encontrado")
            return {'id': u['id'], 'nome': u['nome'], 'email': u['email']}
    raise HTTPException(status_code=404, detail='Usuário não encontrado')

@router.delete('/{id}', response_model=dict)
def delete_usuario(id: int):
    logger.info(f"Requisição para deletar usuário ID {id}")
    if UsuarioModel.deletar(id) == 0:
        logger.warning(f"Usuário ID {id} não encontrado para deletar")
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return {'message': 'Usuário deletado com sucesso'}

@router.put('/{id}', response_model=dict)
def update_usuario(id: int, usuario: UsuarioUpdate):
    logger.info(f"Requisição para atualizar usuário ID {id}")
    try:
        linhas_afetadas = UsuarioModel.atualizar(
            id, usuario.nome, usuario.email
        )
        if linhas_afetadas == 0:
            # logger.warning(f"Usuário ID {user_id} não encontrado para atualizar")
            raise HTTPException(status_code=404, detail='Usuário não encontrado')
        return {'message': 'Usuário atualizado com sucesso'}
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
