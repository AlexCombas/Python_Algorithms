def merge_sort(a_list):

    if len(a_list) == 0 or len(a_list) == 1:
        return a_list
    else:
        middle_index = len(a_list) // 2
        left = merge_sort(a_list[:middle_index])
        right = merge_sort(a_list[middle_index:])

        return merge(left, right)


def merge(left_half, right_half):
    # if either side is empty the you only need to return
    # the other side of the list
    if not left_half or not right_half:
        return left_half or right_half

    result = []
    i, j = 0, 0

    while True:
        if left_half[i] < right_half[i]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

        if i == len(left_half) or j == len(right_half):
            result.extend(left_half[i:] or right_half[j:])
            break
    return result
