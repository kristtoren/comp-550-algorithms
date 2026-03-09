A1 = "abcdb"
A2 = "accabbbcaacbcabcaccaabcbabaabbaaabaacbbaccaacccbcc"

def solve_lps(A_input):
    n = len(A_input)
    
    # Create a 2D DP table initialized to 0
    # dp[i][j] will store the length of LPS in the substring A_input[i..j]
    dp = [[0] * n for _ in range(n)]

    # Base case: Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # L is the length of the substring we are currently checking
    # We build the table diagonally, from shorter strings to longer strings
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            
            # If the ends match and the length is exactly 2
            if A_input[i] == A_input[j] and L == 2:
                dp[i][j] = 2
            # If the ends match and the length is > 2
            elif A_input[i] == A_input[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            # If the ends do not match, take the max of excluding the right or left end
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
                
    # The result for the full string is in the top-right corner of the table
    return dp[0][n - 1]

if __name__ == "__main__":
    ans1 = solve_lps(A1)
    ans2 = solve_lps(A2)
    
    print(f"Q3: Algorithm returns for A1 ('{A1}'): {ans1}")
    print(f"Q4: Algorithm returns for A2: {ans2}")

# RUNTIME: O(n^2) 
# 1. Initialization of the 2D `dp` table takes O(n^2) time.
# 2. The outer loop runs for substring lengths L from 2 to n.
# 3. The inner loop runs (n - L + 1) times for each L.
#    This results in roughly n^2 / 2 total iterations.
# 4. Inside the inner loop, we do constant O(1) operations (array lookups, max()).
# 5. Total time = O(n^2).
#    (Space complexity is also O(n^2) due to the 2D DP table).