import math

def calcola_perimetro():
    print("Di quale figura vuoi calcolare il perimetro?")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")
    
    scelta= input ("Digita il numero della figura che hai scelto:")
    
    if scelta == "1":
        lato = float (input("Inserisci la misura del lato del quadrato:"))
        perimetro = lato* 4
        print(f"Il perimetro del quadrato che abbiamo calcolato è: {perimetro:.2f}")
        
    elif scelta == "2":
        raggio = float(input("Inserisci la misura del raggio del cerchio:"))
        perimetro = 2 * math.pi * raggio
        print(f"La circonferenza del cerchio che abbiamo calcolato è: {perimetro:.2f}") 
      
    elif scelta == "3":
        base = float(input("Inserisci la misura della base del rettangolo:"))
        altezza = float (input("Inserisci la misura dell'altezza del rettangolo"))
        perimetro = float (base*2 + altezza*2)
        print(f"Il perimetro del rettangolo che abbiamo calcolato è: {perimetro:.2f}")       

    else:
        print("Questa scelta non è valida. Inserisci un valore numerico e riprova.")
    
if __name__ == "__main__":
    calcola_perimetro()    
