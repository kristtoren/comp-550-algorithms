import heapq

G = [[[2, 58], [27, 96]], [[3, 64], [7, 51], [9, 91], [16, 82], [17, 77], [19, 62]], [[4, 93], [23, 85], [26, 86], [28, 92], [30, 50]], [[3, 97], [5, 82]], [[6, 50], [15, 92]], [[7, 95], [11, 90], [22, 53], [26, 97]], [[4, 79], [8, 99], [27, 58]], [[2, 72], [3, 93], [9, 52], [12, 63], [20, 99], [21, 81]], [[10, 86]], [[1, 84], [2, 68], [11, 68]], [[8, 52], [12, 87]], [[5, 61], [13, 88], [17, 52], [23, 94]], [[12, 86], [14, 51]], [[8, 91], [15, 73], [28, 86]], [[2, 96], [12, 66], [16, 55], [17, 58], [18, 89], [23, 74], [24, 77], [26, 78], [28, 63]], [[17, 67]], [[2, 51], [6, 98], [18, 95]], [[4, 79], [7, 95], [8, 69], [16, 71], [19, 87], [20, 94]], [[1, 67], [20, 72]], [[5, 92], [21, 71], [30, 98]], [[8, 59], [22, 56], [25, 61]], [[14, 65], [23, 63], [24, 52]], [[19, 99], [24, 90]], [[11, 72], [16, 54], [22, 59], [25, 63]], [[3, 52], [26, 65], [29, 82]], [[1, 87], [11, 68], [27, 83]], [[1, 70], [21, 91], [28, 51]], [[2, 61], [4, 89], [29, 77]], [[2, 62], [6, 66], [18, 50], [27, 84], [30, 85]], [[3, 83], [11, 60]]]
s = 1

def solve_dijkstra(graph, source):
    n = len(graph)
    
    # Create a distance array initialized to infinity
    # d[u] will store the shortest distance from the source to node u
    d = [float('inf')] * (n + 1)
    d[source] = 0
    
    # Priority queue stores tuples of (distance, node)
    # We initialize it with the source node at distance 0
    pq = [(0, source)]
    
    while pq:
        # Get the node with the smallest known distance
        current_dist, u = heapq.heappop(pq)
        
        # If we have already found a shorter path to u, skip processing it
        # (This is standard lazy deletion for Dijkstra with a standard heap)
        if current_dist > d[u]:
            continue
            
        # Iterate over all adjacent nodes v and their edge weights
        # graph[u - 1] handles the 1-based to 0-based index conversion
        for v, weight in graph[u - 1]:
            distance = current_dist + weight
            
            # Relaxation step:
            # If the calculated distance is shorter than the currently known shortest path to v
            if distance < d[v]:
                d[v] = distance
                # Push the updated distance and node into the priority queue
                heapq.heappush(pq, (distance, v))
                
    return d

if __name__ == "__main__":
    distances = solve_dijkstra(G, s)
    
    ans5_1 = distances[2]
    ans5_2 = distances[5]
    ans5_3 = distances[10]
    
    print(f"Question 5.1: The final value of d[2] is {ans5_1}")
    print(f"Question 5.2: The final value of d[5] is {ans5_2}")
    print(f"Question 5.3: The final value of d[10] is {ans5_3}")

# RUNTIME: O((V + E) log V)
# 1. Initialization of the distance array takes O(V) time.
# 2. Each vertex is extracted from the priority queue at most once. The priority queue operations (heappop) take O(log V) time, resulting in O(V log V) for all vertices.
# 3. We iterate over all outgoing edges of every extracted vertex. Across the entire execution, the inner loop runs exactly E times.
# 4. For each edge, if we find a shorter path, we perform a heappush operation which takes O(log V) time. In the worst case, this happens for every edge, taking O(E log V) time.
# 5. Total time = O(V log V + E log V) = O((V + E) log V).
#    (Space complexity is O(V) for the priority queue and distance array).