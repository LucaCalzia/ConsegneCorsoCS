

def cifrario_di_cesare(stringa):
    #scegli l'alfabero
    inp = input("Che alfabeto vuoi scegliere per cifrare, Italiano o Inglese? ")
    if "italiano" in [x.lower() for x in inp.split(" ")]:
        alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "z"]
    else:
        alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    lista = stringa.strip()
    i = 0
    while i<=21:
        is_maiuscola = False
        decifrata = ""
        for lettera in lista:
            is_maiuscola = False
            if lettera.lower() != lettera:
                is_maiuscola = True
                lettera = lettera.lower()


            lettera_decifrata = alfabeto[alfabeto.index(lettera)-i]
            if is_maiuscola:
                decifrata += lettera_decifrata.upper()
            else:
                decifrata += lettera_decifrata
        print(f"Con l'indice {i} la stringa decifrata è: {decifrata}\n")
        i+= 1
    return 

cifrario_di_cesare("HSNFRGH")
    



