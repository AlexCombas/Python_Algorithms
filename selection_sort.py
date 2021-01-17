def selection_sort(a_list):
    for i in range(len(a_list)):

        minimum_index = i
        for current_index in range(i+1, len(a_list)):
            if a_list[minimum_index] > a_list[current_index]:
                minimum_index = current_index

        a_list[i], a_list[minimum_index] = a_list[minimum_index], a_list[i]
