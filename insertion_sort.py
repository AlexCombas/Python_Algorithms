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