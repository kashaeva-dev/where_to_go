# Интерактивная карта Москвы

Этот проект представляет собой интерактивную карту Москвы, на которой пользователи могут просматривать различные виды
активного отдыха с подробными описаниями и комментариями. 
![img.png](readme_images/img_7.png)

Возможные активности добавляются администратором вручную через удобный интерфейс.

## Установка при развертывании проекта локально

Для установки проекта, выполните следующие шаги:

1. Склонируйте репозиторий:
```bash
git clone https://github.com/ваш-пользователь/ваш-репозиторий.git
```
2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv env
source env/bin/activate
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Примените миграции:
```bash
python manage.py migrate
```
5. Заполните базу данных тестовыми данными:
```
python manage.py loaddata fixtures/place_fixture.json
python manage.py loaddata fixtures/image_fixture.json
```
6. Создайте файл .env и заполните в нем следующие переменные:
```
SECRET_KEY=<YOUR SECRET KEY>
ALLOWED_HOSTS=127.0.0.1
DEBUG=True
CSRF_COOKIE_SECURE=False
SESSION_COOKIE_SECURE=False
SECURE_SSL_REDIRECT=False
SECURE_HSTS_SECONDS=''
SECURE_HSTS_INCLUDE_SUBDOMAINS=False
SECURE_HSTS_PRELOAD=False
SECURE_CONTENT_TYPE_NOSNIFF=False
```

## Использование

### Если Вы развернули проект локально

Запустите сервер разработки:
```bash
python manage.py runserver
```
Откройте браузер и перейдите по адресу http://localhost:8000/ для просмотра интерактивной карты Москвы.
Чтобы добавить или изменить локации, 
Вам необходимо перейти в интерфейс администратора по ссылке: http://localhost:8000/admin.

Перед импользованием интерфейса администратора нужно создать суперпользователя. Для этого выполните команду:
```bash
python manage.py createsuperuser
```
Вас попросят ввести имя пользователя, адрес электронной почты и пароль для нового суперпользователя.
Запомните эти данные, так как они понадобятся для входа в админку.

### Если Вы хотите использовать опубликованную версию

Перейдите по ссылке , чтобы посмотреть, как работает интерактивная карта.
Чтобы добавить или изменить локации, Вам необходимо перейти в интерфейс администратора по ссылке:

**Чтобы использовать интерфейс администратора в опубликованной версии у Вас должен быть логин и пароль для входа.**

**Интерфейс администратора позволяет:**

1. Просмотреть список локаций и найти локацию по названию (поиск чувствителен к регистру).
    ![img_1.png](readme_images/img_1.png)
2. Перейти на страницу редактирования локации и для каждой локации:
   - Обновить текстовки
   ![img_2.png](readme_images/img_2.png)
   - Залить новые картинки и удалить старые
   ![img_3.png](readme_images/img_3.png)
   - Выбрать самые яркие картинки и переместить их в начало списка, чтобы изменить порядок их отображения на сайте.
   ![img_5.png](readme_images/img_5.png)
   3. Добавить новые локации или удалить старые
   ![img6.png](readme_images/img_6.png)


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
