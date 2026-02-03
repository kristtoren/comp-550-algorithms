import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from essential_graph_algorithms.bfs import bfs

# the adjacency list that will be used by bfs
graph = {
    0: [1],
    1: [0, 2, 3],
    2: [1, 3],
    3: [1, 2]
}

def alg(graph) -> int:
    diam = 0
    for u in graph: # iterates through every vertex in the graph
        distances, parents = bfs(graph, u) # gets the shortest path distances from u to all other nodes
        max_d_from_u = max(distances.values()) #finding the maximum distance in the current bfs search
        diam = max(diam, max_d_from_u) # updating max dist if the curr bfs dist max is greater than curr diam
    return diam

if __name__ == "__main__":
    res = alg(graph)
    print(f"The diameter of the graph is: {res}")

# Runtime: O(mn) because the alg takes n iterations and each iteration takes O(m+n) which is inherently O(m) 
# because the graph is connected