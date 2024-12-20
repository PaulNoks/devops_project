# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

RUN pip install pytest
# Указываем порт и запускаем приложение
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]
