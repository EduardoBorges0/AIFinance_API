import psycopg
import os

def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        user=os.getenv("DB_USER", "myuser"),
        password=os.getenv("DB_PASSWORD", "mypassword"),
        dbname=os.getenv("DB_NAME", "mydb")
    )

conn = get_connection()
cur = conn.cursor()

# Criando tabela users primeiro
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(100)
)
""")

# Criando tabela despesas com chave estrangeira user_id
cur.execute("""
CREATE TABLE IF NOT EXISTS despesas (
    id SERIAL PRIMARY KEY,
    categoria VARCHAR(100),
    valor NUMERIC,
    user_id INT REFERENCES users(id) ON DELETE CASCADE
)
""")

conn.commit()
cur.close()
conn.close()
