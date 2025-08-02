# DEsafio OP2B

Este projeto é uma API usando FastAPI.

## Configuração do Ambiente
para executar os comandos descritos aqui primeiramente deve se estar neste diretório
```bash
cd desafio
```

### 1. Criar ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual

**Linux/MacOS:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

## Executando a Aplicação

### Rodar o servidor de desenvolvimento:

```bash
python main.py
```

### Rodar o servidor via Docker compose:

```bash
docker-compose up --build
```


A aplicação estará disponível em:
- http://localhost:8000
- Documentação interativa: http://localhost:8000/docs
- Documentação alternativa: http://localhost:8000/redoc


## Executando testes unitários

em seu terminal execute o seguinte comando:


```bash
python -m unittest discover -s tests 
```


## Estrutura do Projeto

```
seu_diretorio/
├── desafio/
|  ├── core/           # Configurações centrais
|  ├── services/       # funções criticas da regra de negocio
|  ├── schemas/        # Schemas Pydantic
|  ├── api/            # Rotas da API
|  ├── tests/            # Testes unitários da API
|  └── main.py         # Ponto de entrada
├── requirements.txt   # Dependências do projeto
├── .env.exemple       # Variáveis de ambiente
└── README.md          # Documentação do projeto
```