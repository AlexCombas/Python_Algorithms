def selection_sort(a_list):
    for i in range(len(a_list)-1):

        minimum_index = i
        for current_index in range(i+1, len(a_list)):
            if a_list[minimum_index] > a_list[current_index]:
                minimum_index = current_index

        a_list[i], a_list[minimum_index] = a_list[minimum_index], a_list[i]


a = [16, 21, 12, 38, 23]
selection_sort(a)
print(a)


def selection_sort_2(a_list):
    for i in range(len(a_list)-1, 0, -1):
        max_position = 0
        for j in range(1, i+1):
            if a_list[j] > a_list[max_position]:
                max_position = j
        temp = a_list[i]
        a_list[i] = a_list[max_position]
        a_list[max_position] = temp


a2 = [84, 21, 96, 15, 47]
print(a2)
selection_sort_2(a2)
print(a2)
