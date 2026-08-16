def read_clienti(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        clienti = {}
        for line in f:
            campi = line.rstrip('\n').split(',')
            cliente = campi[0]
            task = campi[1]
            tempo = int(campi[2])
            ora = int(campi[3])
            clienti[cliente] = {'operazione': task,
                                'arrivo': ora,
                                'durata': tempo}
    return clienti

def read_task(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        sportelli = {}
        for line in f:
            campi = line.rstrip('\n').split(',')    
            sportello = campi[0]
            task1 = campi[1]  
            task2 = campi[2]
            chiusura = campi[3]
            sportelli[sportello] = {'operazioni supportate': [], 
                                    'chiusura': chiusura}
            sportelli[sportello]['operazioni supportate'].append(task1)
            sportelli[sportello]['operazioni supportate'].append(task2)
    return sportelli

# Se più sportelli sono liberi, assegna il cliente al primo sportello in ordine numerico.
# Se tutti gli sportelli che possono supportare il task del cliente sono occupati, 
# stampare un messaggio indicando che il cliente non può essere servito.

def main():
    sportelli = read_task('sportelli.txt')
    clienti = read_clienti('clienti.txt')

    ## Creo un dizionario che indica per ogni cliente quali sportelli possono supportare la sua operazione
    possibilita = {}  # {cliente: [sportelli compatibili]}
    for cliente in clienti:
        for sportello in sportelli:
            if cliente not in possibilita:
                possibilita[cliente] = []
            if clienti[cliente]['operazione'] in sportelli[sportello]['operazioni supportate']:
                possibilita[cliente].append(sportello)
            
    ## Dizionario che conterrà le assegnazioni effettive: sportello -> lista di prenotazioni
    # Ogni prenotazione è un dizionario con 'inizio', 'fine' e 'cliente'
    assegnazioni = {}  # {sportello: [ {'inizio': ..., 'fine': ..., 'cliente': ...} ]}

    # Ciclo su tutti i clienti per assegnarli a uno sportello libero
    for cliente, lista_sportelli in possibilita.items():
        inizio = clienti[cliente]['arrivo']
        fine = inizio + clienti[cliente]['durata']
        cliente_assegnato = False  # flag per sapere se il cliente è stato servito

        for sportello in lista_sportelli:  # controlliamo solo sportelli compatibili
            if sportello not in assegnazioni:
                assegnazioni[sportello] = [] # inizializzo lista vuota per le prenotazioni

            # controlla se lo sportello è libero in quell'intervallo
            libero = True
            for prenotazione in assegnazioni[sportello]: # dizionario di sportello per la prenotazione
                if not (fine <= prenotazione['inizio'] or inizio >= prenotazione['fine']):
                    libero = False  # se l'intervallo del cliente si sovrappone con una prenotazione esistente, non è libero
                    break # basta trovare una sovrapposizione per considerarlo occupato
            
            # controlla anche se lo sportello chiude prima che il cliente finisca
            if libero and fine <= int(sportelli[sportello]['chiusura']):
                # assegno il cliente allo sportello
                assegnazioni[sportello].append({
                    "inizio": inizio,
                    "fine": fine,
                    "cliente": cliente
                })
                cliente_assegnato = True # cliente servito
                print(f"{cliente}. Arrivo: {inizio}. Uscita: {fine}. Sportello: {sportello}")
                break  # cliente assegnato, passo al prossimo

        if not cliente_assegnato:
            print(f"{cliente} non può essere servito/a. Tutti gli sportelli occupati o chiusi.")

main()