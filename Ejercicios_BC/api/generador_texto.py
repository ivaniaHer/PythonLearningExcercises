import requests as req

HEADERS = {
    "Authorization":"Bearer ----",
    "Content-Type": "application/json"
}
API_URL = "https://router.huggingface.co/v1/chat/completions"

payload = {
    "model": "moonshotai/Kimi-K2-Instruct-0905",
    "messages": [
        {
            "role": "user",
            "content": "Tienes el rol de docente, explica lo que es hugging face evitando muchos tecnicismos"
        }
    ],
    "max_tokens":200
}

response = req.post(
    API_URL,
    headers=HEADERS,
    json=payload
)

print("STATUS CODE:", response.status_code)
print("RESPUESTA CRUDA:")
print(response.text)