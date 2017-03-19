import csv

def get_all(rowNumber=0):

    cityNameList = {}
    with open('cityNameList.txt', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            cityNameList[i] = row[rowNumber]
            i += 1
    return cityNameList

