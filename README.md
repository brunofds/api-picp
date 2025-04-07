# API PicPay (api-picp)

API desenvolvida com **FastAPI** para gerenciar usuários, incluindo funcionalidades como criação, listagem e validação de e-mails duplicados. Este projeto utiliza **Docker** e **Docker Compose** para facilitar a configuração e execução do ambiente.

---

## **Funcionalidades**
- **Adicionar Usuário**: Cria um novo usuário com nome e e-mail.
- **Listar Usuários**: Retorna uma lista de todos os usuários cadastrados.
- **Buscar Usuário por ID**: Retorna os dados de um usuário específico.
- **Validação de E-mail**: Impede a criação de usuários com e-mails duplicados.

---

## **Pré-requisitos**
Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## **Configurações Necessárias**
1. **Estrutura do Projeto**:
   Certifique-se de que o projeto está organizado da seguinte forma: