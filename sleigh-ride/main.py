import math

def read_province():
    coordinate = {}
    with open('province.csv', 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            fields = line.rstrip('\n').split(',')
            coordinate[fields[3]] = {'latitudine': float(fields[4]), 'longitudine': float(fields[5])}
    return coordinate

def read_bambini():
    bambini = []
    with open('bambini.csv', 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            fields = line.rstrip('\n').split(',')
            bambini.append({'cognome': fields[0], 'nome': fields[1], 'regalo': fields[2], 'provincia': fields[3]})
    return bambini

def primo_bambino(bambini, coordinate):
    latitudine_max = -90
    indice_bambino = -1
    for i in range(len(bambini)):
        provincia = bambini[i]['provincia']
        if coordinate[provincia]['latitudine'] > latitudine_max:
            indice_bambino = i
            latitudine_max = coordinate[provincia]['latitudine']
    return indice_bambino

def calculate_distance(provinciaA, provinciaB, coordinate):
    latA, lonA = coordinate[provinciaA]['latitudine'] * math.pi / 180.0, coordinate[provinciaA]['longitudine'] * math.pi / 180.0
    latB, lonB = coordinate[provinciaB]['latitudine'] * math.pi / 180.0, coordinate[provinciaB]['longitudine'] * math.pi / 180.0

    delta_lat = latB - latA
    delta_lon = lonB - lonA

    h = math.sin(delta_lat/2) ** 2 + math.cos(latA) * math.cos(latB) * math.sin(delta_lon/2) ** 2
    distanza = 2 * 6731 * math.asin(math.sqrt(h))
    return distanza

def closer_kid(bambini, coordinate, bambino_attuale, bambini_visitati):
    distanza_minima = float('inf')
    indice_bambino = -1
    lat_attuale, lon_attuale = coordinate[bambino_attuale['provincia']]['latitudine'], coordinate[bambino_attuale['provincia']]['longitudine']

    for i in range(len(bambini)):
        if i not in bambini_visitati:
            distanza = calculate_distance(bambino_attuale['provincia'], bambini[i]['provincia'], coordinate)
            if distanza < distanza_minima:
                distanza_minima = distanza
                indice_bambino = i

    return indice_bambino

def main():
    bambini = read_bambini()
    coordinate = read_province()

    # Trova il primo bambino (più a Nord)
    indice_primo_bambino = primo_bambino(bambini, coordinate)
    bambino_attuale = bambini[indice_primo_bambino]
    bambini_visitati = {indice_primo_bambino}

    print(f"Consegnato {bambino_attuale['regalo']} a {bambino_attuale['nome']} {bambino_attuale['cognome']} ({bambino_attuale['provincia']})")

    while len(bambini_visitati) < len(bambini):
        indice_bambino_successivo = closer_kid(bambini, coordinate, bambino_attuale, bambini_visitati)
        bambino_attuale = bambini[indice_bambino_successivo]
        bambini_visitati.add(indice_bambino_successivo)

        print(f"Consegnato {bambino_attuale['regalo']} a {bambino_attuale['nome']} {bambino_attuale['cognome']} ({bambino_attuale['provincia']})")

if __name__ == "__main__":
    main()
