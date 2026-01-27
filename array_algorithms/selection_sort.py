from typing import List

def selectionSort(nums: List[int]) -> List[int]:
    for i in range(len(nums)): #loops through every element in nums
        minIdx = i # the index with the smallest element in this current iteration
        for j in range(i+1, len(nums)): # second loop that finds the smallest elem in rest of list and swaps with nums[i]
            if nums[j] < nums[minIdx]: # if the current j is less than minIdx, replace minidx with j
                minIdx = j
        #swapping nums[i] and nums[minIdx]
        temp = nums[minIdx] 
        nums[minIdx] = nums[i]
        nums[i] = temp
    return nums

if __name__ == "__main__":
    nums = [1, 5, 2, 7, 1, 4, 10]

    print(selectionSort(nums))

# RUNTIME: O(n^2)