A = [
    14, 84, 76, 26, 50, 45, 65, 79, 10, 3, 83, 43, 76, 1, 45, 72, 23, 94, 90, 4, 3, 54, 
    93, 38, 22, 42, 3, 22, 44, 50, 24, 23, 22, 46, 29, 3, 83, 56, 64, 19, 99, 86, 12, 
    33, 72, 71, 93, 42, 83, 67, 31, 59, 88, 84, 51, 59, 4, 25, 79, 42, 18, 55, 70, 67, 
    38, 44, 51, 78, 52, 39, 49, 3, 5, 70, 98, 59, 39, 17, 50, 98, 77, 54, 86, 23, 51, 
    95, 58, 46, 27, 55, 95, 1, 78, 82, 88, 74, 81, 52, 56, 43
]

# helper to reconstruct the sequence implicitly found by the algorithm
# this implements the logic: "trace back from the end index using predecessor array"
def reconstruct_lis(array, prev, end_index):
    sequence = []
    curr = end_index
    while curr is not None:
        sequence.append(array[curr])
        curr = prev[curr]
    return sequence[::-1]  # reverse to get the correct LIS order

def solve_lis(A_input):
    n = len(A_input)
    # empty lists for DP array and predecessors
    d = [1] * n
    prev = [None] * n

    # iterating thru the array
    for i in range(1, n):
        # check all possible previous elements
        for j in range(i):
            if A_input[j] < A_input[i]:
                # Strictly greater (>) ensures we break ties in favor of the smaller index j
                if d[j] + 1 > d[i]:
                    d[i] = d[j] + 1
                    prev[i] = j
                    
    return d, prev

if __name__ == "__main__":
    d_array, prev_array = solve_lis(A)
    
    # Find the max length and the corresponding smallest index
    max_length = 0
    best_index = -1
    for i in range(len(d_array)):
        # Strictly greater (>) ensures we break ties in favor of the smaller index i
        if d_array[i] > max_length:
            max_length = d_array[i]
            best_index = i
            
    # Reconstruct the implicitly found LIS
    lis_sequence = reconstruct_lis(A, prev_array, best_index)

    print(f"Algorithm returns (Max LIS Length): {max_length}")
    print(f"Last 3 elements in d: {d_array[-3:]}")
    print(f"First 3 elements in the LIS: {lis_sequence[:3]}")
    print(f"Last 3 elements in the LIS: {lis_sequence[-3:]}")

# RUNTIME: O(n^2) 
# 1. Initialization of `d` and `prev` takes O(n).
# 2. The algorithm iterates i from 1 to n-1 (outer loop).
# 3. In each iteration, it checks all j from 0 to i-1 (inner loop).
#    This results in 1 + 2 + 3 + ... + (n-1) = n(n-1)/2 operations.
# 4. Total time = O(n) + O(n^2) = O(n^2).