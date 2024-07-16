# Insait IO Home Assignment

This project is a simple Flask server that exposes an endpoint to ask a question. The server sends the question to the OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database. The server and the database are dockerized and run with Docker Compose. The project also includes tests using pytest.

## Project Structure
```plaintext
insait_io-home-assignment/
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── models/
│ │ │ └── init.py
│ │ │ └── question_answer.py
│ │ ├── routes/
│ │ │ └── api/
│ │ │ └── init.py
│ │ │ └── questions.py
│ │ └── services/
│ │ └── init.py
│ │ └── openai_service.py
│ ├── migrations/
│ │ └── ... (Alembic migration files)
│ ├── tests/
│ │ └── init.py
│ │ └── test_routes.py
│ ├── .env
│ ├── .env.example
│ ├── config.py
│ └── run.py
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
└── requirements.txt
```

## Prerequisites

- Docker
- Docker Compose
- Python 3.10

## Setup

1. Clone the repository:

```sh
git clone https://github.com/yourusername/insait_io-home-assignment.git
cd insait_io-home-assignment
```

2. Create a `.env` file in the `backend` directory with the following content:

```bash
DATABASE_URL=postgresql+psycopg2://<POSTGRES_USER>:<POSTGRES_PASSWORD>@<POSTGRES_HOST>:<POSTGRES_PORT>/<POSTGRES_DB>
TEST_DATABASE_URL=postgresql+psycopg2://<POSTGRES_USER>:<POSTGRES_PASSWORD>@localhost:<POSTGRES_PORT>/test
OPENAI_API_KEY='YOUR_OPENAI_API_KEY'
POSTGRES_USER='YOUR_POSTGRES_USER'
POSTGRES_PASSWORD='YOUR_POSTGRES_PASSWORD'
POSTGRES_DB='YOUR_POSTGRES_DB'
POSTGRES_HOST="YOUR_POSTGRES_HOST"
POSTGRES_PORT="YOUR_POSTGRES_PORT"
```
Replace `your_openai_api_key` with your actual OpenAI API key. `POSTGRES_PORT` for `TEST_DATABASE_URL` should be `localhost`.

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
This will run all the tests in the backend/tests directory.