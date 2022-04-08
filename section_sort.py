def selection_sort(list):
    new_list = []
    for i in range(len(list)):
        smallest = list.index(min(list))
        new_list.append(list.pop(smallest))
    return new_list

print(selection_sort([1, 4, 5, 6, 9, 0, 2]))