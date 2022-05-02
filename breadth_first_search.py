"""
Алгоритм >> ПОИСК В ШИРИНУ

Алгоритмом, который решает задачу поиска кратчайшего пути от точки A до B называют поиск в ширину
Граф - визуализация набора связей.
Состоит из узлов и ребёр

Условие задачи: вы выращиваете манго, и ходите найти у себя друга или друга ваших дрзей, кто продает манго
ОЧЕРЕДИ >> пренадлжеат категории структур данных FIFO - Fisrt In, First Out (первый пришёл - первый ушёл)
СТЕК >> пренадлжеат категории структур данных LIFO - Last In, First Out (последний пришёл - первый ушёл)

"""

from collections import deque

graph = {"you": ["alice", "bob", "claire"],  # Связанный список к ключу
         "bob": ["alex", "margo"],
         "alice": ["tom"],
         "claire": ["jonny"],
         "alex": [],
         "ton": [],
         "jonny": [],
         "margo": []
         }


def person_is_seller(name):
    """Если имя друга или друга друзей оканчивается на m считаем, что он продавец МАНГО, иначе алгоритм не найдёт
    никого и выведет FALSE"""

    return name[-1] == "m"


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # Если друг является другом других, то его один раз проверить, и не проверят второй раз

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:  # not person - устаревший формат, not in - лучше
            if person_is_seller(person):
                print(f"{person} продавец МАНГО")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
