import csv

def selection_sort(dictionary, column):
    for i in range(len(dictionary)):
        min_index = i
        for j in range(i + 1, len(dictionary)):
            if dictionary[min_index][column] > dictionary[j][column]:
                min_index = j

        dictionary[i], dictionary[min_index] = dictionary[min_index], dictionary[i]


def insertion_sort(dictionary, column, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(dictionary)
    for i in range(start + 1, end):
        key = dictionary[i]
        j = i - 1
        while (start <= j <= end) and key[column] < dictionary[j][column]:
            dictionary[j + 1] = dictionary[j]
            j -= 1
        dictionary[j + 1] = key


with open('3-2.csv') as file:
    dictionary = list(csv.DictReader(file))

    selection_sort(dictionary, 'nilai')

    i = 0
    while i < len(dictionary):
        j = i + 1
        while j < len(dictionary) and dictionary[i]['nilai'] == dictionary[j]['nilai']:
            j += 1
        if len(dictionary[i:j]) > 1:
            insertion_sort(dictionary, 'nama', i, j)
        i = j

    print('Hasil'.center(50, '-'))
    for i in dictionary:
        print(i)
