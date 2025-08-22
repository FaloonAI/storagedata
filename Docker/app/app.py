from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host="db"   # имя сервиса Postgres из docker-compose.yml
        )
        conn.close()
        return "✅ Flask подключился к базе данных!"
    except Exception as e:
        return f"❌ Ошибка подключения: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
