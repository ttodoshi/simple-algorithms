from collections import deque


def person_is_first(person):
    return person.startswith('A')


def search(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_first(person):
                print(f'{person} is first in list')
                return True
            search_queue += graph[person]
            searched.append(person)
    return False


if __name__ == '__main__':
    graph = {'Daria': ['Bob', 'Dan', 'Alice'], 'Bob': [
        'Tom'], 'Dan': ['Chlore'], 'Alice': [], 'Tom': [], 'Chlore': []}
    search(graph, 'Daria')
