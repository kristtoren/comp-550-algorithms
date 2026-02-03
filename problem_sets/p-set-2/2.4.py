from collections import deque

# connected and undirected
graph = {
    0: [1, 3,],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

def alg(graph) -> dict:

    c = {v: None for v in graph} # initializing all vertices as uncolored (None)

    # picking the start node (first element)
    start_node = list(graph.keys())[0]

    c[start_node] = 0 # setting it to 'color' 0
    queue = deque([start_node]) #adding it to the queue
    
    while queue: #while the queue isnt empty
        u = queue.popleft() # removing the first element and assigning it to u
        
        for v in graph[u]: # going thru every out-neighbot of vertex u
            if c[v] is None: # if the neighbor node has not been visited...
                c[v] = 1 - c[u] #assigning it the opposite color of vertex u
                queue.append(v) #adding it to the queue
            elif c[v] == c[u]:
                # if the v is already colored and the same as vertex u, graph is NOT bipartite
                return None
    return c

if __name__ == "__main__":
    result = alg(graph)
    
    if result:
        print("The graph is Bipartite.")
        print("Coloring:", result)
    else:
        print("Graph is NOT bipartite.")

# Runtime: O(m + n) --> Basically bfs with some tweaks, so still O(m+n)
