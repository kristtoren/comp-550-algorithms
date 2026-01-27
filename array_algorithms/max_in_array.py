from typing import List

def maxInArray(nums: List[int]) -> int:
    maxNum = nums[0] # max num to be returned -- init to first elem in nums
    for num in nums: #loops thru every elem in nums 
        if num > maxNum: #comparison of maxNum and curr num
            maxNum = num
    return maxNum

if __name__ == "__main__":
    nums = [1, 3, 9, -4, 2000]

    print(maxInArray(nums))

# RUNTIME: O(n)