from typing import List

def binarySearch(nums: List[int] , target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (r+l) // 2 # calculates the middle of the two pointers (index)
        if nums[mid] == target: # if that index is the target, return
            return mid
        elif nums[mid] > target: # elif, if its greater than target, we know it must be to the left (less)
            r = mid - 1 # move r to one below mid idx
        else:
            l = mid + 1 # move l to one above mid idx
    return 

if __name__ == "__main__":
    nums = [1 ,3 , 5, 6, 8, 20, 100]
    target = 100

    print(binarySearch(nums, target))

# RUNTIME: O(logn)