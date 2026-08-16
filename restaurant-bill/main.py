from operator import itemgetter

def read_menu(nome_file):
    menu = {}
    with open(nome_file, 'r', encoding='UTF-8') as f:
        for line in f:
            campi = line.rstrip('\n').split(',')
            id = campi[0]

            menu[id] = {'descrizione': campi[1],
                        'costo': float(campi[2]),
                        'iva':  int(campi[3])
            }
    return menu

def read_ordine(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        ordine = {}
        for line in f:
            campi = line.rstrip('\n').split(',')
            id = campi[0]
            ordine[id] = {'quantita': int(campi[1])}
    return ordine

def main():
    menu = read_menu('menu.txt')
    ordine = read_ordine('ordine.txt')
    
    print('RICEVUTA')
    totale = 0
    iva = 0
    prodotti = []
    for id in ordine:
        if id in menu:
            qta = ordine[id]['quantita']
            descrizione = menu[id]['descrizione']
            iva_unit = menu[id]['iva']
            prezzo = (ordine[id]['quantita'] * menu[id]['costo'])
            # Calcolo IVA unitaria e totale
            iva_prodotto = (prezzo * (menu[id]['iva']/100)) / (1 + (menu[id]['iva']/100))
            totale += prezzo            
            iva += iva_prodotto
            prodotti.append((id, qta, descrizione, prezzo, iva_unit))

    prodotti.sort(key=itemgetter(4)) # per liste e tuple funziona solo con indice

    for prodotto in prodotti:
            print(f"{prodotto[1]} {prodotto[2]:<25} {prodotto[3]:>10.2f} IVA {prodotto[4]:>7.2f}%")
            # f"{valore:>larghezza}"  # allinea a destra
    print(f'Totale: {totale:.2f}€')
    print(f'Di cui IVA: {iva:.2f}€')
    




    


main()