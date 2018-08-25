def merge_sort(unordered_list):
    """
    Take an unordered_list and split it into two roughly equal-sized
    sub-lists, then sort each sub-list by doing the same again recursively.
    Once the sub-lists reach size 1 (i.e. they are trivially ordered),
    combine them back together in a sorted fashion.

    :param list unordered_list: elements to be sorted

    :return list: sorted elements
    """
    # Deal with the trivial case
    if len(unordered_list) <= 1:
        return unordered_list

    # Split the list into two chunks
    middle_index = len(unordered_list) // 2
    left_list = unordered_list[:middle_index]
    right_list = unordered_list[middle_index:]

    # Apply merge_sort to each
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    # Merge the final lists together
    sorted_list = list(merge(left_list, right_list))
    return sorted_list


def merge(left_list, right_list):
    """
    Take two lists and combine them in a sorted fashion by iteratively
    comparing the first elements in the lists.

    :param list left_list: list of (partially) unsorted elements
    :param list right_list: another list of (partially) unsorted elements

    :return list: the two lists combined in (more) sorted fashion
    """
    sorted_list = []
    left_index = 0
    right_index = 0

    # Iterate through the two lists, comparing the elements in the two lists
    while left_index < len(left_list) and right_index < len(right_list):
        left_element = left_list[left_index]
        right_element = right_list[right_index]

        # If the_left element is smaller, put it in the sorted list
        if left_element < right_element:
            sorted_list.append(left_element)
            left_index += 1

        # If the right element is smaller, put it in instead
        elif left_element >= right_element:
            sorted_list.append(right_element)
            right_index += 1

    # Append any elements left after this to the sorted_list
    if len(left_list) > 0:
        sorted_list.extend(left_list[left_index:])

    if len(right_list) > 0:
        sorted_list.extend(right_list[right_index:])

    return sorted_list
