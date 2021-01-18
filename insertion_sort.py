def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        element = a_list[i]

        while i > 0 and element < a_list[i-1]:
            a_list[i] = a_list[i-1]
            i -= 1

        a_list[i] = element


a = [10, 3, 6, 8, 2]
insertion_sort(a)
print(a)


def insertion_sort_2(a_list):
    for i in range(1, len(a_list)):
        value = a_list[i]
        position = i
        while position > 0 and a_list[position - 1] > value:
            a_list[position] = a[position - 1]
            position = position - 1

        a[position] = value


a = [84, 21, 96, 15, 47]
print(a)
insertion_sort_2(a)
print(a)
