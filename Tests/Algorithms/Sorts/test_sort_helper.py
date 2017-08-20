from wheel.signatures import assertTrue


def test_sort_helper_1( sort):
    array = [22, 221, 32, 1]
    array = sort.sort(array)
    is_sorted = is_array_sorted(array)
    assertTrue(is_sorted)

def test_sort_helper_2(sort):
    import random
    array = random.sample(range(1, 1000), 999)
    array = sort.sort(array)
    is_sorted = is_array_sorted(array)

    assertTrue(is_sorted)


def test_sort_sorted_array_helper(sort):
    array = []

    for i in range(1,30):
        array.append(i)

    array = sort.sort(array)
    is_sorted = is_array_sorted(array)
    assertTrue(is_sorted)

def is_array_sorted(array):
    is_sorted = True
    i = 1

    while is_sorted & (i < len(array)):
        is_sorted = array[i - 1] <= array[i]
        i = i + 1

    return is_sorted