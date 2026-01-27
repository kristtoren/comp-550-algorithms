from typing import List
from merge_sort import mergeSort

# SOLUTION #1
def twoSum(nums: List[int], target: int):
    mergeSort(nums) #sorting the input list

    l = 0
    r = len(nums) - 1

    while l < r:
        sum = nums[l] + nums[r] #sum of the two current ptrs
        if sum == target: # if equal to target, return
            return l, r
        elif sum > target: # shift ptrs accordingly otherwise
            r -= 1
        else:
            l += 1
    return []

# SOLUTION #2
def twoSum2(nums: List[int], target: int):
    hashMap = {} # defining the hashmap for O(1) lookups

    for i, n in enumerate(nums): # enumerates nums to extract indices and numbers
        diff = target - n # finds the difference between the current element and the target
        if diff in hashMap: # if the diff is already in the hashmap, then we have found the other element to get to the target
            return [hashMap[diff], i] # returning the index of where the diff num is in the hashMap and the index of the other num
        hashMap[n] = i # if not found, adds n to the hashmap with the key = n and value = i (index)
    return [] # returning nothing


if __name__ == "__main__":
    nums = [1, 5, 7, 2, 3, 13]
    target = 8

    print(twoSum(nums, target))
    print(twoSum2(nums, target))

# RUNTIME: O(n)