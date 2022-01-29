arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

def check_zero_sum():
    """
    Check if there is zero sum subarray. Returns true if found one
    """
    unique_sum = set()
    add_sum = 0
    for num in arr:
        add_sum += num
        if num not in unique_sum:
            unique_sum.add(add_sum)
        else:
            return True
    return False

def find_zero_sum():
    """
    Find all zero sum subarrays
    """
    

print(check_zero_sum())