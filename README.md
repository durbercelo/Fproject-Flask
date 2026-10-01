# Fproject

Веб-приложение на Flask с SQLite, регистрацией и авторизацией пользователей, профилями и функционалом работы с книгами.

A Flask web application with SQLite, user registration and authentication, user profiles, and book management functionality.

---

# 🇷🇺 Русская версия

## 🚀 Версия

**v1.0.0**

### Основные изменения

* добавлена поддержка Docker;
* добавлен `docker-compose.yml`;
* обновлена структура проекта;
* HTML-шаблоны перенесены в `templates/`;
* статические файлы перенесены в `static/`;
* обновлены `app.py` и `models.py`;
* добавлены страницы для работы с книгами.

---

## 📋 Требования

Для запуска рекомендуется использовать Docker.

Необходимы:

* Docker
* Docker Compose

Проверить установку:

```bash
docker --version
docker compose version
```

---

## 📥 Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/durbercelo/Fproject-Flask.git
cd Fproject-Flask
```

---

## ⚙️ Конфигурация

Если проект использует переменные окружения, создайте файл `.env` в корневой директории проекта.

> **Важно:** `.env` не должен публиковаться в GitHub. Не храните в репозитории пароли, токены, API-ключи и другие секретные данные.

---

## 🐳 Запуск через Docker

Запустить приложение:

```bash
docker compose up -d --build
```

Проверить состояние контейнеров:

```bash
docker compose ps
```

Посмотреть логи:

```bash
docker compose logs -f
```

Остановить приложение:

```bash
docker compose down
```

---

## 🔄 Обновление

Получить последнюю версию:

```bash
git pull origin main
```

Пересобрать и запустить приложение:

```bash
docker compose up -d --build
```

Проверить состояние:

```bash
docker compose ps
```

---

## 🗄️ База данных

Приложение использует SQLite.

Основная база данных:

```text
users.db
```

При запуске через Docker база данных подключается к контейнеру через `docker-compose.yml`.

> **Важно:** база данных содержит пользовательские данные и не должна публиковаться в публичном Git-репозитории.

Резервные копии базы также не должны добавляться в Git.

---

## 👤 Пользователи

Приложение поддерживает:

* регистрацию;
* авторизацию;
* выход из аккаунта;
* профиль пользователя.

Пароли хранятся в виде хэшей.

---

## 📚 Книги

Приложение поддерживает работу с книгами:

* просмотр списка книг;
* просмотр отдельной книги;
* добавление книги;
* редактирование книги.

Основные шаблоны:

```text
templates/
├── index.html
├── book_detail.html
├── book_form.html
├── login.html
├── register.html
├── profile.html
├── about.html
└── base.html
```

---

## 📁 Структура проекта

```text
Fproject-Flask/
├── app.py
├── models.py
├── create_db.py
├── docker-compose.yml
├── .gitignore
│
├── static/
│   ├── about.css
│   ├── custom.css
│   ├── index.css
│   └── default.jpg
│
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

## 🔧 Запуск без Docker

Для разработки можно запустить приложение напрямую через Python.

Создать виртуальное окружение:

```bash
python3 -m venv venv
```

Активировать его на Linux/macOS:

```bash
source venv/bin/activate
```

На Windows:

```powershell
venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить приложение:

```bash
python3 app.py
```

---

## 🛠️ Полезные команды Docker

Просмотр логов:

```bash
docker compose logs -f
```

Перезапуск:

```bash
docker compose restart
```

Остановка:

```bash
docker compose down
```

Пересборка без кэша:

```bash
docker compose build --no-cache
```

Запуск:

```bash
docker compose up -d
```

Проверка контейнеров:

```bash
docker compose ps
```

---

## 🔒 Безопасность

Не добавляйте в Git:

* `.env`;
* пароли;
* API-ключи;
* токены;
* пользовательские базы данных;
* резервные копии баз данных;
* другие конфиденциальные данные.

Эти файлы исключены через `.gitignore`.

---

## 📌 Релиз

Текущая версия:

**v1.0.0**

Репозиторий:

https://github.com/durbercelo/Fproject-Flask

Для использования конкретного релиза:

```bash
git checkout v1.0.0
```

---

# 🇬🇧 English Version

## 🚀 Version

**v1.0.0**

### Main changes

* added Docker support;
* added `docker-compose.yml`;
* updated project structure;
* moved HTML templates to `templates/`;
* moved static files to `static/`;
* updated `app.py` and `models.py`;
* added book management pages.

---

## 📋 Requirements

Docker is recommended for running the application.

Required:

* Docker
* Docker Compose

Check your installation:

```bash
docker --version
docker compose version
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/durbercelo/Fproject-Flask.git
cd Fproject-Flask
```

---

## ⚙️ Configuration

If the application uses environment variables, create a `.env` file in the project root.

> **Important:** `.env` must not be published to GitHub. Do not store passwords, tokens, API keys, or other secrets in the repository.

---

## 🐳 Running with Docker

Start the application:

```bash
docker compose up -d --build
```

Check container status:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

Stop the application:

```bash
docker compose down
```

---

## 🔄 Updating

Pull the latest version:

```bash
git pull origin main
```

Rebuild and start the application:

```bash
docker compose up -d --build
```

Check the status:

```bash
docker compose ps
```

---

## 🗄️ Database

The application uses SQLite.

Main database:

```text
users.db
```

When running with Docker, the database is mounted into the container through `docker-compose.yml`.

> **Important:** the database contains user data and must not be published to a public Git repository.

Database backups should not be committed to Git either.

---

## 👤 Users

The application supports:

* user registration;
* authentication;
* logout;
* user profiles.

Passwords are stored as hashes.

---

## 📚 Books

The application provides book management functionality:

* browse books;
* view individual books;
* add books;
* edit books.

Main templates:

```text
templates/
├── index.html
├── book_detail.html
├── book_form.html
├── login.html
├── register.html
├── profile.html
├── about.html
└── base.html
```

---

## 📁 Project Structure

```text
Fproject-Flask/
├── app.py
├── models.py
├── create_db.py
├── docker-compose.yml
├── .gitignore
│
├── static/
│   ├── about.css
│   ├── custom.css
│   ├── index.css
│   └── default.jpg
│
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

## 🔧 Running Without Docker

For development, the application can be run directly with Python.

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it on Linux/macOS:

```bash
source venv/bin/activate
```

On Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python3 app.py
```

---

## 🛠️ Useful Docker Commands

View logs:

```bash
docker compose logs -f
```

Restart:

```bash
docker compose restart
```

Stop:

```bash
docker compose down
```

Rebuild without cache:

```bash
docker compose build --no-cache
```

Start:

```bash
docker compose up -d
```

Check containers:

```bash
docker compose ps
```

---

## 🔒 Security

Do not commit the following to Git:

* `.env`;
* passwords;
* API keys;
* tokens;
* user databases;
* database backups;
* other confidential information.

These files are excluded through `.gitignore`.

---

## 📌 Release

Current version:

**v1.0.0**

Repository:

https://github.com/durbercelo/Fproject-Flask

To use a specific release:

```bash
git checkout v1.0.0
```

---

## 📄 License

If the project uses a specific license, add a `LICENSE` file to the repository and specify the license here.
