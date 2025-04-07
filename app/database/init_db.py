from model.usuario_model import UsuarioModel
# Aqui importa outros modelos no guruto


def init_db():
    UsuarioModel.criar_tabela()
    # Adicionar outros modelos aqui conforme forem sendo criados
