class MergeSort:

    def sort(self, array):
        if len(array) > 1:
            guard = len(array) // 2
            subarray1 = array[0: guard]
            subarray2 = array[guard: len(array)]

            subarray1 = self.sort(subarray1)
            subarray2 = self.sort(subarray2)
            result = self.merge(subarray1, subarray2)

            return result

        else:
            return array

    def merge(self, subarray1, subarray2):

        result = []

        while (len(subarray1) > 0) & (len(subarray2) > 0):

            if subarray1[0] <= subarray2[0]:
                result.append(subarray1[0])
                subarray1.__delitem__(0)
            else:
                result.append(subarray2[0])
                subarray2.__delitem__(0)

        if (len(subarray1) > 0):
            for i in range(len(subarray1)):
                result.append(subarray1[i])
        else:
            for i in range(len(subarray2)):
                result.append(subarray2[i])

        return result