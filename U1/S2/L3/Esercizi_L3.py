'''Si scriva un programma in Python che in base alla scelta dellʼutente permetta di calcolare il perimetro di diverse figure geometriche'''
import math 

def calcola_perimetro():
    try:
        figura = input("Inserisci la figura di cui vuoi calcolare il perimetro: ").lower()
        match(figura):
            case "quadrato":
                l = int(input("Inserisci lunghezza del lato: "))
                return l*4
            case "rettangolo":
                b = int(input("Inserisci lunghezza della base: "))
                a = int(input("Inserisci lunghezza dell'altezza: "))
                return (b+a)*2
            case "triangolo":
                a = int(input("Inserisci lunghezza del lato 1: "))
                b = int(input("Inserisci lunghezza del lato 2: "))
                c = int(input("Inserisci lunghezza del lato 3: "))
                return a+b+c
            case "cerchio":
                l = int(input("Inserisci lunghezza del diametro: "))
                return 2*math.pi*l
    except ValueError:
        print("Non hai inserito un intero: ")
        calcola_perimetro()