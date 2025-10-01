## AIFinance API
Essa API foi feita para um  app AI-First App para gestão financeira. Na API, podemos dar um input para na rota **/api/create_expense** e do prompt, ele irá extrair seu gasto e sua respectiva categoria. Nessa API É usado algumas regras para evitar o uso de Prompt Injection.

Funcionalidades principais:
   - Registro de despesas e receitas.
   - Armazenamento seguro no banco PostgreSQL.
   - API REST com FastAPI e Uvicorn.
   - Configuração completa via Docker Compose.

## **Como rodar?**

### 1. Requisitos
   - Docker ≥ 20.x
   - Docker Compose ≥ 1.29.x
   - Python ≥ 3.11 (para desenvolvimento local)

### 2. Arquivo .env
   - Crie um arquivo .env direto na pasta raíz, junto ao docker-compose.yml, nesse arquivo terá:
   ```bash
   OPENAI_API_KEY= Sua chave API da OpenAI
   ```
### 3. Arquivo .env.postgresql
   - Crie um arquivo .env.postgresql para ter os parâmetros para se conectar ao banco de dados PostgreSQL, junto ao docker-compose.yml.
   ```bash
    DB_HOST=
    DB_PORT=
    DB_USER=
    DB_PASSWORD=
    DB_NAME=
   ```

### 3. Build e start dos containers
  Na terminal, na raíz do projeto, execute:
  ```bash
  docker-compose up --build
  ```
  Isso fará:
   - Criara e iniciará o container finance_api

## 4. Acessando a API
   - A API estará disponível em: http://localhost:8000
   - A documentação automática do FastAPI (Swagger) pode ser acessada em: http://localhost:8000/docs
   
## 5. Parar os containers
   - Para parar e remover os containers, redes e volumes criados pelo Compose:
   ```bash
docker-compose down
   ```
## 6. Observações importantes
   - Toda vez que você alterar o código da API e quiser atualizar a imagem, use docker-compose up --build novamente.
   - Certifique-se de que o arquivo .env contenha sua chave OpenAI válida.
   - O banco PostgreSQL está exposto na porta 5432 para conexão local, se necessário.
