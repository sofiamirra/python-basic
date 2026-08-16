def read_scores(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        prima = f.readline() # scarto
        partite = {} # {'giocatore': [ [sfidante, punteggio], [sfidante, punteggio] ] }
        giocatori1 = set()
        giocatori2 = set()
        for line in f:
            campi = line.rstrip('\n').split(';')
            giocatore1 = campi[7]
            giocatore2 = campi[8]
            punteggio = campi[16]
            giocatori1.add(giocatore1)
            giocatori2.add(giocatore2)
            if giocatore1 not in partite:
                partite[giocatore1] = []
            if giocatore2 not in partite:
                partite[giocatore2] = []
            partite[giocatore1].append([giocatore1, giocatore2, punteggio])
            partite[giocatore2].append([giocatore1, giocatore2, punteggio])

        giocatori = giocatori1.union(giocatori2)
    return giocatori, partite

def main():
    giocatori, partite = read_scores('tennis.txt')

    # I giocatori devono essere stampati in ordine alfabetico uno per riga;
    lista_giocatori = []
    for giocatore in giocatori:
        lista_giocatori.append(giocatore)
    lista_giocatori.sort()
    for i in range(len(lista_giocatori)):
        print(f'{i+1}. {lista_giocatori[i]}')

    # Selezionare un giocatore tra quelli che hanno partecipato al torneo. 
    selezione = int(input('\nScegli un giocatore: '))
    print('\n')

    # Visualizzare i dati (avversario e punteggio) di tutti i match del tennista scelto.
    for giocatore, lista_partite in partite.items():
        if giocatore == lista_giocatori[selezione-1]:
            for element in lista_partite:
                giocatore1 = element[0]
                giocatore2 = element[1]
                score = element[2]
                print(f'{giocatore1} vs. {giocatore2} {score}')

main()