from google import genai
from dotenv import load_dotenv
import os

# .env file load karega
load_dotenv()

# API key read karega
api_key = os.getenv("GEMINI_API_KEY")

print("API Key:", api_key)

# Gemini client
client = genai.Client(api_key=api_key)

# AI se response lo
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Reply only with: Gemini Connected Successfully"
)

print(response.text)