import sys
arr = [-10, -3, 5, 6, -2]
def find_pair_with_max_product():
    """
    Find a pair in the array with maximum product
    """
    if len(arr) <= 1:
        return ()
    max1, max2 = -sys.maxsize, -sys.maxsize
    min1, min2 = sys.maxsize, sys.maxsize
    for i, num in enumerate(arr):
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    if max1*max2 > min1*min2: return (max1, max2)
    else: return (min1,min2)

print(find_pair_with_max_product())