class InsertionSort:
    def sort(self, array):
        length = len(array)

        for j in range (1, length):
            key = array[j]
            i = j-1

            while (i >=0) & (array[i] > key):
                array[i+1] = array[i]
                i = i-1

            array[i + 1] = key

        return array


