import os
from google import genai
from google.genai import types

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise SystemExit("Imposta prima la variabile GEMINI_API_KEY.")

client = genai.Client(api_key=api_key)

# Il system prompt definisce il comportamento dell'assistente.
system_prompt = """
Sei Security Assistant, un assistente di sicurezza informatica.
Rispondi in italiano, in modo chiaro e adatto a un principiante.

Aiuta a comprendere reti, Linux, Python, vulnerabilità,
protezione dei sistemi e analisi dei log.

Quando proponi comandi, spiega cosa fanno.
Per le esercitazioni pratiche, usa sistemi propri o laboratori
per i quali è stata concessa autorizzazione.
Se mancano informazioni, chiedi chiarimenti.
Non inventare risultati di scansioni o controlli mai eseguiti.
"""

# Crea una conversazione che mantiene la cronologia in memoria.
chat = client.chats.create(
    model="gemini-flash-latest",
    config=types.GenerateContentConfig(
        system_instruction=system_prompt
    )
)

print("Security Assistant avviato.")
print("Scrivi 'esci' per terminare.\n")

while True:
    try:
        messaggio = input("Tu: ").strip()

        if messaggio.lower() in ("esci", "exit", "quit"):
            print("Conversazione terminata.")
            break

        if not messaggio:
            continue

        risposta = chat.send_message(messaggio)

        print("\nAssistant:", risposta.text or "Nessuna risposta testuale.")
        print()

    except (KeyboardInterrupt, EOFError):
        print("\nConversazione terminata.")
        break

    except Exception as errore:
        print(f"\nErrore nella richiesta: {errore}\n")