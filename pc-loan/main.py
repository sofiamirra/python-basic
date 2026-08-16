def read_registrazioni(nome_file):
    registrazioni = {}
    with open(nome_file, 'r', encoding='UTF-8') as f:
        for line in f:
            campi = line.rstrip('\n').split(':')
            id = campi[0]
            persona = int(campi[1])
            data = campi[2]
            
            ## Struttura dizionario registrazioni = {'id': {'data': persona}}
            # [id] rappresenta l'ID di ciascun PC
            # {'data' : persona} associa la matricola alla data del prestito
            # ogni PC può avere più prestiti in giorni diversi: serve una struttura 
            # che memorizzi più record per ciascun PC senza sovrascrivere dati precedenti.

            if id not in registrazioni:  # se l'ID non è ancora registrato lo inizializzo come chiave
                registrazioni[id] = {}            
            registrazioni[id][data] = persona # associo la matricola alla data del prestito
    return registrazioni

def read_PC(nome_file):
    pc = []
    with open(nome_file, 'r', encoding='UTF-8') as f:
        for line in f:
            campi = line.rstrip('\n')
            pc.append(campi)
    return pc

def main():
    # Legge i file di input
    registrazioni = read_registrazioni('registrazioni.txt')
    pc = read_PC('parcoPC.txt')

    ## Conto quante occorrenze per ciascuna coppia id, matricola [se prestito è attivo]
    from collections import Counter
    conteggio = Counter()  # per contare quante volte un PC è stato preso in prestito da una matricola
    for id in registrazioni: # per ogni azione registrata
        if id in pc: #  verifico che l'id del pc sia tra quelli aziendali
            matricole = registrazioni[id].values()  # lista di matricole che hanno preso in prestito un pc
            for matricola in matricole: 
                conteggio[(id, matricola)] += 1 # incremento di 1 il conteggio della coppia (PC, matricola)
            # Alla fine, conteggio conterrà la frequenza con cui ogni PC è stato preso da ogni matricola.
        #    conteggio = Counter({
        #    ('PC1', 123): 2,
        #    ('PC2', 456): 1    })


    ## Stampa prestiti attivi
    prestiti = {}  # creo dizionario: chiave = matricola, valore = [lista dei PC attualmente in prestito]
    for (id, matricola), count in conteggio.items():  # itero su ogni coppia (PC, matricola) e il suo conteggio 
    # for chiave, valore in conteggio.items() → restituisce sia la chiave che il valore, così puoi usare count correttamente.
        if count == 1:  # considero solo prestiti attivi 
            if matricola not in prestiti:  # se la matricola non ha ancora una lista, la creo (dizionario annidato)
                prestiti[matricola] = []
            prestiti[matricola].append(id)  # aggiungo il PC alla lista dei prestiti attivi della matricola
    
    print("Elenco dei prestiti in corso:")
    for matricola in sorted(prestiti):  
        lista = sorted(prestiti[matricola]) # ridefinisco la lista prestiti[matricola] per ordinarla
        print(f"{matricola}: {', '.join(lista)}")  

    # PC disponibili
    disponibili = [] # lista che conterrà gli ID dei PC non attualmente in prestito
    for id in sorted(pc): # Ciclo su tutti i PC del parco, ordinati alfabeticamente
        in_prestito = False # flag che indica se il PC è già in prestito
        for lista in prestiti.values(): # Ciclo su tutte le liste di PC in prestito (valori del dizionario prestiti)
            if id in lista:  # controllo se il PC corrente è in una delle liste
                in_prestito = True # il PC è in prestito
                break  # esco dal ciclo perché non serve controllare le altre matricole
        if not in_prestito:
            disponibili.append(id) # lo aggiungo alla lista dei PC disponibili
    print(f"\nPC disponibili per il prestito: {', '.join(disponibili)}")

main()
