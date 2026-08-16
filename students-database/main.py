
def read_studenti(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        prima = f.readline()
        studenti = {} # un record distinto per ogni studente, definito da ID
        for line in f:
            campi = line.rstrip('\n').split(',')
            id = int(campi[0])
            studenti[id] = {'ID': int(campi[0]), 
                            'cognome_studente': campi[1],
                            'grado': campi[2],
                            'GPA': float(campi[3])}
    return studenti

def read_criteria(nome_file): # tre righe di formato diverso: lette una per volta
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        prima = f.readline() 
        campi = prima.rstrip('\n').split(',')
        lista_id = []
        for campo in campi:
            campo = int(campo)
            lista_id.append(campo)
        seconda = str(f.readline().rstrip('\n'))
        terza = str(f.readline().rstrip('\n'))
    return lista_id, seconda, terza

def main():
    studenti = read_studenti('studenti.txt')
    lista_id, seconda, terza = read_criteria('criteria.txt')

    ## Studenti trovati per ID 
    print('Studenti trovati per ID:')
    for id in studenti:
        if id in lista_id: # se l'ID dello studente è nella lista di id richiesti
            print(studenti[id]) # stampo tutto il dizionario dello studente

    ## Studenti trovati per cognome 
    print('\nStudenti trovati per cognome:')
    for id in studenti:
        if studenti[id]['cognome_studente'] in seconda: # accesso semplice a dizionario
            print(studenti[id]) # stampo tutto il dizionario dello studente

    ## Media del GPA per grado  
    lista_GPA = []       
    for id in studenti:
            if studenti[id]['grado'] in terza: # accesso semplice a dizionario
                gpa = studenti[id]['GPA']
                lista_GPA.append(gpa)
    media = sum(lista_GPA)/len(lista_GPA)
    print(f'\nMedia del GPA per il grado {terza}: {media:.2f}')

main()

