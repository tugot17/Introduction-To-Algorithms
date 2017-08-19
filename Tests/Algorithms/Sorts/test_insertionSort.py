from unittest import TestCase

from Algorithms.Sorts.InsertionSort import InsertionSort
from Tests.Algorithms.Sorts.test_sort_helper import test_sort_helper_1,test_sort_helper_2


class TestInsertionSort(TestCase):
    def test_sort1(self):
        insert_sort = InsertionSort()
        test_sort_helper_1(self, insert_sort)

    def test_merge_sort_2(self):
        insert_sort = InsertionSort()
        test_sort_helper_2(self, insert_sort)