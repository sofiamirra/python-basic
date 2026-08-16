
def read_pedaggi(nome_file):
    pedaggi = []
    with open(nome_file, 'r', encoding='UTF-8') as f:
        for line in f:
            campi = line.rstrip('\n').split(';')
            pedaggi.append((campi[0], campi[1], float(campi[2])))
    return pedaggi

def read_auto(nome_file):
    passaggi = {}
    with open(nome_file, 'r', encoding='UTF-8') as f:
        for line in f:
            campi = line.rstrip('\n').split(';')
            targa = campi[0]
            percorso = [campi[1], campi[2]]
            if targa not in passaggi:
                passaggi[targa] = [percorso]
            else:
                passaggi[targa].append(percorso)
    return passaggi

def calcola_pedaggio(ingresso, uscita, tratte):
    # calcola indice tratta che ha ingresso = ingresso
    pos_in = -1
    for i, tratta in enumerate(tratte):
        if tratta[0] == ingresso:
            pos_in = i
    # calcola indice tratta che ha uscita = uscita
    pos_out = -1
    for i, tratta in enumerate(tratte):
        if tratta[1] == uscita:  # ✅ corretto: uscita è nella posizione 1
            pos_out = i

    if pos_in != -1 and pos_out != -1 and pos_out >= pos_in:
        pedaggio = 0.0
        for i in range(pos_in, pos_out + 1):
            pedaggio += tratte[i][2]  # ✅ sommo il pedaggio corretto
        return pedaggio, pos_out - pos_in + 1
    else:
        pos_in = -1
        for i, tratta in enumerate(tratte):
            if tratta[1] == ingresso:
                pos_in = i
        pos_out = -1
        for i, tratta in enumerate(tratte):
            if tratta[0] == uscita:
                pos_out = i
        pedaggio = 0.0
        for i in range(pos_out, pos_in + 1):
            pedaggio += tratte[i][2]
        return pedaggio, pos_in - pos_out + 1

def main():
    tratte = read_pedaggi('pedaggi.txt')
    passaggi = read_auto('auto.txt')
    pedaggi_auto = []

    for targa in passaggi:
        elenco_percorsi = passaggi[targa]
        pedaggio_tot = 0
        n_tratte_tot = 0

        for percorso in elenco_percorsi:
            pedaggio, n_tratte = calcola_pedaggio(percorso[0], percorso[1], tratte)
            pedaggio_tot += pedaggio
            n_tratte_tot += n_tratte

        # stampo con due decimali
        print(f"{targa}: {pedaggio_tot:.2f} pedaggio pagato ({n_tratte_tot} tratte percorse in {len(elenco_percorsi)} ingressi)")

        pedaggi_auto.append((targa, pedaggio_tot))

    # trovo la targa con pedaggio massimo
    pedaggio_max = 0.0
    targa_max = ''
    for targa, pedaggio_tot in pedaggi_auto:
        if pedaggio_tot > pedaggio_max:
            pedaggio_max = pedaggio_tot
            targa_max = targa

    print(f"L'auto che ha pagato il pedaggio maggiore ha targa {targa_max}.")

main()
