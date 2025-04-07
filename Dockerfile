FROM python:3.11-slim

WORKDIR /app
COPY . /app

# Define variáveis de ambiente padrão
ARG ENV=production
ENV ENV=${ENV}
ENV PYTHONPATH=/app/app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
