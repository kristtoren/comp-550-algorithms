# input values and weights
v = [64, 111, 58, 168, 98, 192, 142, 129, 214, 205, 240, 243, 127, 190, 150, 216, 221, 242, 242, 123, 215, 237, 113, 93, 202, 187, 71]
w = [1, 2, 2, 23, 10, 38, 16, 24, 8, 18, 31, 59, 14, 27, 46, 21, 64, 49, 35, 40, 37, 11, 3, 10, 14, 44, 5]
B = 31

def fractional_knapsack(v, w, B):
    n = len(v) # number of values

    # list of items values, weights, and ratios
    items = []
    for i in range(n):
        items.append({
            'id': i,
            'v': v[i],
            'w': w[i],
            'ratio': v[i] / w[i]
        })
    
    # sorting items by non-decreasing ration v[i]/w[i]
    items.sort(key=lambda x: x['ratio'], reverse=True)
    
    total_value = 0.0
    current_weight = 0
    x = [0.0] * n  # vector x to store fractions
    
    # iterating thru sorted items
    for item in items:

        #if the curr weight exceeds B, end
        if current_weight >= B: 
            break
            
        if current_weight + item['w'] <= B:
            # take the whole item
            x[item['id']] = 1.0
            current_weight += item['w']
            total_value += item['v']
        else:
            # take a fraction of the item to fill the remaining space
            remaining = B - current_weight
            fraction = remaining / item['w']
            x[item['id']] = fraction
            total_value += item['v'] * fraction
            current_weight += remaining
            break # knapsack is full
            
    return total_value, x

if __name__ == "__main__":
    val, x = fractional_knapsack(v, w, B)
    print(f"Optimal Value: {val}")

# RUNTIME: O(n log n)
# 1. Sorting the n items by their value-to-weight ratio (v[i]/w[i]) takes O(n log n) time.
# 2. The subsequent loop iterates through the n items at most once. Inside the loop, 
#    operations (comparisons, addition, assignment) take O(1) time.
# 3. Therefore, the total running time is dominated by the sort: O(n log n).