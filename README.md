# Fproject

Веб-приложение на **Flask** для работы с книгами, пользователями, отзывами и авторизацией.

**Версия:** `v1.0.0`

---

# 🇷🇺 Русский

## О проекте

**Fproject** — веб-приложение на Flask с системой регистрации и авторизации пользователей, каталогом книг, страницами отдельных книг и возможностью оставлять отзывы.

Проект использует:

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* SQLite
* Docker / Docker Compose
* HTML / CSS

---

## Возможности

### 👤 Пользователи

* регистрация;
* вход и выход из аккаунта;
* авторизация пользователей;
* профиль пользователя;
* хранение паролей в хешированном виде.

### 📚 Книги

* просмотр каталога книг;
* просмотр отдельной книги;
* добавление и редактирование книг;
* работа с описанием и информацией о книгах.

### ⭐ Отзывы

* просмотр отзывов;
* добавление отзывов авторизованными пользователями;
* отображение отзывов на страницах книг.

---

## Запуск через Docker

### Требования

Для запуска необходимы:

* Docker
* Docker Compose

Проверить установку:

```bash
docker --version
docker compose version
```

### Клонирование

```bash
git clone https://github.com/durbercelo/Fproject-Flask.git
cd Fproject-Flask
```

### Настройка SECRET_KEY

Приложение использует переменную окружения `SECRET_KEY`.

В production рекомендуется хранить секрет отдельно от исходного кода.

Создайте файл `.env`:

```env
SECRET_KEY=your-secret-key
```

Не добавляйте `.env` в Git.

> В текущей конфигурации `docker-compose.yml` переменная `SECRET_KEY` уже задана через `environment`. Перед публикацией проекта в открытый репозиторий рекомендуется заменить этот вариант на использование `.env` или Docker secrets.

### Запуск

```bash
docker compose up -d --build
```

Проверить контейнер:

```bash
docker compose ps
```

Посмотреть логи:

```bash
docker compose logs -f
```

Приложение внутри контейнера работает на:

```text
0.0.0.0:5000
```

Docker публикует порт на localhost хоста:

```text
127.0.0.1:5000
```

Поэтому приложение доступно локально на сервере по адресу:

```text
http://127.0.0.1:5000
```

Если приложение необходимо открыть из интернета, рекомендуется использовать reverse proxy, например Nginx, перед Flask-приложением.

---

## Обновление приложения

После получения новых изменений:

```bash
git pull
docker compose up -d --build
```

Проверить состояние:

```bash
docker compose ps
```

---

## Остановка

```bash
docker compose down
```

---

## База данных

Проект использует SQLite.

Основная база:

```text
users.db
```

В Docker база подключается через volume:

```yaml
volumes:
  - ./users.db:/opt/app/users.db
```

Это позволяет сохранять данные пользователей и книг независимо от пересоздания контейнера.

**Важно:** файл `users.db` не должен добавляться в GitHub. Он исключён через `.gitignore`.

Перед обновлением проекта рекомендуется создавать резервную копию базы:

```bash
cp users.db users_backup_$(date +%Y%m%d_%H%M%S).db
```

---

## Структура проекта

```text
Fproject-Flask/
├── app.py
├── models.py
├── docker-compose.yml
├── Dockerfile
├── .gitignore
├── users.db
├── static/
│   ├── about.css
│   ├── custom.css
│   ├── index.css
│   └── default.jpg
└── templates/
    ├── about.html
    ├── base.html
    ├── book_detail.html
    ├── book_form.html
    ├── index.html
    ├── login.html
    ├── profile.html
    └── register.html
```

---

## Docker-команды

### Запуск

```bash
docker compose up -d --build
```

### Просмотр контейнеров

```bash
docker compose ps
```

### Логи

```bash
docker compose logs -f flask
```

### Перезапуск

```bash
docker compose restart
```

### Остановка

```bash
docker compose down
```

### Пересборка

```bash
docker compose build --no-cache
docker compose up -d
```

---

## Безопасность

Перед использованием проекта в production рекомендуется:

1. Не хранить `SECRET_KEY` непосредственно в публичном `docker-compose.yml`.
2. Использовать `.env` или Docker secrets.
3. Не публиковать `users.db`.
4. Регулярно создавать резервные копии базы данных.
5. Использовать HTTPS.
6. Размещать Flask за reverse proxy.
7. Не использовать development-сервер Flask как публичный production-сервер.

---

## Версия

Текущая версия:

```text
v1.0.0
```

---

## Лицензия

Лицензия проекта пока не указана.

---

# 🇬🇧 English

## About

**Fproject** is a Flask-based web application with user registration and authentication, a book catalog, individual book pages, and user reviews.

The project uses:

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* SQLite
* Docker / Docker Compose
* HTML / CSS

---

## Features

### 👤 Users

* user registration;
* login and logout;
* user authentication;
* user profiles;
* hashed password storage.

### 📚 Books

* browse the book catalog;
* view individual books;
* add and edit books;
* manage book descriptions and information.

### ⭐ Reviews

* view reviews;
* authenticated users can add reviews;
* reviews are displayed on book pages.

---

## Running with Docker

### Requirements

You need:

* Docker
* Docker Compose

Check your installation:

```bash
docker --version
docker compose version
```

### Clone the repository

```bash
git clone https://github.com/durbercelo/Fproject-Flask.git
cd Fproject-Flask
```

### Configure SECRET_KEY

The application uses the `SECRET_KEY` environment variable.

For production, the secret should be stored outside the source code.

Create a `.env` file:

```env
SECRET_KEY=your-secret-key
```

Do not commit `.env` to Git.

> In the current configuration, `docker-compose.yml` defines `SECRET_KEY` directly under `environment`. Before publishing the project publicly, it is recommended to move the secret to `.env` or use Docker secrets.

### Start the application

```bash
docker compose up -d --build
```

Check the container:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

The Flask application listens inside the container on:

```text
0.0.0.0:5000
```

Docker publishes the port on the host as:

```text
127.0.0.1:5000
```

Therefore, the application is locally available on the server at:

```text
http://127.0.0.1:5000
```

If the application needs to be accessible from the Internet, a reverse proxy such as Nginx should be placed in front of the Flask application.

---

## Updating the application

After pulling new changes:

```bash
git pull
docker compose up -d --build
```

Check the status:

```bash
docker compose ps
```

---

## Stopping

```bash
docker compose down
```

---

## Database

The project uses SQLite.

Main database:

```text
users.db
```

Docker mounts the database using:

```yaml
volumes:
  - ./users.db:/opt/app/users.db
```

This keeps the application data on the host independently of the container lifecycle.

**Important:** `users.db` should not be committed to GitHub. It is excluded through `.gitignore`.

Create a database backup before updating:

```bash
cp users.db users_backup_$(date +%Y%m%d_%H%M%S).db
```

---

## Project structure

```text
Fproject-Flask/
├── app.py
├── models.py
├── docker-compose.yml
├── Dockerfile
├── .gitignore
├── users.db
├── static/
│   ├── about.css
│   ├── custom.css
│   ├── index.css
│   └── default.jpg
└── templates/
    ├── about.html
    ├── base.html
    ├── book_detail.html
    ├── book_form.html
    ├── index.html
    ├── login.html
    ├── profile.html
    └── register.html
```

---

## Docker commands

### Start

```bash
docker compose up -d --build
```

### Check containers

```bash
docker compose ps
```

### View logs

```bash
docker compose logs -f flask
```

### Restart

```bash
docker compose restart
```

### Stop

```bash
docker compose down
```

### Rebuild

```bash
docker compose build --no-cache
docker compose up -d
```

---

## Security

Before using the project in production:

1. Do not store `SECRET_KEY` directly in a public `docker-compose.yml`.
2. Use `.env` or Docker secrets.
3. Do not publish `users.db`.
4. Create regular database backups.
5. Use HTTPS.
6. Run Flask behind a reverse proxy.
7. Do not expose Flask's development server directly to the public Internet.

---

## Version

Current version:

```text
v1.0.0
```

---

## License

No project license has been specified yet.
