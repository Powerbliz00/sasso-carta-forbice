import random  # libreria per generare numeri casuali
# variabile per il restart del gioco
restart = True

# funzione per stampare cornici ASCII
def stampa_cornice(messaggio):
    lunghezza = len(messaggio) + 4
    print("+" + "-" * lunghezza + "+")
    print("|  " + messaggio + "  |")
    print("+" + "-" * lunghezza + "+")

# funzione per iniziare la partita
def inizia_partita():
    print("SASSO, CARTA, FORBICI!")
    print("Scegli un’opzione: ")
    print("1. Sasso")
    print("2. Carta")
    print("3. Forbici")

    while True:  # ciclo per garantire un input valido
        try:
            # scelta del giocatore
            scelta_giocatore = int(input("Inserisci il numero corrispondente alla tua scelta (1-3): "))
            if scelta_giocatore not in [1, 2, 3]:  # verifica se la scelta è valida
                raise ValueError("Scelta non valida. Devi inserire 1, 2 o 3.")
            break  # esci dal ciclo se l'input è valido
        except ValueError:
            print("Input non valido. Assicurati di inserire un numero intero tra 1 e 3.")  # messaggio personalizzato

    # scelta del computer automatica con la libreria random e il metodo randint
    scelta_computer = random.randint(1, 3)

    # Condizioni di vittoria, pareggio e perdita
    if scelta_giocatore == scelta_computer:
        stampa_cornice("PAREGGIO!")
    elif scelta_giocatore == 1 and scelta_computer == 2:
        stampa_cornice("HAI PERSO! La carta batte il sasso.")
    elif scelta_giocatore == 1 and scelta_computer == 3:
        stampa_cornice("HAI VINTO! Il sasso batte le forbici.")
    elif scelta_giocatore == 2 and scelta_computer == 1:
        stampa_cornice("HAI VINTO! La carta batte il sasso.")
    elif scelta_giocatore == 2 and scelta_computer == 3:
        stampa_cornice("HAI PERSO! Le forbici battono la carta.")
    elif scelta_giocatore == 3 and scelta_computer == 1:
        stampa_cornice("HAI PERSO! Il sasso batte le forbici.")
    elif scelta_giocatore == 3 and scelta_computer == 2:
        stampa_cornice("HAI VINTO! Le forbici battono la carta.")

    # ciclo di restart del gioco 
    global restart  # dichiarazione della variabile globale
    while True:  # ciclo per garantire un input valido per il restart
        restart = input("Vuoi giocare ancora? (s/n): ").lower()
        if restart in ['s', 'n']:
            break  # esci dal ciclo se l'input è valido
        else:
            print("Input non valido. Devi inserire 's' per sì o 'n' per no.")  # messaggio personalizzato

    # Controllo della risposta per decidere se riavviare il gioco
    if restart == "n":
        stampa_cornice("GRAZIE PER AVER GIOCATO!")
        exit()  # termina il programma
    else:
        inizia_partita()  # riavvia la partita

# Avvio del gioco
inizia_partita()
