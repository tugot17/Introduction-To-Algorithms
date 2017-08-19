def test_sort_helper_1(self, sort):
    array = [22, 221, 32, 1]
    array = sort.sort(array)

    self.assertTrue(array[0] == 1)
    self.assertTrue(array[1] == 22)
    self.assertTrue(array[3] == 221)


def test_sort_helper_2(self, sort):
    import random
    array = random.sample(range(1, 1000), 999)


    array = sort.sort(array)

    is_sorted = True
    i = 1

    while is_sorted & (i < len(array)):
        is_sorted = array[i - 1] <= array[i]
        i = i + 1

    self.assertTrue(is_sorted)