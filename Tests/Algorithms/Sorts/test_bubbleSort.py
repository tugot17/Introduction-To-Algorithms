from unittest import TestCase

from Algorithms.Sorts.BubbleSort import BubbleSort
from Tests.Algorithms.Sorts.test_sort_helper import test_sort_helper_1, test_sort_helper_2, \
    test_sort_sorted_array_helper


class TestInsertionSort(TestCase):
    def test_insertion_sort1(self):
        bubble_sort = BubbleSort()
        test_sort_helper_1(bubble_sort)

    def test_insertion_sort2(self):
        bubble_sort = BubbleSort()
        test_sort_helper_2(bubble_sort)

    def test_sorted_array_sort(self):
        bubble_sort = BubbleSort()
        test_sort_sorted_array_helper(bubble_sort)