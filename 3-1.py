import csv

def bubble_sort(dictionary):
    for i in range(len(dictionary)):
        for j in range(i + 1, len(dictionary)):
            if dictionary[i]['english'] > dictionary[j]['english']:
                dictionary[i], dictionary[j] = dictionary[j], dictionary[i]


def selection_sort(dictionary):
    for i in range(len(dictionary)):
        min_index = i
        for j in range(i + 1, len(dictionary)):
            if dictionary[min_index]['english'] > dictionary[j]['english']:
                min_index = j

        dictionary[i], dictionary[min_index] = dictionary[min_index], dictionary[i]


def insertion_sort(dictionary):
    for i in range(1, len(dictionary)):
        key = dictionary[i]
        j = i - 1
        while j >= 0 and key['english'] < dictionary[j]['english']:
            dictionary[j + 1] = dictionary[j]
            j -= 1
        dictionary[j + 1] = key


def sort(dictionary, choice):
    if choice == 'bubble sort':
        bubble_sort(dictionary)
    elif choice == 'selection sort':
        selection_sort(dictionary)
    elif choice == 'insertion sort':
        insertion_sort(dictionary)


user_input = input('''* bubble sort
* selection sort
* insertion sort
Pilih metode : ''').lower().strip()

with open('3-1.csv') as file:
    dictionary = list(csv.DictReader(file))

    sort(dictionary, user_input)

    print('Hasil'.center(50, '-'))
    for i in dictionary:
        print(i)