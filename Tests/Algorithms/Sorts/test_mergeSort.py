from unittest import TestCase

from Algorithms.Sorts.MergeSort import MergeSort
from Tests.Algorithms.Sorts.test_sort_helper import test_sort_helper_1, test_sort_helper_2, \
    test_sort_sorted_array_helper


class TestMergeSort(TestCase):
    def test_sort1(self):
        merge_sort = MergeSort()
        test_sort_helper_1( merge_sort)

    def test_merge_sort_2(self):
        merge_sort = MergeSort()
        test_sort_helper_2( merge_sort)

    def test_merge_sort_of_sorted_array(self):
        merge_sort = MergeSort()
        test_sort_sorted_array_helper( merge_sort)