FROM python:3.8

WORKDIR /app/
COPY data/ ./data/
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
CMD python3 app.py & celery -A app.celery worker --loglevel=info
