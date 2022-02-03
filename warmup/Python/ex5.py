arr = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target = 8

def find_longest_subarray_with_target_sum():

    max_len = 0
    d = {}
    add_sum = 0
    for i, num in enumerate(arr):
        add_sum += num
        dist_from_target = abs(add_sum - target)
        if add_sum not in d:
            d[add_sum] = i
        
        if dist_from_target in d:
            sub_len = abs(d[dist_from_target] - i)
            if sub_len > max_len: max_len = sub_len

    print(max_len)
            

find_longest_subarray_with_target_sum()