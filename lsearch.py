def linear_search(main_list, item):
    for i in range(len(main_list)):
        if main_list[i] == item:
            return i
    return -1


a = [5, 2, 8, -2, 10, 6, 1]
print(linear_search(a, 10))
