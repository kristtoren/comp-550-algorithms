from typing import List

def alg(heights: List[int]) -> int:
    
    maxNum = 0 # max area
    l = 0
    r = len(heights) - 1

    while l < r: # while l and r ptrs havent crossed
        area = (r-l) * min(heights[l], heights[r]) #area calculation
        maxNum = max(maxNum, area) #the max Area achieved

        if heights[l] < heights[r]: # if lft ptr smaller than rght, increment left
            l += 1
        else:
            r -= 1 # otherwise decrement right

    return maxNum

if __name__ == "__main__":
    nums = [1, 4, 7, 2, 6, 10, 11]

    print(alg(nums))

# RUNTIME: O(n)