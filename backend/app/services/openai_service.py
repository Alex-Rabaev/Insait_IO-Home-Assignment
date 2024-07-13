import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY


def get_openai_response(question):
    response = openai.Completion.create(
        engine="davinci", prompt=question, max_tokens=150
    )
    return response.choices[0].text.strip()
