def quicksort(unsorted_list):
    less = []
    pivotList = []
    more = []
    arr_length = len(unsorted_list)

    if arr_length <= 1:
        return unsorted_list

    else:
        pivot = unsorted_list[0]

        for element in unsorted_list:
            if element < pivot:
                less.append(element)
            elif element > pivot:
                more.append(element)
            else:
                pivotList.append(element)

        less = quicksort(less)
        more = quicksort(more)
        sorted_list = less + pivotList + more

        return sorted_list

unsorted_list = ([5, 4, 3, 2, 1])
sorted_list = quicksort(unsorted_list)
