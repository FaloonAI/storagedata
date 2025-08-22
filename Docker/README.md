# Команды:
```bash
mkdir my_project && cd my_project
docker compose up -d --build
```
# Структура:
my_project/
├── docker-compose.yml
├── app/
│   ├── Dockerfile
│   └── app.py


# Ответ на вопросы:
- Почему нет "python app.py", "python -r requirements.txt"?
  - Все команды прописаны в Dockerfile
- Что используется?
  - Flask (Python API) — бэкенд
  - Postgres — база данных
  - Adminer — веб-интерфейс для работы с БД

# Содержание Docker-файлов:

## docker-compose.yml
```yml
version: "3.8"

services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - pg_data:/var/lib/postgresql/data

  adminer:
    image: adminer
    restart: always
    ports:
      - "8080:8080"

  web:
    build: ./app
    restart: always
    ports:
      - "5000:5000"
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    depends_on:
      - db

volumes:
  pg_data:
```


## Dockerfile
```
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```