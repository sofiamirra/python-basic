## Funzione per leggere il file degli esami
# Ogni riga del file è del tipo: matricola, data, corso, voto
# Restituisce una lista di liste, dove ogni sottolista contiene i campi della riga
## Ogni riga rappresenta un evento, è importante mantenere la struttura cronologica
# i dati sono “eventi” multipli, l’ordine conta, ci possono essere ripetizioni → perfetta la lista.

def read_esami(nome_file):
    esami = []
    with open(nome_file, 'r', encoding = 'UTF-8') as f: # Apre il file in modo sicuro e lo chiude in automatico
        for line in f:
            campi = line.rstrip('\n').split(',')
            esami.append(campi)
    return esami

## Funzione per leggere il file dei CFU
# Ogni riga del file è del tipo: codice,crediti,obbligatorio
# Restituisce un dizionario dove la chiave è il codice dell'esame
# e il valore è un altro dizionario con crediti e obbligatorietà
## Gli esami sono univoci: dizionario utile per accedere velocemente
# ai dati di un corso conoscendone il codice

def read_cfu(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        cfu = {} # Dizionario vuoto per memorizzare i dati dei corsi
        for line in f:
            campi = line.rstrip('\n').split(',') # Restituisce una lista contenente i campi della riga
            cfu[campi[0]] = { # Imposta chiave dizionario
                'crediti': int(campi[1]), 
                'obbligatorio': bool(int(campi[2])) # Fare prima int, poi bool
            } # Imposta valori associati dizionario
    return cfu

# NOTA SULLA SCELTA DI NON RINOMINARE SUBITO I CAMPI:
# - Durante la lettura dei file non ha molto senso assegnare nomi come 'matricola', 'voto', 'data' o 'esame' 
#   subito dentro le funzioni read_esami() / read_cfu(), perché quelle variabili avrebbero senso 
#   solo dentro la funzione e poi verrebbero perse.
# - Conviene invece restituire strutture generiche (liste o dizionari) e rinominare i campi 
#   direttamente nella main() quando servono. 
#   In questo modo evitiamo di fare il lavoro due volte e abbiamo i nomi parlanti (matricola, voto, ecc.) 
#   proprio nel punto in cui li utilizziamo davvero.

def main():
    esami = read_esami('esami.log.txt')  # Lista di tutti gli esami registrati
    cfu = read_cfu('cfu.dati.txt')  # Dizionario con info su CFU e obbligatorietà

    # Crea un dizionario vuoto che conterrà tutti gli studenti.
    # Struttura: chiave = matricola, valore = dizionario degli esami di quello studente.
    studenti = dict() 
    
    # Ciclo sugli esami per costruire il dizionario degli studenti
    for esame in esami: # Per ogni sottolista di esami (per ogni registrazione incontrata)
        matricola = esame[0]
        codice = esame[2]
        voto = esame[3]
        # Ignoriamo gli esami non superati ('A' = assente, 'R' = respinto)
        if voto != 'A' and voto != 'R':
            # Se la matricola non è ancora presente, viene aggiunta come nuova chiave al dizionario già esistente
            if matricola not in studenti:
                studenti[matricola] = dict()
            # Aggiorniamo il voto dell'esame: sempre l'ultimo superato
            studenti[matricola][codice] = voto # Nel dizionario le chiavi sono uniche: il nuovo valore sovrascrive il precedente

    # Ciclo per calcolare media, CFU totali e obbligatori per ogni studente
    for matricola in studenti: # Per ogni studente del dizionario
        tot_crediti = 0
        tot_crediti_obbligatori = 0
        media = 0.0
        print(f'Media di {matricola}: ')

    ## Alternativa: for studente in studenti (scorre tutte le chiavi del dizionario, ovvero le matricole)
    # for codice in studenti[studente]:
    #       voto = studenti[studente][codice]

        for codice in studenti[matricola]: # Scorre tutti i codici degli esami di quello studente
            crediti = cfu[codice]['crediti'] # Otteniamo i crediti dal dizionario CFU
            obbligatorio = cfu[codice]['obbligatorio'] # Otteniamo se il corso è obbligatorio
            voto = studenti[matricola][codice] # Otteniamo il voto dallo studente
            if voto == '30L':
                voto = 33
            else: 
                voto = int(voto)

            tot_crediti += crediti 
            if obbligatorio: # Genera problemi se non ben convertito nella riga 29
                tot_crediti_obbligatori += crediti
            media = media + voto*crediti
        media = media / tot_crediti
        print(f'CFU totali {tot_crediti}, CFU obbligatori {tot_crediti_obbligatori}, Media: {media:.2f}')
        if tot_crediti >= 30 and tot_crediti_obbligatori >= 10:
            print('Ammissibile')
        else: 
            print('Non ammissibile')
             
if __name__ == "__main__":
    main()
