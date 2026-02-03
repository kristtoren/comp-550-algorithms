import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import essential_graph_algorithms.topological_sort as ts

# DAG - directed acyclic graph
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

def alg(graph) -> tuple:
    # manually resetting globals from topo_sort()
    ts.t = 1
    ts.topo_list = []
    ts.recursion_stack = set()
    ts.back_edge_count = 0
    ts.pre = {v: -1 for v in graph}
    ts.post = {v: -1 for v in graph}
    ts.parent = {v: -1 for v in graph}
    
    #running topo_sort()
    T = ts.topo_sort(graph)

    # # of vertices in topo sort
    n = len(T)

    #iterating through the topo sorted list
    for i in range(n - 1):
        u = T[i] 
        v = T[i+1]

        if v not in graph.get(u, []): #checking if the edge between i and i+1 exists
            return (u, v) #found this missing edges

    return None

if __name__ == "__main__":
    result = alg(graph)
    
    if result:
        print(f"Found non-reachable pair: {result}")
    else:
        print("No such pair found.")

# Runtime: O(m + n) because topo sort takes O(m+n). We iterate through all vertices n-1 
# and inside that loop we check the out-deg list for each bertex which is O(m+n), giving us
#  O(m+n) +  O(m+n) =  O(m+n)