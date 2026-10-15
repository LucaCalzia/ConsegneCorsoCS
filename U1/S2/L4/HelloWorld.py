import os
from google import genai

# Legge la chiave API dalla variabile d'ambiente.
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise SystemExit("Imposta prima la variabile GEMINI_API_KEY.")

# Crea il client per comunicare con Gemini.
client = genai.Client(api_key=api_key)

# Invia un prompt e riceve una risposta.
response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Ciao Gemini! Presentati."
)

# Stampa il testo della risposta.
print(response.text)