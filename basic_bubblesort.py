def bubble_sort_1(list_a):
    n = len(list_a)
    for i in range(n):
        for j in range(0, n-1):
            if list_a[j] > list_a[j + 1]:
                list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]


a = [10, 8, 3, 6, 1]
bubble_sort_1(a)
print(a)
