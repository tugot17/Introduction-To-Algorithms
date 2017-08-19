from unittest import TestCase

from Algorithms.Sorts.MergeSort import MergeSort
from Tests.Algorithms.Sorts.test_sort_helper import test_sort_helper_1, test_sort_helper_2


class TestMergeSort(TestCase):
    def test_sort1(self):
        merge_sort = MergeSort()
        test_sort_helper_1(self, merge_sort)

    def test_merge_sort_2(self):
        merge_sort = MergeSort()
        test_sort_helper_2(self, merge_sort)