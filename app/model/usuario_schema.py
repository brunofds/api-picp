from pydantic import BaseModel, EmailStr
from typing import Optional



class Usuario(BaseModel):
    """
        Modelo Pydantic para representar os dados do usuário
    """
    nome: str
    email: EmailStr


# Modelo Pydantic para representar os dados do usuário
class UsuarioOut(Usuario):
    """
    Represents the output model for a user.
    Attributes:
        id (int): The unique identifier of the user.
        nome (str): The name of the user.
    """
    id: int



class UsuarioUpdate(BaseModel):
    """
    Modelo Pydantic para atualizar os dados do usuário
    Attributes:
        nome (Optional[str]): The name of the user.
        email (Optional[EmailStr]): The email of the user.
        senha (Optional[str]): The password of the user.
    """
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
