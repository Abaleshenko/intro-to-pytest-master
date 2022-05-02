"""
СОРТИРОВКА ВЫБОРОМ

Время работы - медленный
Сортируем элементы по возрастания. Реализуем функцию для нахождения минимального индекса с мин элементом
И реализуем функцию с сортировкой выбора
"""


def find_min(s):
    smallest = s[0]
    smallest_index = 0
    for i in range(1, len(s)):
        if smallest > s[i]:
            smallest_index = i
            smallest = s[i]
    return smallest_index


def selectionSort(s):
    newsq = []

    for i in range(len(s)):
        # Находим найменший элемент массива
        smallest = find_min(s)
        # И добавляем его в новый массив, удаляя его из исходного
        newsq.append(s.pop(smallest))
    return newsq


print(selectionSort([5, 7, -2, 8, 4]))