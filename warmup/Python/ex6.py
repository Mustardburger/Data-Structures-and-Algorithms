arr = [0, 0, 1, 0, 1, 0, 0]
def longest_sub_binary_array():
    """
    Given a binary array, find the longest subarray where number of 0 == number of 1
    """
    d = {}
    d[0] = -1
    max_len = 0
    end_ind = -1
    add_sum = 0
    for i, num in enumerate(arr):
        if num == 0: add_sum -= 1
        else: add_sum += num
        if add_sum in d:
            s = d[add_sum]
            if i-s > max_len:
                max_len = i-s
                end_ind = i
        else:
            d[add_sum] = i

    print(arr[end_ind-max_len+1:end_ind+1])

longest_sub_binary_array()

    

