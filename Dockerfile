FROM python:3.10-slim

WORKDIR /app

COPY backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY backend/ .

RUN alembic upgrade head

CMD ["python", "run.py"]