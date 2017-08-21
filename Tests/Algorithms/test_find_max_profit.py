from unittest import TestCase

from Algorithms.FindMaxProfit import find_max_profit


class TestFind_max_profit(TestCase):
    def test_find_max_profit_1(self):
        array = [8, 5, 13, 28, 5]
        self.assertEqual((23, 1, 3), find_max_profit(array))

    def test_find_max_profit_2(self):
        array = [8, 7, 5, 4, 2]
        self.assertEqual((0,2, 2), find_max_profit(array))

    def test_find_max_profit_3(self):
        array = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
        self.assertEqual((43, 7, 11), find_max_profit(array))