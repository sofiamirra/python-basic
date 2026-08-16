
from operator import itemgetter
def read_file(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        record = {} # record = {professione: [followers]}
        for line in f:
            campi = line.rstrip('\n').split(';')
            professione = campi[3]
            followers = float(campi[2])
            if professione not in record:
                record[professione] = []
            record[professione].append(followers)
    return record

def main():
    record = read_file('instagram.txt')

    istogramma = []
    for professione, lista_followers in record.items():
        totale = sum(lista_followers)
        informazioni = []
        informazioni.append(professione)
        informazioni.append(totale)
        istogramma.append(informazioni)
    istogramma.sort(key=itemgetter(1), reverse = True) # ordinamento decrescente

    for element in istogramma:
        professione = element[0]
        followers = element[1]
        print(f'{professione}: {followers:.1f}M')

main()