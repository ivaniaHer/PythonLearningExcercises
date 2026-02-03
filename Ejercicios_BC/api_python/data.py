import pandas as pd
from openai import OpenAI

OPENAI_API_KEY = ''
df = pd.read_csv('DatasetComentarios.csv', encoding="utf-8-sig")

client = OpenAI(api_key=OPENAI_API_KEY)

PROMPT_CLASIFICACION = """
Eres un asistente de análisis de datos.
Clasifica el siguiente comentario como: 
POSITIVO, NEGATIVO, NEUTRO U OTRO TIPO

Devuelve únicamente una de esas palabras. 
No agregues explicaciones

comentario:
"""

PROMPT_RESUMEN = "Resume en una frase los principales problemas mencionados"
def clasificar_comentario(texto):
    """
    Esta funcion actua como el conector:
    - Recibe un texto
    - Llama a la API de OpenAI
    - Devuelve la clasificacion que ha solicitado
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role":"user",
                "content":PROMPT_CLASIFICACION + texto
            }
        ],
        temperature=0 # Controla el nivel de creatividad de la IA
    )
    return response.choices[0].message.content.strip()

# procesamiento del archivo csv
df["clasificacion"]=df["comentario"].apply(clasificar_comentario)
print('Testeando clasificaciones')
print(df.head(10))

CATEGORIAS_VALIDAS = ['POSITIVO', 'NEGATIVO', 'NEUTRO']
def validar_clasificacion(valor):
    if valor in CATEGORIAS_VALIDAS:
        return valor
    return "Error"
df["clasificacion"]=df["clasificacion"].apply(validar_clasificacion)
print(df["clasificacion"].value_counts())
negativos=df[df["clasificacion"]=="NEGATIVO"]
print(negativos)

df.to_csv("Clasificacion_comentarios.csv", index=False)

def resumir_comentarios(texto):
    """
    Usar la IA para generar un resumen de los principales problemas
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content":PROMPT_RESUMEN+texto
            }
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
if not negativos.empty:
    texto_negativo = "".join(negativos["comentarios"].tolist())
    resumen = resumir_comentarios(texto_negativo)
    print(resumen)
else:

    print('No hay comentarios negativos')