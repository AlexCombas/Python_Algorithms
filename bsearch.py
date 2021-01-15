a = [3, 5, 6, 8, 10, 15, 20]


def binary_search(data, item):
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high) // 2
        if item == data[middle]:
            return middle
        elif item < data[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1


print(binary_search(a, 7))
