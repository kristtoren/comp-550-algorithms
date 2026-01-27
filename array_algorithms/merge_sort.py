from typing import List

def mergeSort(nums: List[int]) -> List[int]:
    n = len(nums)

    if n <= 1: # base case for if the list as 0 or 1 element
        return nums
    
    mid = n // 2 # finds the middle of the input list

    numsLeft = mergeSort(nums[:mid]) # left half of nums - recursive sort
    numsRight = mergeSort(nums[mid:]) # right half of nums - recursive sort

    i = 0 # ptr for nums left
    j = 0 # ptr for nums right
    B = [] # list that will hold the merged + sorted elements

    # MERGE LOOP
    while i < len(numsLeft) and j < len(numsRight): #runs until one of the lists is exhausted
        if numsLeft[i] <= numsRight[j]: # finds the smaller of the two elems
            B.append(numsLeft[i]) #appending the smaller elem to B
            i += 1
        else: 
            B.append(numsRight[j]) # same here, but for right list
            j += 1

    B.extend(numsLeft[i:]) #adding the rest of nums left to B
    B.extend(numsRight[j:])  #adding the rest of nums right to B
    
    return B


if __name__ == "__main__":
    nums = [1, 5, 2, 7, 1, 4, 10]

    print(mergeSort(nums))

# RUNTIME: O(nlogn)