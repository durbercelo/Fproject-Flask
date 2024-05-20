FROM python:3.9.19-slim-bullseye
RUN pip3 install Flask-Login
RUN pip3 install Flask-SQLAlchemy
Copy . /opt/app
Workdir /opt/app
Cmd ["python", "./app.py"]