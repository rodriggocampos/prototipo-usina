# API de Monitoramento de Usinas Fotovoltaicas

Este projeto consiste em uma API desenvolvida com **FastAPI** para o monitoramento de usinas fotovoltaicas. Ela oferece endpoints para manipulação de dados sobre **usinas**, **inversores** e **métricas**. O banco de dados utilizado é o **SQLite**, e o **SQLAlchemy** é empregado para a comunicação entre a API e o banco de dados.

## Estrutura do Projeto

A estrutura do código foi organizada de forma modular para garantir a clareza e a manutenção facilitada do projeto. A seguir está uma explicação de como o código foi organizado:

>├── app/  
>│ ├── init.py # Inicializa a aplicação FastAPI  
>│ ├── main.py # Arquivo principal da aplicação, onde a FastAPI é instanciada  
>│ ├── models/ # Contém os modelos de dados (SQLAlchemy)  
>│ │ ├── init.py  
>│ │ ├── usina.py # Modelo para dados de usina  
>│ │ ├── inversor.py # Modelo para dados de inversores  
>│ │ └── metricas.py # Modelo para dados de métricas  
>│ ├── schemas/ # Contém os esquemas de dados (pydantic)  
>│ │ ├── init.py  
>│ │ ├── usina.py # Esquema para validação de dados de usina  
>│ │ ├── inversor.py # Esquema para validação de dados de inversores  
>│ │ └── metricas.py # Esquema para validação de dados de métricas  
>│ ├── crud/ # Operações CRUD (Create, Read, Update, Delete)  
>│ │ ├── init.py  
>│ │ ├── usina.py # CRUD para usinas  
>│ │ ├── inversor.py # CRUD para inversores  
>│ │ └── metricas.py # CRUD para métricas  
>│ └── database.py # Configuração do banco de dados (SQLAlchemy)  
>├── requirements.txt # Dependências do projeto  
>└── README.md # Este arquivo  


### Descrição das pastas e arquivos

- **`app/main.py`**: Arquivo principal da aplicação, onde a instância do FastAPI é criada e as rotas são incluídas.
- **`app/models/`**: Contém os modelos de dados que representam as tabelas no banco de dados.
- **`app/schemas/`**: Contém os esquemas do Pydantic, usados para validar e estruturar os dados de entrada e saída.
- **`app/crud/`**: Contém as operações CRUD (Create, Read, Update, Delete) específicas para cada entidade (usinas, inversores e métricas).
- **`app/database.py`**: Configura o banco de dados e o SQLAlchemy para interação com o SQLite.
- **`requirements.txt`**: Lista todas as dependências do projeto.

## Como Rodar o Projeto

### Pré-requisitos

- **Python 3.7+**
- **pip** para instalar pacotes Python

### Passos para executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rodriggocampos/prototipo-usina.git
   cd prototipo-usina

2. **Crie um ambiente virtual (opcional, mas recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use: venv\Scripts\activate
    
3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt

4. **Execute o aplicação:**
    ```bash
    uvicorn app.main:app --reload

5. **Em outro terminal rode os seguintes comandos para inserir usinas e inversores e importar as métricas:**
    ```bash
    python -m scripts.init_db
    python scripts/import_metrics.py

## Estrutura Técnica

### Backend
- **Framework:** FastAPI
- **Banco de Dados:** SQLite
- **ORM:** SQLAlchemy

---

### Rotas RESTful

- `GET /api/v1/usinas`  
- `POST /api/v1/usinas`  
- `PUT /api/v1/usinas/{id}`  
- `DELETE /api/v1/usinas/{id}`  
  > CRUD completo para **usinas**

- `GET /api/v1/inversores`  
- `POST /api/v1/inversores`  
- `PUT /api/v1/inversores/{id}`  
- `DELETE /api/v1/inversores/{id}`  
  > CRUD completo para **inversores**

- `GET /api/v1/metricas/`  
  > Métricas agregadas por usina ou inversor, com funcionalidades como:  
  - Cálculo da **potência máxima**  
  - Cálculo da **temperatura média**  
  - Cálculo de **geração de energia** (via agregação)

---

### Funcionalidades CRUD

- **Usinas**
  - Criar, listar, buscar por ID, atualizar e remover
- **Inversores**
  - Vinculados a uma usina, com operações CRUD completas
- **Métricas**
  - Podem ser consultadas por inversor ou usina
  - Filtros por intervalo de tempo disponíveis
