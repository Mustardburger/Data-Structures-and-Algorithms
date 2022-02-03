arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]


def check_zero_sum():
    """
    Check if there is zero sum subarray. Returns true if found one
    """
    unique_sum = set()
    unique_sum.add(0)
    add_sum = 0
    for num in arr:
        add_sum += num
        if add_sum in unique_sum:
            return True
        unique_sum.add(add_sum)
    return False


def find_zero_sum():
    """
    Find all zero sum subarrays
    """
    temp = []
    temp.append(0)
    add_sum = 0
    for i, num in enumerate(arr):
        add_sum += num
        if add_sum in temp:
            ind = temp.index(add_sum)
            while ind <= i:         # Find all occurrances in temp that has the same value as add_sum
                print(arr[ind:i+1])
                try:
                    ind = temp.index(add_sum, ind+1)
                except:
                    break
        temp.append(add_sum)


find_zero_sum()
# print(check_zero_sum())
