a = [3, 5, 6, 8, 10, 15, 20]


def binary_search_r(data, low, high, item):
    if low <= high:
        middle = (low + high) // 2
        if data[middle] == item:
            return middle
        elif data[middle] > item:
            return binary_search_r(data, low, middle - 1, item)
        else:
            return binary_search_r(data, middle + 1, high, item)
    else:
        return 1


print(binary_search_r(a, 0, len(a), 20))
