class BubbleSort:
    def sort(self, array):
        for i in range(len(array) - 1):
            for j in range(1, len(array)-i):
                if (array[j-1] > array[j]):
                    helper = array[j]
                    array[j] = array[j-1]
                    array[j-1] = helper

        return array