🚀 Teste Prático - Engenharia de Dados | 10 Pastéis

Este projeto visa automatizar a coleta, tratamento e armazenamento de dados climáticos usando Python, a API OpenWeatherMap e um banco de dados PostgreSQL.

---

📌 Visão Geral
🔹 Coleta de dados climáticos em tempo real da cidade de Curitiba via API OpenWeatherMap.
🔹 Tratamento dos dados coletados (limpeza e padronização).
🔹 Armazenamento dos dados processados no banco PostgreSQL.
🔹 Utilização de variáveis de ambiente para segurança e organização.
🔹 Estrutura clara e organizada para fácil reprodutibilidade.

---

🛠️ Tecnologias Utilizadas
✅ Python 3.x
✅ requests → Requisição da API
✅ pandas → Estruturação dos dados
✅ sqlalchemy → Conexão com o banco
✅ psycopg2-binary → Driver PostgreSQL
✅ dotenv → Gerenciamento de variáveis de ambiente
✅ PostgreSQL 12+

---

## 📁 Estrutura do Projeto
Teste-Pratico-10P/
│── main.py            # Script principal de coleta e salvamento dos dados
│── create_tables.sql  # Script SQL para criação da tabela 'clima'
│── .env               # Arquivo com variáveis de ambiente
│── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto

---

🔑 Pré-requisitos
🔸 Python 3 instalado
🔸 PostgreSQL configurado e rodando localmente
🔸 Conta e chave de API do OpenWeatherMap (Não é necessário pois a chave da API já está no projeto)
🔸 Criar um banco de dados clima_db no PostgreSQL

---

🏗️ Setup do Projeto

1️⃣ Clone o repositório

```bash
git clone https://github.com/briansnack/Teste-Pratico-10P.git
cd Teste-Pratico-10P

2️⃣ Configure um ambiente virtual (opcional, mas recomendado)

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

3️⃣ Instale as dependências

pip install -r requirements.txt

4️⃣ Configure o banco PostgreSQL

# Acesse o PostgreSQL
psql -U postgres

# Crie o banco
CREATE DATABASE clima_db;

# Acesse o banco e crie a tabela
\c clima_db;

CREATE TABLE clima (
    cidade VARCHAR(100),
    temperatura FLOAT,
    umidade INT,
    descricao VARCHAR(255),
    data_coleta TIMESTAMP
);

🚀 Executando o Projeto

# No terminal, execute:

python main.py

📢 Mensagem esperada:
✅ "Dados salvos com sucesso!"

🔍 Para verificar os dados inseridos:
SELECT * FROM clima;

```
---

📊 Decisões Técnicas
✅ API escolhida: OpenWeatherMap pela robustez, gratuidade e excelente documentação.
✅ Tratamento dos dados: Uso do pandas para padronização e futura escalabilidade.
✅ Conexão ao banco: SQLAlchemy, garantindo flexibilidade e segurança.
✅ Variáveis sensíveis armazenadas em .env para evitar exposição (.env visível nesse projeto para facilitar na hora de rodar o projeto e não ser necessária a criação).

📌 Observações
⚠️ O projeto foi desenvolvido para rodar localmente com PostgreSQL.
⚠️ A criação da tabela pode ser feita via script .sql ou manualmente.

🔮 Próximos Passos
🔹 Automatizar coleta diária (cron/apscheduler)
🔹 Armazenar dados históricos de múltiplas cidades
🔹 Criar um painel de visualização interativo com Dash ou Power BI