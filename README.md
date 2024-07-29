# Тестовое задание для ХайТек Плант
Тестовое задание для ХайТек Плант - веб-приложение для пользователей
## Описание задания

Создать веб-приложение c использованием фреймворка Django.
Приложение должны быть авторизованы следующие функции:
- авторизация/регистрация через адрес электронной почты+пароль с подтверждением адреса электронной почты
- страница со списком пользователей
- страница профиля пользователя
- страница редактирования профиля
- сброс пароля
- изменение пароля
- изменение адреса электронной почты

Дополнительные требования:
- Данное веб-приложение должно иметь возможность запуска через docker-compose на Windows/Linux/MacOS
- При разработке необходимо использовать СУБД Postgres.

## Технологии
* Сервис реализован на Django
* Используются django шаблоны
* Используется библиотека django-all-auth для авторизации пользователей
* Реализована регистрация через адрес электронной почты+пароль с подтверждением адреса электронной почты
* Python версии 3.11
* База данных - PostgreSQL
* Проект разворачивается с помощью docker compose
* Релизован pre-commit - при коммите код проверяется линтером и автоматически исправляются ошибки

#№ Локальный запуск: Docker Compose

1. Клонируйте репозиторий с GitHub переменные окружения уже находятся в корневой папке проекта для удобства:

```bash
git clone git@github.com:LoG1s7/test-task-hightech-plant.git && \
cd test-task-hightech-plant&& \
```
2. Создайте файл ".env" в папке "test-task-hightech-plant". Пример наполнения в файле ".env.example"
```bash
cd test-task-hightech-plant && touch .env
```
3. Из корневой директории проекта выполните команду:
```bash
sudo docker compose -f infra/docker-compose.yml up -d --build
```
  Проект будет развернут в трех docker-контейнерах (db, web, nginx) по адресу http://localhost/.

4. Чтобы выполнить миграции выполните команду:
```bash
sudo docker compose -f infra/docker-compose.yaml exec web python manage.py migrate
```
5. Чтобы собрать статические файлы выполните команду:
```bash
sudo docker compose -f infra/docker-compose.yaml exec web python manage.py collectstatic --no-input
```
6. Чтобы создать суперюзера выполните команду и следуйте инструкции:
```bash
sudo docker compose -f infra/docker-compose.yaml exec web python manage.py createsuperuser
```
7. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
sudo docker compose -f infra/docker-compose.yml down
```
  Если также необходимо удалить том базы данных:
```bash
docker compose -f infra/docker-compose.yml down -v
```
#### Админ-панель Django
```bash
http://localhost/admin
```
#### Url проекта
```bash
- http://localhost/accounts/login/ — Вход в систему
- http://localhost/accounts/signup/ — Регистрация
- http://localhost/accounts/logout/ — Выход из системы
- http://localhost/accounts/password/reset/ — Сброс пароля
- http://localhost/accounts/password/change/ — Изменение пароля
- http://localhost/ - список зарегистрированных пользователей
- http://localhost/accounts/profile/{uuid}/ — Страница профиля пользователя
- http://localhost/accounts/profile/edit/ — Редактирование профиля
```
## Автор
[Aleksandr Kolesnikov](https://github.com/log1s7)
