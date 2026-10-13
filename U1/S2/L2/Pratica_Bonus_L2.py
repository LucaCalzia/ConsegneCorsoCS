# Esercizio 1
''' Descrizione: Scrivi una funzione che calcoli la media mobile di una lista di numeri. La media mobile di un elemento è definita come la media degli ultimi
 n elementi della lista, inclusi l'elemento corrente. '''

def media_mobile(lista, n):
    j = 0
    nuova_lista = []
    for i in range(0,len(lista)):
        sottolista = lista[:i+1]
        if len(sottolista) > n: 
            j+=1
            sottolista = lista[j:i+1]
        media = sum(sottolista)/len(sottolista)
        nuova_lista.append(int(media)) if media.is_integer() else nuova_lista.append(round(media,1))
    return nuova_lista
        

print(media_mobile( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

# Esercizio 2
'''Scrivi una funzione che analizzi una stringa di testo e restituisca un dizionario con il conteggio delle occorrenze di ciascuna parola.
Ignora la punteggiatura e considera le parole in modo case-insensitive.'''

import re 

def analisi_parole(stringa):
    dizionario = dict()
    testo_pulito = re.sub(r"[^\w\s]", "", stringa)
    for parola in testo_pulito.split(" "):
        parola_insensitive = parola.lower()
        if parola_insensitive in dizionario:
            dizionario[parola_insensitive] +=1
        else:
            dizionario[parola_insensitive] = 1
    return dizionario

print(analisi_parole("Ciao, ciao! Come stai? Stai bene?"))