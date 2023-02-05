# Greetings traveller

Указать в корне проекта данные для подключения к БД (Пример env.example):
.env

Запустить докер и создать контейнер в фоновом режиме:
docker-compose up --build -d

Войти в БД psql и заполнить ее тестовыми данными:
psql -h 127.0.0.1 -U app -d movies_database -f movies_database.ddl

Установить необходимые пакеты для проекта:
pip install -r requirements.txt