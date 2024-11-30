# Django проект с документацией API

Этот Django проект содержит документацию API с использованием drf-yasg для Swagger UI и Redoc.

## Установка

1. Клонируйте репозиторий
2. Установите необходимые зависимости с помощью
   `pip install -r requirements.txt`
3. Выполните миграции с помощью

``` bash
python manage.py makemigrations
python manage.py migrate
```

3. Создайте суперпользователя с помощью

``` bash
python manage.py createsuperuser
```

4. Запустите сервер с помощью

``` bash
python manage.py runserver
```

## Использование

Для доступа к документации API:

- Swagger UI: http://localhost:8000/swagger/
- Redoc: http://localhost:8000/redoc/

## URL Пути

- `/admin/`: Панель администратора Django
- `/operators/`: Просмотр списка операторов(`OperatorList` APIView)
    - `GET`: Получение списка операторов
    - `POST`: Добавление новых операторов из файла
- `/operators/operator_table/`: Просмотр таблицы операторов (`OperatorTableView` View)
    - `GET`: Отображение таблицы операторов
- `/swagger/`: Swagger UI для документации API
- `/redoc/`: Redoc для документации API
- `/`: Перенаправляет на `/operators/operator_table/`

