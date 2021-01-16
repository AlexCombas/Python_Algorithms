def bubble_sort_1(list_a):
    n = len(list_a)
    for i in range(n):
        for j in range(0, n-1):
            if list_a[j] > list_a[j + 1]:
                list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]


a_1 = [10, 8, 3, 16, 2, 9, 7, 10, 2, 12, 22, 11, 6, 1]
bubble_sort_1(a_1)
print(a_1)


def bubble_sort_2(list_a):
    n = len(list_a)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if list_a[j] > list_a[j+1]:
                list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
                swapped = True

        if not swapped:
            break


a_2 = [10, 8, 3, 16, 2, 9, 7, 10, 2, 12, 22, 11, 6, 1]
bubble_sort_2(a_2)
print(a_2)
