import requests
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_ID = "text-davinci-002"

def generate_funny_book_name(book_name):
    prompt = (
        "Generate a funny name for book titled "
        + book_name
        + "."
    )
    payload = {
        "prompt": prompt,
        "model": "text-davinci-003",
        "temperature": 0.7,
        "max_tokens": 256,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    response = requests.post(
        "https://api.openai.com/v1/completions",
        json=payload,
        headers=headers,
    )
    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["text"].strip()
    else:
        print("Error generating book name:", response.text)
