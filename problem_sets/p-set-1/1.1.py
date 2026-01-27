from typing import List

# SOLUTION #1
def alg(nums: List[int]) -> int:
    n = len(nums) - 1 # we do -1 because we want n to be the length of nums minus the extra element
    # the difference in the total sum of the list minus ((n * (n+1))/2) will find us the repeated value
    # this is true because nums is equal to ((n * (n+1))/2) + k where k is the repeated element
    # we know ((n * (n+1))/2) is equivalent to 1 + 2 + ... + n
    return sum(nums) - ((n * (n+1)) // 2)

# SOLUTION #2
def alg2(nums: List[int]) -> int:
    b = [0] * len(nums) # binary array intialized to 0's
    for num in nums: # iterates through every element in nums
        if b[num] == 1: #checks to see if that element was already found
            return num
        b[num] = 1 # once a num in nums is visited, set the num at its respective index to 1 in b


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9] # input

    # output = alg(nums)
    output = alg2(nums)
    print(output)

# RUNTIME: O(n)