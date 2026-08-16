def read_passeggeri(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        passeggeri = {} # Passeggeri = {Origine: [eta, eta, eta]}
        ## Dizionario di liste che mantiene tutti i valori facendo calcoli all'interno

        record = {} # Record = {Numero Volo: {'passeggero': sesso}}
        ## Dizionario annidato che permette accesso diretto a ciascun passeggero
        for line in f:            
            campi = line.rstrip('\n').split(',')
            eta = int(campi[1])
            nome = campi[0]
            origine = campi[3]
            volo = campi[5]
            sesso = campi[2]

            # Inserisce l'età nella lista dell'origine corrispondente
            if origine not in passeggeri:
                passeggeri[origine] = []
            passeggeri[origine].append(eta)

            # Inserisce il sesso del passeggero nel record del volo
            if volo not in record:
                record[volo] = {}
            record[volo][nome] = sesso
    return passeggeri, record

def main():
    passeggeri, record = read_passeggeri('passeggeri.txt') # accedo ad entrambe le strutture dati

    ## Calcolare la media delle età dei passeggeri per ciascuna origine
    media = 0.0
    print("Media dell'età per ciascuna origine")
    # Ciclo su ogni origine presente nel dizionario 'passeggeri'
    for origine, lista_eta in passeggeri.items():
        # 'lista_eta' contiene tutte le età dei passeggeri che partono da questa origine
        somma = sum(lista_eta) # Somma tutte le età della lista
        n_pass = len(lista_eta)
        media = somma / n_pass
        print(f"Origine: {origine}, Media età: {media:.1f}")

    ## Stabilire volo più popolare e numero passeggeri maschi e femmine
    a = {} # Dizionario per memorizzare i conteggi per ogni volo
    for volo in sorted(record):
        conto_m = 0
        conto_f = 0
        totale = 0
        # Ciclo su tutti i passeggeri di questo volo
        for nome in record[volo]:
            if record[volo][nome] == 'M':
                conto_m += 1
            elif record[volo][nome] == 'F':
                conto_f += 1
            totale = conto_m + conto_f
            # Memorizza i conteggi nel dizionario 'a' per accesso futuro
            a[volo] = {'maschi': conto_m,
            'femmine': conto_f,
            'totale': totale}

    # Trova il numero massimo di passeggeri su tutti i voli
    lista_totali = []
    for volo in a:
        totale = a[volo]['totale']
        lista_totali.append(totale)
        n = max(lista_totali)

    for volo in a:
        totale = a[volo]['totale']
        maschi = a[volo]['maschi']
        femmine = a[volo]['femmine']
        if totale == n: # Confronta se il record totale è proprio il massimo, allora è il volo più popolare
            print(f'Numero di volo più popolare: {volo}, Passeggeri M: {maschi} / F: {femmine}')

main()