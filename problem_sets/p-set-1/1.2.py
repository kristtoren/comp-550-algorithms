from typing import List 

def alg(nums: List[int]) -> List[int]:
    l = 0
    r = len(nums) - 1
    k = len(nums) - 1 # nums to keep track of pos in res (since we are going backwards)
    res = [0] * len(nums) # result list to return

    while l <= r: #while the ptrs have not overlapped
        # if nums[l]^2 > nums[r]^2, make nums[l]^2 the last element in res, since it is the largest element in nums
        if nums[l] * nums[l] > nums[r] * nums[r]: 
            res[k] = nums[l] * nums[l]
            l += 1 #adjusting the left ptr
        else: # otherwise, nums[r]^2 is bigger
            res[k] = nums[r] * nums[r]
            r -= 1 #adjusting the left ptr
        k -= 1 # decrementing k since we are moving backwards in the res list
    return res

if __name__ == "__main__":
    input  = [-4, -1, 0, 1, 2, 9]

    print(alg(input))

# RUNTIME: O(n)