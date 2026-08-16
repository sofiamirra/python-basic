def read_file():
    datas = []
    with open('glucometer.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.rstrip('\n').split(' ')
            datas.append({'id': fields[0], 'time': fields[1], 'index': int(fields[2])})
    return datas

def extract_statistics(datas):
    exceeded_counts = {}
    exceeded_patients = []
    for data in datas:
        if data['index'] > 200:
            patient_id = data['id']
            if patient_id not in exceeded_counts:
                exceeded_counts[patient_id] = 1
            else:
                exceeded_counts[patient_id] += 1
            exceeded_patients.append(data)
    sorted_patients = sorted(exceeded_counts.items(), reverse=True)
    for patient, count in sorted_patients:
        for reading in exceeded_patients:
            if reading['id'] == patient:
                print(f"{reading['id']} {reading['time']} {reading['index']}")

def main():
    datas = read_file()
    extract_statistics(datas)

if __name__ == '__main__':
    main()
