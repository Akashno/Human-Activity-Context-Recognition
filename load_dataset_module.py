import csv



final_dictionary = {}

def activity_data(file):
    with open(file, 'r') as data_file:
        reader = csv.DictReader(data_file)
        extracted_data = {}
        for row in reader:
            id = row['_id']
            del row['_id']
            extracted_data[id] = row
    return extracted_data


def activity_features(file):
    final_dictionary = {}
    orX = []
    orY = []
    orZ = []
    rX = []
    rY = []
    rZ = []
    accX = []
    accY = []
    accZ = []
    mX = []
    mY = []
    mZ = []
    gX = []
    gY = []
    gZ = []
    soundLevel = []
    extracted_data_dictionary = activity_data(file)
    sensors = ['orX', 'orY', 'orZ', 'rX', 'rY', 'rZ', 'accX',
               'accY', 'accZ', 'mX', 'mY', 'mZ', 'gX', 'gY', 'gZ','soundLevel']

    for sensor in sensors:
        for key, value in extracted_data_dictionary.items():
            if sensor == 'orX':
                orX.append(float(value[sensor]))
                final_dictionary[sensor] = orX
            if sensor == 'orY':
                orY.append(float(value[sensor]))
                final_dictionary[sensor] = orY
            if sensor == 'orZ':
                orZ.append(float(value[sensor]))
                final_dictionary[sensor] = orZ
            if sensor == 'rX':
                rX.append(float(value[sensor]))
                final_dictionary[sensor] = rX
            if sensor == 'rY':
                rY.append(float(value[sensor]))
                final_dictionary[sensor] = rY
            if sensor == 'rZ':
                rZ.append(float(value[sensor]))
                final_dictionary[sensor] = rZ
            if sensor == 'accX':
                accX.append(float(value[sensor]))
                final_dictionary[sensor] = accX
            if sensor == 'accY':
                accY.append(float(value[sensor]))
                final_dictionary[sensor] = accY
            if sensor == 'accZ':
                accZ.append(float(value[sensor]))
                final_dictionary[sensor] = accZ
            if sensor == 'mX':
                mX.append(float(value[sensor]))
                final_dictionary[sensor] = mX
            if sensor == 'mY':
                mY.append(float(value[sensor]))
                final_dictionary[sensor] = mY
            if sensor == 'mZ':
                mZ.append(float(value[sensor]))
                final_dictionary[sensor] = mZ
            if sensor == 'gX':
                gX.append(float(value[sensor]))
                final_dictionary[sensor] = gX
            if sensor == 'gY':
                gY.append(float(value[sensor]))
                final_dictionary[sensor] = gY
            if sensor == 'gZ':
                gZ.append(float(value[sensor]))
                final_dictionary[sensor] = gZ
            if sensor == 'soundLevel':
                soundLevel.append(float(value[sensor]))
                final_dictionary[sensor] = soundLevel

    return final_dictionary


