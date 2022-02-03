nums = [8, 7, 2, 5, 3, 1]
target = 10

############################### METHOD 1 - BRUTE FORCE ################################
def brute_force():
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f"({nums[i]}, {nums[j]})")

############################### METHOD 2 - SORTING ####################################
def sorting():
    nums.sort()
    low, high = 0, len(nums) - 1

    while low < high:

        if nums[low] + nums[high] == target:
            print(f"({nums[low]}, {nums[high]})")

        if nums[low] + nums[high] > target:
            high -= 1
        else:
            low += 1

############################## METHOD 3 - HASHING #####################################
def hashing():
    d = {}
    for num in nums:
        if target - num not in d:
            d[num] = target - num
        else:
            print(f"({num}, {target - num})")


if __name__ == "__main__":
    hashing()


