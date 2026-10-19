
import datetime

def assistente_virtuale():
    lista_stringa_utente = input("Cosa vuoi sapere? ").lower().strip("?!.,").split()
    match lista_stringa_utente:
        case _ if ( "data" in lista_stringa_utente or "giorno" in lista_stringa_utente) and any(p in lista_stringa_utente for p in ["ora", "ore", "orario"]):
            print(f"Il giorno e l'ora di adesso sono: {datetime.date.today().strftime("%d/%m/%Y")} {datetime.datetime.now().time().strftime("%H:%M")}")
        case _ if "data" in lista_stringa_utente or "giorno" in lista_stringa_utente:
            print(f'La data di oggi è {datetime.date.today().strftime("%d/%m/%Y")}')

        case _ if any(p in lista_stringa_utente for p in ["ora", "ore", "orario"]):
            print(f"L'ora attuale è {datetime.datetime.now().time().strftime("%H:%M")}")

        case _ if "nome" in lista_stringa_utente or "chiami" in lista_stringa_utente or "chi sei" in " ".join(lista_stringa_utente):
            print("Mi chiamo Assistente Virtuale")

        case _ if any(p in lista_stringa_utente for p in ["esci", "termina", "chiudi"]):
            return

        case _:
            print("Non ho capito la domanda.")
            assistente_virtuale()
    return

assistente_virtuale()