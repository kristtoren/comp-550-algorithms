v1 = [3, 1, 2]
w1 = [2, 1, 4]
B1 = 4

v2 = [3, 17, 15, 5, 10, 9, 13, 15, 2, 1, 16, 9, 15, 1, 9, 14, 5, 18, 18, 1, 1, 11, 18, 8, 5, 9, 1, 5, 9, 10, 5, 5, 5, 9, 6, 1, 16, 11, 13, 4, 19, 17, 3, 7, 14, 14, 18, 9, 16, 13]
w2 = [6, 12, 17, 17, 10, 12, 1, 5, 16, 8, 4, 11, 14, 13, 8, 9, 10, 15, 10, 8, 10, 1, 1, 14, 19, 12, 8, 4, 10, 19, 15, 11, 17, 5, 10, 19, 11, 9, 6, 11, 19, 1, 15, 16, 17, 15, 16, 10, 11, 9]
B2 = 40

def solve_knapsack(values, weights, capacity):
    n = len(values)
    
    # Create a 2D DP table initialized to 0
    # dp[i][j] will store the max value using the first i items with capacity j
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Iterate through all items
    for i in range(1, n + 1):
        # Iterate through all possible capacities from 1 up to B
        for j in range(1, capacity + 1):
            
            # If the current item's weight is less than or equal to current capacity
            if weights[i - 1] <= j:
                # Max of:
                # 1. Not including the item (taking value from row above)
                # 2. Including the item (value of item + max value of remaining capacity)
                dp[i][j] = max(
                    dp[i - 1][j], 
                    dp[i - 1][j - weights[i - 1]] + values[i - 1]
                )
            else:
                # Item is too heavy, we can't include it
                dp[i][j] = dp[i - 1][j]
                
    # The bottom-right cell contains the maximum value for all items and full capacity
    return dp[n][capacity]

if __name__ == "__main__":
    ans5 = solve_knapsack(v1, w1, B1)
    ans6 = solve_knapsack(v2, w2, B2)
    
    print(f"Q5: Algorithm returns for small knapsack: {ans5}")
    print(f"Q6: Algorithm returns for large knapsack: {ans6}")

# RUNTIME: O(nB) 
# 1. Initialization of the 2D `dp` table takes O(nB) time.
# 2. The outer loop runs n times (once for each item).
# 3. The inner loop runs B times (for each capacity amount up to B).
# 4. Inside the inner loop, we do constant O(1) operations (array lookups, max()).
# 5. Total time = O(nB), which is pseudo-polynomial since it depends on the magnitude of B.
#    (Space complexity is also O(nB) due to the 2D DP table, though it can be optimized to O(B)).