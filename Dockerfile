# 1. Используем официальный образ Python
FROM python:3.13-slim

# 2. Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# 3. Устанавливаем переменные окружения, чтобы Python выводил все сразу в лог
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 4. Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем весь код проекта в рабочую директорию
COPY . .