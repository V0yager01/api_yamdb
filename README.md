# api_yamdb
## Описание проекта
Проект **YaMDb** собирает отзывы пользователей на произведения, которые разделены на категории и жанры. Администраторы могут добавлять новые произведения, категории и жанры. Пользователи могут оставлять свои отзывы, ставить оценки произведениям и комментировать отзывы других пользователей.

## Технологии:
* Python
* Django
* Djangorestframework
* Djangorestframework-simplejwt

## Запуск проекта
- Склонировать репозиторий
```
git clone git@github.com:V0yager01/api_yamdb.git
```
- Перейти в репозиторий в командной строке
```
cd api_yamdb
```
- Cоздать и активировать виртуальное окружение

Для Linux и macOS
```
python3 -m venv venv
```
Для Windows (далее вместо ```python3``` для Windws всегда использовать ```python```)
```
python -m venv venv
```
- Установить зависимости из файла requirements.txt при помощи pip
```
pip install -r requirements.txt
``` 
- Применить миграции
```
python3 yatube_api/manage.py migrate
```
- Запустить проект
```
python3 yatube_api/manage.py runserver
```
## Создание суперпользователя
- В директории с файлом manage.py выполнить команду
```
python3 manage.py createsuperuser
```
- Ввести имя пользователя, **email** и пароль (дважды)

## Регистрация нового пользователя
- Передать **username** и **email** на эндпоинт 127.0.0.1:8000/api/v1/auth/signup/
- Получить код подтверждения на переданный **email**.

Права и ограничения:
- Доступно без токена.
- Запрещено использовать имя 'me' в качестве **username**.
- Поля **email** и **username** должны быть уникальными. 

## Получение JWT-токена
- Передать **username** и **confirmation code** на эндпоинт 127.0.0.1:8000/api/v1/auth/token/ из письма. Доступно без токена.

## Примеры запросов
- Регистрация пользователя  
```
POST /api/v1/auth/signup/
```  
- Получение данных своей учетной записи:  
```
GET /api/v1/users/me/
```  
- Добавление новой категории  
```
POST /api/v1/categories/
```  
- Удаление жанра
```
DELETE /api/v1/genres/{slug}
```  
- Частичное обновление информации о произведении
```
PATCH /api/v1/titles/{titles_id}
```  
- Получение списка всех отзывов
```
GET /api/v1/titles/{title_id}/reviews/
```   
- Добавление комментария к отзыву  
```
POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```  
## Полная документация к API проекта:

Перечень запросов к ресурсу можно посмотреть в описании API

```
http://127.0.0.1:8000/redoc/
```

## Над проектом работали
<br>[Виолетта Сафонова](https://github.com/vioivio)</br>
<br>[Егор Крыльцов](https://github.com/kregm1)</br>
<br>[Ильяс Халиуллин](https://github.com/V0yager01)</br>
