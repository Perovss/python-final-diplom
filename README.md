### Начало работы:

   В .env файл вписать название базы данных, юзера, пароль, хост и порт итд.

```
# Postgres settings

POSTGRES_USER=root
POSTGRES_PASSWORD=root
POSTGRES_DB=db

# email settings for mail.ru

EMAIL_HOST=smtp.mail.ru
EMAIL_HOST_USER=username@mail.ru
EMAIL_HOST_PASSWORD=password
EMAIL_PORT=2525
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=username@mail.ru
SERVER_EMAIL=username@mail.ru


SECRET_KEY="#############################################"
```

   Поднять базы данных в докере:

   > docker-compose up -d

   Установить зависимости:

   > pip install -r requirements.txt

   Сделать миграции:

   > python3 manage.py migrate

   Запустить приложение

   > python3 manage.py runserver

### Тестовые запросы для Postman:

https://github.com/Perovss/python-final-diplom/blob/master/postman_scenaries.json

### Для остановки проекта необходимо выполнить:

> docker-compose down -v

