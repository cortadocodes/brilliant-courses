import pytest

from merge_sort import merge_sort


@pytest.mark.parametrize("unsorted_list, expected", [
    ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]),
    ([4, 3, 2, 1, 0], [0, 1, 2, 3, 4]),
    ([-7, 10, -32, 5, 70], [-32, -7, 5, 10, 70])
])
def test_merge_sort(unsorted_list, expected):
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == expected