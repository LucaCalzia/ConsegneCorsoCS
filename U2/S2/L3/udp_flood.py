# importiamo le librerie necessarie
import socket # per gestire i socket
import random # per generare byte casuali
import ipaddress #per controllare che l'ip inserito abbia un formato valido

try:
    ip_target = input("Inserisci l'IP del target: ").strip() #chiediamo l'IP target
    ipaddress.IPv4Address(ip_target)
    porta_target = int(input("Inserisci la porta UDP target: ")) #chiediamo la porta che ascolta
    if porta_target<1 or porta_target>65535:
        raise ValueError("La porta deve essere compresa tra 1 e 65535.")

    numero_pacchetti = int(input("Quanti pacchetti vuoi inviare? ")) # chiediamo quanti pacchetti vogliamo inviare
    if numero_pacchetti<=0:
        raise ValueError("Il numero di pacchetti deve essere positivo.")

    # Creiamo il socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as mittente: #creiamo un socket con indirizzi IPv4 che usa UDP e gli assegnamo il nome di mittente
        # Ora costruiamo il contenuto del pacchetto da inviare
        pacchetto = random.randbytes(1024) #genera 1024 bytes casuali

        # dato che UDP non ha bisogno di stabilire prima un handshake, possiamo inviare direttamente il pacchetto a destinazione
        for i in range(numero_pacchetti):   #iteriamo tante volte quanti sono i pacchetti da mandare
            mittente.sendto(pacchetto, (ip_target,porta_target))    # inviamo il pacchetto ad indirizzo e porta richiesti
#gestisce gli input non validi 
except ValueError as errore:
    print(f"Errore nei dati inseriti: {errore}")
#gestisce gli errori segnalati dalle operazioni di rete
except OSError as errore:
    print(f"Errore di rete: {errore}")