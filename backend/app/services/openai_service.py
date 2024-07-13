from openai import OpenAI
from config import Config


client = OpenAI(
    api_key = Config.OPENAI_API_KEY
)


def get_openai_response(question):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
        ],
    )

    openai_response = completion.choices[0].message.content

    return openai_response
