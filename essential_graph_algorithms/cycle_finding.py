from dfs import dfs

# the adjacency list that will be used by bfs
graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [1]
}

def find_cycle(graph):
    # resetting the dfs global variables 
    global t, pre, post, back_edge_count, recursion_stack
    pre = {v: -1 for v in graph}
    post = {v: -1 for v in graph}
    t = 1
    back_edge_count = 0
    recursion_stack = set()
    
    pre, post, parent = dfs(graph)  # pre, post, and parent results from running dfs
    
    # checking all edges for a back edge
    for u in graph: # every vertex
        for v in graph[u]: # every out-deg at that vertex
            if pre[v] < pre[u] and post[u] < post[v]: # check for back edge
                path = [] # cycle path
                current = u #current vertex is the one we start at 
                while current != v: #while we have not reached the vertex w/ the back edge
                    path.append(current) #add the current vertex to the path
                    current = parent[current] # sets the current vertex to the parent of the current
                 # at the end, append v and u
                path.append(v)
                path.append(u)
                return path
    return None # no cycle was found

if __name__ == "__main__":
    cycle = find_cycle(graph)
    
    if cycle:
        print(f"cycle found: {cycle}")
        print(f"cycle length: {len(cycle) - 1}")  # -1 because first and last vertex are the same
    else:
        print("no cycle found")

# RUNTIME: O(n + m) where n = # vertices and m = # edges