
import string
def read_personaggi(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        personaggi = []
        for line in f:
            campi = line.rstrip('\n')
            personaggi.append(campi)
    return personaggi

def read_favola(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        parole = [] 
        for line in f:
            campi = line.rstrip('\n').split(' ')
            for parola in campi: # pulisco ogni parola
                parola = parola.strip(string.punctuation).upper() 
                parole.append(parola)
    return parole

def main():
    personaggi = read_personaggi('personaggi.txt')
    parole = read_favola('favola.txt')

    # Stampa nome personaggio ed occorrenze
    occorrenze = {} # dizionario: {'personaggio': [parola, parola, parola]}
    for personaggio in personaggi:
        if personaggio not in occorrenze:
            occorrenze[personaggio] = []
        for parola in parole:
            if parola == personaggio:
                occorrenze[personaggio].append(parola)

    for personaggio, lista_occorrenze in sorted(occorrenze.items()):
        if lista_occorrenze:
            occ = len(lista_occorrenze)
            print(f'{personaggio}: {occ} occorrenze')
    
    # Stampa personaggio più e meno occorrente
    max_occ = 0
    min_occ = None
    max_p = None
    min_p = None
    for personaggio, lista_occorrenze in occorrenze.items():
        occ = len(lista_occorrenze)  # numero di occorrenze
        if occ > max_occ:
            max_occ = occ
            max_p = personaggio
        if min_occ is None or occ < min_occ:
            if occ > 0:
                min_occ = occ
                min_p = personaggio

    if max_p is not None:
        print(f'Il personaggio più ricorrente: {max_p} ({max_occ} occorrenze)')
    if min_p is not None:
        print(f'Il personaggio meno ricorrente: {min_p} ({min_occ} occorrenze)')

main()

