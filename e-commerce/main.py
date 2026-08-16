# - La lista dei nomi dei clienti riportati in ordine alfabetico uno per riga, 
# con il numero totale di ordini effettuati da ciascuno
# -Il nome del cliente con la spesa totale maggiore e il relativo importo totale speso, 
# visualizzato con due cifre decimali. 
# -Il nome del prodotto con meno unità vendute. 

# Numero di ordini di ciascun cliente:
# - Bianchi Luca: 1
# - Neri Sara: 1
# - Rossi Mario: 2
# - Verdi Anna: 2

# Cliente con la spesa totale maggiore:
# - Rossi Mario, con un totale di 1259.95 euro.

# Prodotto meno venduto:
# - Laptop, con 1 unità vendute.

def read_ordini(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        prima = f.readline()
        ordini = {} # {cliente: [ {'ordine': id, 'prodotto': p, 'quantita' = N, 'prezzo_u' = 18] }
        for line in f:
            campi = line.rstrip('\n').split(',')
            cliente = campi[4]

            if cliente not in ordini:
                ordini[cliente] = []
            ordini[cliente].append({'ordine': int(campi[0]),
                                    'prodotto': campi[1],
                                    'quantita': int(campi[2]),
                                    'prezzo_u': float(campi[3])})
    return ordini

def main():
    ordini = read_ordini('ordini.txt')

    conteggio = {} # cliente: [ordine, ordine]
    for cliente in ordini:
        if cliente not in conteggio:
            conteggio[cliente] = []
        for ordine in ordini[cliente]:
            numero = ordine['ordine']
            conteggio[cliente].append(numero)

    print('Numero di ordini di ciascun cliente: ')
    for cliente, lista_ordini in sorted(conteggio.items()):
        numero = len(lista_ordini)
        print(f'- {cliente}: {numero}')

    spesa = {} # cliente: [costo*q, costo*q]
    for cliente in ordini:
        if cliente not in spesa:
            spesa[cliente] = []
        for acquisto in ordini[cliente]:
            prezzo = acquisto['prezzo_u'] * acquisto['quantita']
            spesa[cliente].append(prezzo)

        totale = sum(spesa[cliente])
        spesa[cliente].append(totale)

    # Step 2: sostituire la lista con il totale
    for cliente in spesa:   
        spesa[cliente] = sum(spesa[cliente])
        lista_costi = list(spesa.values())
    massimo = max(lista_costi)
    
    print('\n')
    print('Cliente con la spesa totale maggiore: ')
    for cliente in spesa:
        if spesa[cliente] == massimo:
            print(f' - {cliente} con un totale di {massimo} euro')


    prodotti = {} # prodotto: [1 1 1]
    for cliente in ordini:
        for shopping in ordini[cliente]:
            prodotto = shopping['prodotto']
            quantita = shopping['quantita']
            if prodotto not in prodotti:
                prodotti[prodotto] = []
            prodotti[prodotto].append(quantita)

    for prodotto, lista_quantita in prodotti.items():
        prodotti[prodotto] = sum(lista_quantita)
        lista_quantita = prodotti.values()
    minimo = min(lista_quantita)

    print('\n')
    print('Prodotto meno venduto: ')
    for prodotto in prodotti:
        if prodotti[prodotto] == minimo:
            print(f' - {prodotto} con {minimo} unità vendute')






    # print(lista_costi)

 

    







main()


