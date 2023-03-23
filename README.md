### api_yatupe:
Это API для проекта Yatube. В данном API реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

### Технологии:
Python 3.9.10,
Django 3.2.16,
DRF,
JWT + Djoser

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке.

```
git clone git@github.com:Holorid/api_final_yatube.git
```

```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение.

```
python3 -m venv env
```

```
source env/bin/activate
```
Установить зависимости из файла requirements.txt.

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Выполнить миграции.

```
python3 manage.py migrate
```
Запустить проект.

```
python3 manage.py runserver
```

### Примеры
Для неавторизованных пользователей доступен только get запрос.

```
api/v1/posts/ - получение списка всех постов
api/v1/posts/{id}/ - получение поста
api/v1/groups/ - получение списка всех групп
api/v1/groups/{id}/ - получение группы
api/v1/{post_id}/comments/ - получение списка всех комментариев под определенным постом
api/v1/{post_id}/comments/{id}/ - получение комментария
```

За исключением follow. Этот эндпоинт доступен только авторизованным пользователям.

```
api/v1/follow/ - получение подписок текущего пользователя
api/v1/follow/{id}/ - получение одной подписки
```

Авторизаяци проходит по токену.

```
api/v1/jwt/create/ - Получить токен, передав в body: 
{
"username": "your_nickname",
"password": "your_password"
}
api/v1/jwt/refresh/ - Обновление токена
api/v1/jwt/verify/ - Проверка токена
```

### Документация API
Всю документацию можно найти тут http://127.0.0.1:8000/redoc/