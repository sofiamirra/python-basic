
def read_price(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        prezzi = {} 
        prima = f.readline() # scarta linea d'intestazione
        for line in f:
            campi = line.rstrip('\n').split(',') # definisco campi
            data = campi[0]
            store = campi[2]
            prodotto = campi[3]
            essenziale = campi[4]
            prezzo = float(campi[5])

            if essenziale == 'E': # converto in booleano
                essenziale = 1
            else:
                essenziale = 0
            
            # La struttura è:
            # prezzi = {"Prodotto": {"essential": True, "stores":  {"store": { "data": prezzo, "data": prezzo }}                                       
            # *Dizionario annidato: necessario quando vuoi gestire più negozi e date per lo stesso prodotto.
            # Se il prodotto non esiste ancora nel dizionario principale, lo aggiungo come chiave (*evita KeyError)
            if prodotto not in prezzi:
                prezzi[prodotto] = {
                    'essential': bool(essenziale),
                    'stores': {} # dizionario che conterrà i negozi e i prezzi per data
                }

            # Se il negozio non è ancora presente nel dizionario 'stores' del prodotto, lo aggiungo come chiave (*evita KeyError)
            if store not in prezzi[prodotto]['stores']:
                prezzi[prodotto]['stores'][store] = {}        
            
            prezzi[prodotto]['stores'][store][data] = prezzo # Assegno il prezzo per la data specifica
    return prezzi
    #     "Apple": {
            #         "essential": True,
            #         "stores": {
            #             "Coop": { "2025-08-31": 6.59, "2025-09-01": 6.79 },
            #             "Sobeys": { "2025-08-31": 6.99 }
            #         }
            #     },
            #     ...

def read_shops(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        shops = []
        for line in f:
            campi = line.rstrip('\n') # non devo separare nulla, evito split
            shops.append(campi)
    return shops

def main():
    prezzi = read_price('NLFoodPricing.txt')
    shops = read_shops('shops.txt')
    
    ## Elenco dei prodotti essenziali
    essenziali = []
    for prodotto in sorted(prezzi):
        if prezzi[prodotto]['essential']:
            essenziali.append(prodotto)
    print("Prodotti:\n", '\n'.join(essenziali))


    ## Per ogni negozio e prodotto essenziale indica prezzo minimo
    for store in sorted(shops): # solo dal file shops
        print('\n', store)
        for prodotto in sorted(essenziali): # solo prodotti essenziali
            if store in prezzi[prodotto]['stores']:  # controllo se il prodotto è venduto in quel negozio
                storico = prezzi[prodotto]['stores'][store].values() # ottengo tutti i prezzi disponibili per quel negozio              
                minimo = min(storico)
                print(f'{prodotto}: {minimo} $/kg')
                 
    ## Parte interattiva: l'utente chiede il prezzo minimo di un prodotto
    domanda = str(input('Che cibo vuoi cercare? (q per smettere): '))
    while domanda != 'q':
        if domanda in essenziali: # se il prodotto è negli esseziali
            minimo = 30
            store_min = None
            # ciclo su tutti i negozi in cui il prodotto è venduto
            for store in prezzi[domanda]['stores']:
                prezzo = min(prezzi[domanda]['stores'][store].values()) # calcola il prezzo minimo tra tutte le date disponibili per quel negozio. 
                # Output: dict_values([6.59, 6.79])
                if prezzo < minimo: # confronto per trovare il minimo assoluto
                    minimo = prezzo
                    store_min = store
            print(f'Prezzo minimo: {minimo} $/kg da {store_min}')
        else:
            print("Prodotto non trovato o non essenziale.")
        domanda = str(input('Che cibo vuoi cercare? (q per smettere): '))

if __name__ == '__main__':
    main()
