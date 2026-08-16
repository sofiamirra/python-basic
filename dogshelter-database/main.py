
def read_dogs(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        prima = f.readline()
        record = {} # dizionario: {Razza: {Livello: [punteggi] }}
        for line in f:
            campi = line.rstrip('\n').split(',')
            razza = campi[2]
            livello = campi[3]
            punteggio = float(campi[4])
            if razza not in record:
                record[razza] = {}
            if livello not in record[razza]:
                record[razza][livello] = []
            record[razza][livello].append(punteggio)
    return record

## Versione Standard        
# def main():
#     record = read_dogs('dogs.txt')
    
#     ## Calcola media punteggi per razza
#     ordine_livelli = ["Beginner", "Intermediate", "Advanced", "Expert"]
#     for razza in record:
#         print(f'\n{razza}')
#         for livello in ordine_livelli: # .items() non permette di ordinare, perciò scorro lista
#             if livello in record[razza]:
#                 lista_punti = record[razza][livello]
#                 somma = sum(lista_punti)
#                 lunghezza = len(lista_punti)
#                 media = somma / lunghezza
#                 print(f'Livello {livello}: media {media:.2f}')
    
#     ## Calcola razza con il punteggio medio più alto per il livello Expert
#     razze = {} # dizionario razze = {razza: media}
#     for razza in record:
#         for livello, lista_punti in record[razza].items():
#             if livello == 'Expert':
#                 somma_e = sum(lista_punti)
#                 lunghezza_e = len(lista_punti)
#                 media_e = somma_e/lunghezza_e
#                 razze[razza] = media_e
    
#     for razza in razze:
#         lista_medie = razze.values()
#         massimo = max(lista_medie)
#         if razze[razza] == massimo:
#             print(f'\nLa razza con il punteggio medio più alto per il livello Expert è: {razza}')
        
# main()


# # VERSIONE con fuzione per calcolo media

def media_livello(record, razza, livello): # prende in input il dizionario, la razza e il livello
    if razza in record and livello in record[razza]:
        lista_punti = record[razza][livello] # Estraggo la lista dei punteggi per quella razza e quel livello
        somma = sum(lista_punti)
        lunghezza = len(lista_punti)
        media = somma / lunghezza
        return media # Restituisco la media

def main():
    record = read_dogs('dogs.txt')

    # Stampa le medie per ogni razza
    ordini_livelli = ["Beginner", "Intermediate", "Advanced", "Expert"]
    for razza in record: # ciclo su tutte le razze presenti
        print(f'\nRazza: {razza}')
        for livello in ordini_livelli: # ciclo sui livelli in ordine fisso
            media = media_livello(record, razza, livello) # calcolo la media con la funzione
            if media: # stampo solo se il livello esiste per quella razza
                print(f'Livello {livello}: media {media:.2f}')

    # Trova la razza migliore per il livello Expert
    razze_expert = {}  # dizionario {razza: media}
    for razza in record:
        media_expert = media_livello(record, razza, "Expert")  # calcolo media livello Expert
        if media_expert: # aggiungo solo se la razza ha cani Expert
            razze_expert[razza] = media_expert

    for razza in razze_expert:
        lista_medie = razze_expert.values()
        massimo = max(lista_medie)
        if razze_expert[razza] == massimo: # Trovo la razza con il valore massimo
            print(f'\nLa razza con il punteggio medio più alto per il livello Expert è: {razza}')

main()
