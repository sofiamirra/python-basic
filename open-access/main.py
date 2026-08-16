def read_pubblicazioni(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        editori = {} # {editore: {True: [], False: [] } }
        for line in f:
            campi = line.rstrip('\n').split(';')
            id = campi[0]
            editore = campi[1]
            source = campi[2]
            if editore not in editori:
                editori[editore] = {'TRUE': [], 'FALSE': []}
            # altrimenti se qualche editore non ha false, non viene mai creata la lista e darà KeyError
            if source in ('TRUE', 'FALSE'):
                editori[editore][source].append(id)
    return editori

def read_costi(nome_file):
    with open(nome_file, 'r', encoding = 'UTF-8') as f:
        costi = {}
        for line in f:
            campi = line.rstrip('\n').split(';')
            editore = campi[0]
            costo = int(campi[1])
            costi[editore] = costo
    return costi

def main():
    editori = read_pubblicazioni('pubblication_data.txt')
    costi = read_costi('publisher_fees.txt')
    
    # Pubblicazioni per editore:
    print('Pubblicazioni per editore: ')
    for editore in sorted(editori):
        if editore in costi: # calcolo il numero di true e false e poi il totale
            lista_true = editori[editore]['TRUE']
            lista_false = editori[editore]['FALSE']
            if editori[editore]['TRUE']:                
                conto_true = len(lista_true)
            else:
                conto_true = 0
            if editori[editore]['FALSE']:
                conto_false = len(lista_false)
            else: 
                conto_false = 0
            totale = conto_true + conto_false
            perc_true = (conto_true / totale) * 100
            print(f'{editore}: {totale} articoli, {perc_true:.2f}% open source')

    # Editore con costo massimo:
    costo_massimo = 0
    editore_max = None
    for editore in editori:
        if editore in costi:
            conto_true = len(editori[editore]['TRUE']) # ridefinisco dal dizionario principale
            costo_tot = costi[editore] * conto_true
            if costo_tot > costo_massimo: # verifico il massimo
                costo_massimo = costo_tot
                editore_max = editore
    print(f"\nEditore con costo massimo: {editore_max} ({costo_massimo})")

main()