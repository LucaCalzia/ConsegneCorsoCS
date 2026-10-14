############################################################################# Esercizi Facili##################################################################################

# 1
# Scrivi un programma che chieda all'utente di inserire due numeri e poi calcoli e mostri la loro somma.
def somma():
    try:
        a = int(input("Inserisci il primo numero: "))
        b = int(input("Inserisci il secondo numero: "))
        return a+b
    except ValueError:
        print("Devi inserire due numeri interi !!!")
        somma()

# 2
# Scrivi un programma che chieda all'utente di inserire un numero e determini se è pari o dispari
def pari_o_dispari():
    try:
        a = int(input("Inserisci un numero: "))
        print("Il numero è pari") if a%2==0 else print("Il numero è dispari")
        return
    except ValueError:
        print("Devi inserire un numero intero !!!")
        pari_o_dispari()

# 3
# Scrivi un programma che chieda all'utente di inserire una stringa e poi conti e mostri il numero di caratteri in essa.
def conta_caratteri():
    return len(list(input("Inserisci una stringa: ")))

# 4 
# Scrivi un programma che chieda all'utente di inserire un anno e determini se è bisestile.
def bisestile():
    try:
        anno = int(input("Inserisci un anno: "))
        return True if (anno%4==0 or anno%100==0 or anno%400==0) else False
    except ValueError:
        print("Devi inserire un anno, non una stringa !!!")
        bisestile()

############################################################################# Esercizi Medi##################################################################################
# 1
# Scrivi un programma che chieda all'utente di inserire un numero intero e calcoli il suo fattoriale
def calcola_fattoriale():
    try:
        n = int(input("Inserisci un numero: "))
        j = n-1
        while j>0:
            n = n*j 
            j-=1
        return n
    except ValueError:
        print("Devi inserire un numero intero !!!")
        calcola_fattoriale()

# 2
# Scrivi un programma che chieda all'utente di inserire un numero n e generi i primi n numeri della sequenza di Fibonacci.
def calcola_fibonacci():
    try:
        n = int(input("Inserisci un numero: "))
        j = n-1
        while j>0:
            n = n+j 
            j-=1
        return n
    except ValueError:
        print("Devi inserire un numero intero !!!")
        calcola_fibonacci()

# 3
# Scrivi un programma che chieda all'utente di inserire una stringa e poi la inverta.
def inverti_stringa():
    stringa = list(input("Inserisci una stringa: "))
    lista_invertita = []
    for lettera in stringa:
        lista_invertita.insert(0,lettera)
    return ''.join(lista_invertita)

############################################################################# Esercizi Medi##################################################################################
# 1
# Scrivi un programma che chieda all'utente di inserire una stringa e poi conti le occorrenze di ogni parola in essa.
import re

def conta_occorrenze():
    case_sensitive = input("La stringa deve essere case-sensitive, rispondi con y/n: ").lower()
    if case_sensitive=="y":
        case_sensitive = True
    elif case_sensitive=="n":
        case_sensitive = False
    else:
        print("Inserisci y o n !!!")
        conta_occorrenze()
    if case_sensitive: 
        return conta_occorrenze_CS() 
    else: 
        return conta_occorrenze_CI()
    
    
def conta_occorrenze_CS():
    stringa = re.sub(r"[^\w\s]", "", input("Inserisci una stringa: ")).split(" ")
    dizionario = dict()
    for parola in stringa:
        if parola in dizionario:
            dizionario[parola] += 1
        else:
            dizionario[parola] = 1
    return dizionario

def conta_occorrenze_CI():
    stringa = re.sub(r"[^\w\s]", "", input("Inserisci una stringa: ")).split(" ")
    dizionario = dict()
    for parola in stringa:
        parola = parola.lower()
        if parola in dizionario:
            dizionario[parola] += 1
        else:
            dizionario[parola] = 1
    return dizionario



# 2
# Scrivi un programma che chieda all'utente di inserire una lista di numeri (separati da spazi) e calcoli la media, la mediana e la moda.
def media_mediana_moda():
    try:
        lista = input("Inserisci una lista di numeri: ").split(" ")
        media = sum(int(x) for x in lista)/len(lista)
        lista = [int(x) for x in lista]
        mediana = calcola_mediana(lista)
        moda = calcola_moda(lista)
        print(f'Media: {media}, Mediana: {mediana}, Moda: {moda}')
        return (media,mediana,moda)
    except ValueError:
        print("La lista non è composta da tutti numeri interi")
        media_mediana_moda()

def calcola_mediana(lista):
    lista.sort()
    centro = (len(lista)//2)
    if len(lista)%2==0:
        return sum(lista[centro-1:centro+1])/2
    else:
        return lista[centro]

def calcola_moda(lista):
    dizionario = dict()
    for x in lista:
        if x in dizionario:
            dizionario[x]+=1
        else:
            dizionario[x]=1

    max_count = max(dizionario.values())
    mode = [x[0] for x in dizionario.items() if x[1]==max_count]
    if len(mode)==1:
        return mode[0]
    return mode

