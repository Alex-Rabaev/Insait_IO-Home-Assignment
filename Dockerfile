FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY backend/ .

# for runing Alembic migrations before starting the app
CMD ["sh", "-c", "alembic upgrade head && python run.py"]