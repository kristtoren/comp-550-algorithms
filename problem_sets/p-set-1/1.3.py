from typing import List

def alg(a: List[int], b: List[int]) -> List[int]:
    c = [] # res list
    for num in b: # goes thru every elem in b
        if num in a: # if that elem is in a, add to c
            c.append(num)
    return c

if __name__ == "__main__":
    a = [1, 3, 5, 7, 9]
    b = [1, 5, 9, 11]

    print(alg(a, b))

# RUNTIME: O(nlogm) where n = # of elem in b and m = # of elem in m
# Note: technically supposed to sort a and then do a binary search for the num in b every iteration,
# making this loop run n times and takes logm time each iteration