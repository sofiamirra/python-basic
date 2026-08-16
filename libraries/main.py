## Funzione per leggere l'inventario originale dal file
def read_inventario(nome_file):
    libri = {}
    # Dizionario principale: chiave = codice copia, valore = dizionario con ISBN, titolo e autore
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        for line in f:
            campi = line.rstrip('\n').split(';')
            libri[campi[0]] = {'isbn': campi[1],
                               'titolo': campi[2],
                               'autore': campi[3]
                               }
    return libri

def main():
    libri = read_inventario('inventarioOld.txt')

    ## Creo un dizionario che conti quante copie ci sono per ogni ISBN
    # Dizionario: chiave = ISBN, valore = numero di copie presenti
    conteggio_isbn = {} 
    for codice in libri: # Per ogni copia fisica in biblioteca
        isbn = libri[codice]['isbn']  # Prendo l'ISBN della copia
        if isbn in conteggio_isbn: # Se l'ISBN che analizzo c'è già, incremento il counter
            conteggio_isbn[isbn] += 1 # Inserisce come valore nel dizionario l'intero che rappresenta il numero di copie
        else:
            conteggio_isbn[isbn] = 1 # Altrimenti lascio invariato

    ## Creo un dizionario in cui inserisco gli ISBN con almeno tre copie
    # Dizionario: chiave = ISBN, valore = lista di tutti i codici copia
    almenoTre = {}
    for isbn in conteggio_isbn: # Per ogni ISBN in inventario
        if conteggio_isbn[isbn] > 3: # Se il suo valore associato è un intero maggiore di 3
            codici = [] # Creo una lista dei codici copia corrispondenti a questo ISBN
            for codice in libri: # Per ogni copia fisica in biblioteca
                if libri[codice]['isbn'] == isbn: # se il suo ISBN è uguale a uno di quelli dei libri con almeno tre copie
                    codici.append(codice) # memorizzo il codice nella lista
            almenoTre[isbn] = codici # memorizzo la lista di codici copia come valore del dizionario

    ## Scrittura file inventarioScuola
    with open('inventarioScuola.txt', 'w', encoding = 'UTF-8') as f: # apro in scrittura
        for isbn in sorted(almenoTre):  # ordino alfabeticamente per ISBN
            codici = almenoTre[isbn] # lista di tutti i codici copia per quell'ISBN
            regalare = codici[3:] # seleziono solo le copie dalla quarta in poi
            if regalare: 
                primo_codice = codici[0] # le copie dello stesso ISBN hanno stesso titolo e autore (lo prendo una sola volta)
                titolo = libri[primo_codice]['titolo']
                autore = libri[primo_codice]['autore']
                f.write(f'{isbn};{autore};{titolo};{";".join(regalare)} \n') # regalare è una lista di codici
                
   ## Creo un insieme di tutte le copie regalate
   # set = struttura dati ottimale per verificare rapidamente se un elemento è presente
    codici_regalati = set()
    for codici in almenoTre.values(): # liste di codici copia per ogni ISBN
        codici_regalati.update(codici[3:])  # aggiungo tutte le copie in eccesso

    ## Creo un dizionario dei libri rimanenti
    # Dizionario: chiave = ISBN, valore = lista dei codici copia rimasti
    isbn_to_codici_rimanenti = {}
    for codice in libri:  # Ciclo su tutte le copie fisiche in biblioteva
        if codice not in codici_regalati: # Se la copia non è stata regalata ne estraggo i dati
            isbn = libri[codice]['isbn']     
            titolo = libri[codice]['titolo']
            autore = libri[codice]['autore']
            if isbn not in isbn_to_codici_rimanenti: # Se è la prima volta che incontro l'ISBN 
                isbn_to_codici_rimanenti[isbn] = [] # Inizializzo come valori una lista che conterrà i codici
            isbn_to_codici_rimanenti[isbn].append(codice) # Appendo il codice alla lista dei valori del dizionario

    ## Scrivo file inventarioNew.txt
    with open('inventarioNew.txt', 'w', encoding='UTF-8') as f:
        for isbn in sorted(isbn_to_codici_rimanenti): # Per ogni ISBN di quelli rimasti
            codici = isbn_to_codici_rimanenti[isbn] # lista di codici per quell'ISBN
            primo_codice = codici[0] # prendo titolo e autore dalla prima copia
            titolo = libri[primo_codice]['titolo']
            autore = libri[primo_codice]['autore']
            f.write(f'{isbn};{autore};{titolo};{";".join(codici)}\n')

if __name__ == '__main__':
    main()
