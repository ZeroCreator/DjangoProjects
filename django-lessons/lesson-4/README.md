###4. Определение моделей. Миграции: создание и выполнение

Что такое модели (Model), как объявлять. Класс models.Model, а также классы для полей таблиц: CharField, TextField, ImageField, DateTimeField, BooleanField. Рассматриваются параметры: max_length, blank, upload_to, auto_now_add, auto_now и default. Рассказывается о настройке приложения для загрузки файлов: константы MEDIA_ROOT и MEDIA_URL. 
Создание и запуск миграций приложения. Команды:
- создание миграций: python manage.py makemigrations
- просмотр SQL-запроса: python manage.py sqlmigrate women 0001
- выполнение миграций: python manage.py migrate

####Команды для миграций:
python manage.py makemigrations
####Посмотреть SQL-запрос:
python manage.py sqlmigrate women 0001
####Создание таблицы в базе данных:
python manage.py migrate