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
```bash

├── app
│   ├── app.log
│   ├── controller
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   └── usuario_controller.py
│   ├── database
│   │   ├── init_db.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── database.db
│   ├── logs
│   │   └── app.log
│   ├── main.py
│   ├── model
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── usuario_model.py
│   │   └── usuario_schema.py
│   ├── __pycache__
│   │   ├── main.cpython-310.pyc
│   │   └── main.cpython-311.pyc
│   └── tests
│       ├── conftest.py
│       ├── __init__.py
│       ├── __pycache__
│       ├── test_usuario_api.py
│       └── test_usuario_model.py
├── database.db
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
└──  tree.txt
```

2. **Banco de Dados**:
O banco de dados SQLite será inicializado automaticamente ao executar o projeto. Certifique-se de que o arquivo `init_db.py` está configurado corretamente para criar as tabelas necessárias.

---

## **Instalação e Execução**

### **1. Clonar o Repositório**
Clone o repositório para sua máquina local:
```bash
git clone https://github.com/brunofds/api-picp.git
cd api-picp
```

### **2. Construir a Imagem Docker**
Construa a imagem Docker do projeto:
```bash
docker compose build
```

### **3. Executar o Projeto**
Inicie o ambiente com o Docker Compose:
```bash
docker compose up fastapi-dev
```
O servidor estará disponível em: [http://localhost:8000](http://localhost:8000)

### **4. Testar a API**
Acesse a documentação interativa da API gerada automaticamente pelo FastAPI:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## **Comandos Úteis**

### **Parar os Contêineres**
Para parar os contêineres em execução:
```bash
docker compose down
```

### **Recriar os Contêineres**
Se houver alterações no código ou na configuração, recrie os contêineres:
```bash
docker compose up --build
```

---

## **Tecnologias Utilizadas**
- **FastAPI**: Framework para construção de APIs rápidas e eficientes.
- **SQLite**: Banco de dados leve e integrado.
- **Docker**: Para containerização do ambiente.
- **Docker Compose**: Para orquestração dos contêineres.

---

## **Contribuição**
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
