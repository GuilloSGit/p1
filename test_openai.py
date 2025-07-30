# test_openai.py
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY", None)
if not openai.api_key:
    raise RuntimeError("No se cargó OPENAI_API_KEY")

resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Hola desde test"}]
)
print(resp.choices[0].message.content)
