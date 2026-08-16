def read_input(file_name):
    input_data = []
    with open(file_name, 'r', encoding='UTF-8') as f:
        for line in f:
            parts = line.strip().split(' ')
            filename = parts[0]
            row = int(parts[1])
            col = int(parts[2])
            input_data.append([filename, row, col])
    return input_data

def read_file(file_name):
    lines = []
    with open(file_name, 'r', encoding='UTF-8') as f:
        for line in f:
            line = line.rstrip('\n')  
            lines.append(line)
    return lines

def main():
    input_data = read_input('input.txt')

    # Inizializza una matrice 10x10 con tutti i valori '9' (bianco)
    N = 10
    matrix = []
    for i in range(N):              # Per ogni riga
        row = []
        for j in range(N):          # Per ogni colonna
            row.append('9')         # Inserisce un '9'
        matrix.append(row)          # Aggiunge la riga alla matrice

    # Inzializza contenitori per calcoli successivi
    n_files = []
    count_char = {} 
    intensity = {} 

    # Incolla ciascuna immagine nella posizione specificata
    for element in input_data:                      
        filename, start_row, start_col = element     # Per ogni lista in input, ne definisco gli elementi di cui è composta
        image_lines = read_file(filename)            # In base al file in input, lo legge e ne crea una lista di stringhe (pixel)
        n_files.append(filename)
    
        # enumerate scorre una riga ottenendo sia l'indice che il dato
        for i, line in enumerate(image_lines):       # i: riga dell'immagine, line: stringa con contenuto riga
            for j, pixel in enumerate(line):         # j: colonna dell'immagine, pixel: singolo carattere della stringa
                if filename not in intensity: 
                        intensity[filename] = []
                if pixel != 'X':                     # Se il pixel NON è trasparente
                    matrix[start_row + i][start_col + j] = pixel  # Sovrascrive il pixel
                    intensity[filename].append(int(pixel))
    
    # Number of input image files
    length = len(n_files)
    print(f'Number of input image files: {length}')

    # Name of the image file that contains the biggest input image (including transparent pixels)
    for element in input_data:         
        for line in image_lines:
            if filename in count_char:
                count_char[filename] += len(line)
            else:
                count_char[filename] = len(line)

    max_value = 0
    max_image = None
    for filename, value in count_char.items():
        if value > max_value:
            max_value = value
            max_image = filename
    print(f'Largest image: {max_image}')

    # Name of the darkest image, where the intensity of an image is calculated as the average value of its pixels
    # and its intensity value with two decimal digits (note: the darkest image has the lowest intensity among all images)
    dark_value = None
    darkest_image = None
    for filename, intensities in intensity.items():
        avg = sum(intensities) / len(intensities) #3.70
        if dark_value is None or avg < dark_value:
            if avg > 0.0:
                dark_value = avg
                darkest_image = filename
    print(f'Darkest image: {darkest_image} {dark_value:.2f}')
    print('\n')

    # Stampa la matrice finale riga per riga
    for row in matrix:
        print(''.join(row))  # Concatena i caratteri di ogni riga in una stringa

main()