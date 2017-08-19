from unittest import TestCase

from Algorithms.SummingTwoBinaryNumbers import add_binnary_numbers


class TestAdd_binnary_numbers(TestCase):
    def test_add_binnary_numbers1(self):
        array1 = [1, 1, 1, 1]
        array2 = [1, 1, 1, 1]

        result = add_binnary_numbers(array1, array2)
        self.assertEqual([1,1,1,1,0], result)

    def test_add_binnary_numbers2(self):
        array1 = [1, 1, 0, 0, 1]
        array2 = [1, 1, 0, 0]

        result = add_binnary_numbers(array1, array2)
        self.assertEqual([1, 0, 0, 1, 0, 1], result)