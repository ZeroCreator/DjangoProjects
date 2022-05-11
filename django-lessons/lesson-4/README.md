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


###5. CRUD - основы ORM по работе с моделями

Рассматриваются базовые операции добавления, чтения, изменения и удаления записей из таблицы БД с использованием ORM-интефрейса Django. Вы у знаете о методе save() и delete(). Менеджере записей objects и его методах: create(), all(), filter(), exclude(), get(). О сортировке записей методом order_by(). О просмотре выполненных SQL-запросов через коллекцию connection.queries. Атрибут pk.

####Операции в терминале:
python manage.py shell
####Подключение класса:
from women.models import Women
####Создание новой записи в таблице БД:
Women(title='Анжелина Джоли', content='Биография Анжелины Джоли')

w1 = _

w1.save()

####Доступ к данным поля через стандартные атрибуты класса:
w1.id

w1.title

w1.time_create

####Атрибут pk (синоним id) - номер текущей записи, по которому устанавливается связь между таблицами:
w1.pk

####Просмотреть SQL-запросы:
from django.db import connection

connection.queries

w2 = Women(title='Энн Хэтэуэй', content='Биография Энн Хэтэуэй')

w2.save()

w3 = Women()

w3.title = 'Джулия Робертс'

w3.content = 'Биография Джулии Робертс'

w3.save()

####Менеджер добавления записи сразу сохраняет в таблицу:
w4 = Women.objects.create(title='Ума Турман', content='Биография Умы Турман')

Women.objects.create(title='Кира Найтли', content='Биография Киры Найтли')

####Чтение данных из таблицы базы данных:
Women.objects.all()

w = _

w[0]

w[0].title

len(w)

for wi in w: print(wi.title)

Women.objects.filter(title='Энн Хэтэуэй')
Women.objects.filter(pk=2)
Women.objects.filter(pk__gte=2) # >=
Women.objects.filter(pk__lte=2) # <=
Women.objects.exclude(pk=2) # !=
Women.objects.get(pk=2) #исключение при отсутствии записи

####Сортировка
Women.objects.filter(pk__lte=4).order_by('title')
Women.objects.filter(pk__lte=4).order_by('-title')
Women.objects.order_by('-time_update')

####Изменение записи в таблице
wu = Women.objects.get(pk=2)

wu.content = 'Биография Марго Робби'

####Удаление записей
wd = Women.objects.filter(pk__gte=4)

wd.delete()








