bin_arr = [1, 0, 1, 0, 1, 0, 0, 1]

def binary_sorting():

    one_ind = bin_arr.index(1)
    for i in range(one_ind, len(bin_arr)):
        if bin_arr[i] == 0:
            bin_arr[i] = 1
            bin_arr[one_ind] = 0
            one_ind += 1

    print(bin_arr)

binary_sorting()
