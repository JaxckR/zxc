# Backend обучающего peer to peer сайта

Перед началом пользования приложением нужно переименовать jwt_certs/private-mock.pem в private.pem и jwt_certs/public-mock.pem в public.pem.<br>
Это стоит делать лишь в среде разработки! В продашкене стоит самостоятельно генерировать ключи

## Быстрый старт

### Предустановки
- Python 3.12
- Docker
- Postgres
<br>

### С использованием docker
1. Необходимо любым удобным Вам способом скопировать данный проект к себе на устройство
2. Заполните .env.dist файл своими данными(либо используйте mock-данные) и переименуйте в .env
```dotenv
POSTGRES_USER=eduUser
POSTGRES_PASSWORD=eduPassword
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=eduDB

REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

JWT_ALGORITHM=RS256
JWT_ACCESS_MINUTES_EXPIRES=15
JWT_REFRESH_DAYS_EXPIRES=30
```
3. Используйте docker для быстрого запуска приложения
```bash
docker compose up
```

### Без использования докер

Перед всеми пунктами Вам нужно будет создать базу данных postgres

1. Необходимо любым удобным Вам способом скопировать данный проект к себе на устройство
2. Заполните .env.dist файл своими данными(либо используйте mock-данные) и переименуйте в .env
```dotenv
POSTGRES_USER=eduUser
POSTGRES_PASSWORD=eduPassword
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=eduDB

REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

JWT_ALGORITHM=RS256
JWT_ACCESS_MINUTES_EXPIRES=15
JWT_REFRESH_DAYS_EXPIRES=30
```
3. Установите все зависимости
```bash
pip install uv
uv sync
```
4. Примените все миграции
```bash
alembic upgrade head
```
5. Запустите приложение
```bash
uv run uvicorn edu.main:get_app --factory
```

**Примечание** <br> 
Если вы работаете на windows и хотите запустить без использования docker, 
то приложение обязательно запускать через main.py файл. 