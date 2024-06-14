import math

def calcola_perimetro_area():
    figure_disponibili = {"1": "Quadrato", "2": "Cerchio", "3": "Rettangolo"}
    valore_precedente = 0  # Memorizza il valore dell'area della figura calcolata precedentemente

    while figure_disponibili:
        print("\nOpzioni disponibili:")
        for key, figura in figure_disponibili.items(): #Richiamo figure disponibili nel dizionario
            print(key + ". " + figura)
        print("4. Esci dal programma")

        scelta = input("Scegli un'opzione inserendo il numero corrispondente o '4' per uscire: ")

        if scelta in figure_disponibili:
            if scelta == "1":  # Quadrato
                lato = valore_precedente if valore_precedente > 0 else float(input("Inserisci la misura del lato del quadrato: "))
                perimetro = lato * 4
                area = lato ** 2
            elif scelta == "2":  # Cerchio
                raggio = valore_precedente if valore_precedente > 0 else float(input("Inserisci la misura del raggio del cerchio: "))
                perimetro = 2 * math.pi * raggio
                area = math.pi * raggio ** 2
            elif scelta == "3":  # Rettangolo
                base = valore_precedente if valore_precedente > 0 else float(input("Inserisci la misura della base del rettangolo: "))
                altezza = float(input("Inserisci la misura dell'altezza del rettangolo: "))
                perimetro = 2 * (base + altezza)
                area = base * altezza

            print(f"Il perimetro calcolato è: {perimetro:.2f}")
            print(f"L'area calcolata è: {area:.2f}")
            valore_precedente = area  # Aggiorna il valore precedente con l'area appena calcolata
            del figure_disponibili[scelta]  # Rimuovi la figura calcolata

        elif scelta == "4":
            print("Grazie per aver usato il nostro programma! Alla prossima.")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    calcola_perimetro_area()
