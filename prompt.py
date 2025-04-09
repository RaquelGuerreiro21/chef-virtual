import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

def gerar_receita(ingredientes):
    prompt = f"""
    Você é um chef de cozinha. Com base nos ingredientes abaixo, crie uma receita completa e detalhada:
    
    Ingredientes: {ingredientes}

    A receita deve conter:
    - Nome do prato
    - Ingredientes necessários
    - Modo de preparo passo a passo
    - Tempo estimado de preparo

    Seja criativo, mas mantenha coerência com os ingredientes informados.
    """

    body = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(url, headers={"Content-Type": "application/json"}, json=body)
    data = response.json()

    try:
        return data['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"Ocorreu um erro: {e}\nResposta da API: {data}"
