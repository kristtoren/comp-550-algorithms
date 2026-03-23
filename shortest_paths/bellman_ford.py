G = [[[2, 53], [6, -66], [14, -84], [15, -52], [16, 70], [17, 83], [27, 76], [29, -87]], [[3, 78], [10, -72], [13, 96], [14, -81], [16, -60], [17, -99], [18, 95], [19, -82], [25, -54], [29, -56]], [[4, 91], [8, -58], [9, 63], [10, 95], [19, 58], [20, 61], [26, 89]], [[5, 69], [9, -89], [17, 87], [21, 66]], [[6, 90], [8, -52], [9, 78]], [[7, 84], [10, -96], [11, 51], [18, 83], [19, 73], [21, 51], [22, 56], [24, -51], [25, 90]], [[8, 73], [18, 57], [20, -63]], [[9, 83], [10, -96], [11, -93], [18, -86], [21, 76], [22, -93], [23, -58], [24, 95]], [[10, 98], [17, 72], [24, 82]], [[11, 73], [12, 97], [13, 96], [18, -50], [21, 61], [22, 63], [25, -56], [28, 87]], [[12, 89], [20, 50], [21, -92]], [[13, 98], [16, -66], [19, 60], [21, -59], [24, 84], [25, -63], [26, 91]], [[14, 66], [15, 91], [16, 91], [18, 90], [21, 82], [28, 74], [29, 72]], [[15, 79], [18, 58], [19, 90], [23, 98], [29, -75], [30, -67]], [[16, 96], [17, -94], [24, -84], [30, 80]], [[17, 55], [18, 74], [23, -98], [27, -84]], [[18, 70], [21, -71]], [[19, 99], [21, 54], [26, 99], [28, 53]], [[20, 89], [21, -89], [25, -94]], [[21, 87], [23, -61]], [[22, 59], [24, 91], [26, 54]], [[23, 53], [27, 83], [28, 81]], [[24, 65]], [[25, 75], [26, -82], [30, 63]], [[26, 61]], [[27, 75]], [[28, 56]], [[29, 98]], [[30, 67]], []]
s = 1

def bellman_ford(graph, source):
    n = len(graph)

    # creating a dp array with all values initialized to inf
    # d[u] will store the shortest distance from source to node u
    d = [float('inf')] * (n + 1)
    
    # distance to the source node is 0
    d[source] = 0

    # Iterate |V| - 1 times (where |V| is the number of vertices, n)
    for _ in range(n - 1):
        # Iterate through all vertices u in the graph (1 to n)
        for u in range(1, n + 1):
            # If the current distance to u is not infinity, check its outgoing edges
            if d[u] != float('inf'):
                # graph[u - 1] because the list is 0-indexed while nodes are 1-indexed
                for v, weight in graph[u - 1]:
                    # Relaxation step:
                    # If the known distance to v is greater than the path through u,
                    # update the shortest distance to v.
                    if d[u] + weight < d[v]:
                        d[v] = d[u] + weight
                        
    return d

if __name__ == "__main__":
    distances = bellman_ford(G, s)
    
    ans3_1 = distances[2]
    ans3_2 = distances[5]
    ans3_3 = distances[10]
    ans3_4 = distances[15]
    
    print(f"Question 3.1: The final value of d[2] is {ans3_1}")
    print(f"Question 3.2: The final value of d[5] is {ans3_2}")
    print(f"Question 3.3: The final value of d[10] is {ans3_3}")
    print(f"Question 3.4: The final value of d[15] is {ans3_4}")

# RUNTIME: O(VE) where V is the number of vertices and E is the number of edges.
# 1. Initialization of the distance array takes O(V) time.
# 2. The outer loop runs V - 1 times.
# 3. Inside the outer loop, we iterate over every node u and all of its outgoing edges. 
#    Collectively across the inner loops, we process every edge exactly once per outer loop iteration.
# 4. Each edge relaxation operation (addition and comparison) takes constant O(1) time.
# 5. Total time = O(V * E). 
#    (Space complexity is O(V) due to the 1D distance array).