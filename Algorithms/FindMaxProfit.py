'''
Chapter 4 find the biggest profit using Divide & Conquer
'''
def find_max_profit(array):
    return find_max_profit_using_divide_and_conquer(array, 0, len(array)-1)



def find_max_profit_using_divide_and_conquer(array, start, end):
    if end-start == 0:
        return 0, start, start

    if end - start == 1:
        return array[end] - array[start], start, end


    mid = start + (end-start)//2

    max_profit1, buy_day_1, sell_day_1 = find_max_profit_using_divide_and_conquer(array, start, mid)
    max_profit2, buy_day_2, sell_day_2 = find_max_profit_using_divide_and_conquer(array, mid+1, end)


    min_val_in_subarray_1 = array[start]
    min_val_in_subarray_1_id = start

    for i in range(start+1, mid+1):
        if array[i] < min_val_in_subarray_1:
            min_val_in_subarray_1 = array[i]
            min_val_in_subarray_1_id = i

    max_val_in_subarray_2 = array[mid+1]
    max_val_in_subarray_2_id = mid+1

    for i in range(mid+2, end+1):
        if array[i] > max_val_in_subarray_2:
            max_val_in_subarray_2 = array[i]
            max_val_in_subarray_2_id = i

    max_profit3 = max_val_in_subarray_2 - min_val_in_subarray_1


    max_profit = find_max(max_profit1, max_profit2, max_profit3)

    if max_profit == max_profit1:
        return max_profit1, buy_day_1, sell_day_1

    if max_profit == max_profit2:
        return max_profit2, buy_day_2, sell_day_2

    if max_profit == max_profit3:
        return max_profit3, min_val_in_subarray_1_id, max_val_in_subarray_2_id



def find_max(one, two, three):
    a = []
    a.append(one)
    a.append(two)
    a.append(three)
    a.sort()
    return a[2]



