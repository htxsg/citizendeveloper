import requests
import os

# Set OpenAI API key
openai_api_key = os.environ["OPENAI_API_KEY"]

# Set the API endpoint and model to use
endpoint = "https://api.openai.com"
model = "text-davinci-003"

# Function to generate text using OpenAI API
def generate_text(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}",
    }
    data = {
        "model": model,
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 1024,
        "n": 1,
        "stop": None,
    }
    response = requests.post(f"{endpoint}/v1/completions", headers=headers, json=data)
    response_json = response.json()
    return response_json["choices"][0]["text"].strip()
