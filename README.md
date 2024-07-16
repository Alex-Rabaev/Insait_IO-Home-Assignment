# Insait IO Home Assignment

This project is a simple Flask server that exposes an endpoint to ask a question. The server sends the question to the OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database. The server and the database are dockerized and run with Docker Compose. The project also includes tests using pytest.

## Project Structure
```plaintext
Insait_IO-Home-Assignment/
├── backend/
│ ├── app/
│ │ ├── models/
│ │ │ └── __init__.py
│ │ │ └── question_answer.py
│ │ ├── routes/
│ │ │ └── api/
│ │ │ │ └── __init__.py
│ │ │ │ └── questions.py
│ │ │ └── __init__.py
│ │ └── services/
│ │ │ └── __init__.py
│ │ │ └── openai_service.py
│ │ └── __init__.py
│ ├── migrations/
│ │ └── ... (Alembic migration files)
│ ├── tests/
│ │ └── __init__.py
│ │ └── test_routes.py
│ ├── .env
│ ├── .env.example
│ ├── alembic.ini
│ ├── config.py
│ ├── database.py
│ └── run.py
├── .env
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── docker-compose.yml
└── requirements.txt
```

## Prerequisites

- Docker
- Docker Compose
- Python 3.10

## Setup

1. Clone the repository:

```sh
git clone https://github.com/Alex-Rabaev/Insait_IO-Home-Assignment.git
cd insait_io-home-assignment
```

2. Create two `.env` files.

    1. **First in the `backend` directory** with the following content:
        ```bash
        DATABASE_URL=postgresql+psycopg2://<POSTGRES_USER>:<POSTGRES_PASSWORD>@db:5432/<POSTGRES_DB>
        TEST_DATABASE_URL=postgresql+psycopg2://<POSTGRES_USER>:<POSTGRES_PASSWORD>@localhost:5432/test
        OPENAI_API_KEY='YOUR_OPENAI_API_KEY'
        ```
        Replace `YOUR_OPENAI_API_KEY`, `<POSTGRES_USER>`, `<POSTGRES_PASSWORD>`, and `<POSTGRES_DB>` with your actual values.

    2. **Second in the main directory** (where `docker-compose.yml` is located) with the following content:
        ```bash
        POSTGRES_USER='YOUR_POSTGRES_USER'
        POSTGRES_PASSWORD='YOUR_POSTGRES_PASSWORD'
        POSTGRES_DB='YOUR_POSTGRES_DB'
        ```
        Replace `YOUR_POSTGRES_USER`, `YOUR_POSTGRES_PASSWORD`, and `YOUR_POSTGRES_DB` with your actual values.

3. Build and run the Docker containers:

```sh
docker-compose up --build
```
This will set up the PostgreSQL database, apply Alembic migrations, and start the Flask server.

## Endpoints
**Ask a Question**
- **URL: `/api/questions/ask`**
- **Method: `POST`**
- **Request Body:**
```json
{
  "question": "What is the capital of France?"
}
```
- **Response:**
```json
{
  "id": 1,
  "question": "What is the capital of France?",
  "answer": "Paris is the capital of France."
}
```
**Get All Questions and Answers**
- **URL: `/api/questions/`**
- **Method: `GET`**
- **Response:**
```json
[
  {
    "id": 1,
    "question": "What is the capital of France?",
    "answer": "Paris is the capital of France."
  }
]
```
**Get Question and Answer by ID**
- **URL: `/api/questions/{id}`**
- **Method: `GET`**
- **Response:**
```json
{
  "id": 1,
  "question": "What is the capital of France?",
  "answer": "Paris is the capital of France."
}
```
**Delete Question and Answer by ID**
- **URL: `/api/questions/{id}`**
- **Method: `DELETE`**
- **Response:**
```json
{
  "message": "Question deleted successfully"
}
```
## Running Tests
To run the tests, use the following command:
```sh
pytest
```
This will run all the tests in the backend/tests directory. The database container must be running when this command is executed.
