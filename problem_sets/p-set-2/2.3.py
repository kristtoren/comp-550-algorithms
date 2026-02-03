from collections import deque

# undirected graph
graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2, 4],
    4: [3],
    5: []
}

def alg(graph) -> dict:
    c = {v: 0 for v in graph} # dict initializing each vertex's value to 0
    cc_num = 1 # original island num

    #going thru all vertices in the graph
    for u in graph:
        if c[u] == 0: # if the vertex has not been visited, visit it!!

            # --- Start BFS Wrapper ---
            queue = deque([u])
            c[u] = cc_num  # marking the start node
            while queue:
                curr = queue.popleft() 
                for v in graph[curr]: #checking all neighbors of curr
                    if c[v] == 0:
                        c[v] = cc_num  # labeling the vertex with the current cc_num
                        queue.append(v)
            # --- End BFS Wrapper ---
            
            cc_num += 1 #incrementing for the next island

    return c

if __name__ == "__main__":
    result = alg(graph)
    
    print("Connected Components Labeling:")
    print(result)
    

# Runtime: O(m + n)
# Explanation: We visit every vertex once and iterate over every edge twice (once from each end).
# n is the number of vertices, m is the number of edges.