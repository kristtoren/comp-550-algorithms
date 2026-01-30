# COPIED DFS CODE INTO THIS FILE AND ADDED A FEW LINES TO TRACK TOPOLOGICAL SORT LIST

# the adjacency list that will be used by bfs
graph = {
    0: [1, 2, 3],
    1: [3],
    2: [3],
    3: []
}

pre = {v: -1 for v in graph} # creating the pre dictionary that maps each vertex to its arrival time
post = {v: -1 for v in graph} # creating the post dictionary that maps each vertex to its exit time
parent = {v: -1 for v in graph} # creating the parent dictionary to track DFS tree structure

t = 1 #initializing the timer

back_edge_count = 0 # tracks the number of back edges
recursion_stack = set() # adds the current vertex to the 'recursion stack' to keep track of neighbors

topo_list = [] # list to store topological ordering

def explore(graph, vertex): # helper function that recursively explores each vertex
    global t, pre, post, parent, back_edge_count, recursion_stack # making sure that we are using the global variables, not local ones
    pre[vertex] = t # setting the arrival to the current time
    t += 1 # incrementing the time

    recursion_stack.add(vertex) # adding the called upon vertex to the recursion stack

    for v in graph[vertex]: # loops through every out-deg in the current vertex
        if pre[v] == -1: # check to see if the out-deg vertex has not been visited
            parent[v] = vertex # set parent pointer for DFS tree
            explore(graph, v) # explore once again
        elif v in recursion_stack:
            back_edge_count += 1
    post[vertex] = t # once we are done with the current vertex, we mark its exit time

    topo_list.insert(0, vertex) # inserting the vertex to the beginning of the list (older post value)

    t += 1 # incrementing the clock

    recursion_stack.remove(vertex) # when we are done with the vertex, remove it from the stack

def topo_sort(graph): 
    for u in graph: #loops through each vertex in the graph
        if pre[u] == -1: # checks to see if the vertex has not yet been visited
            explore(graph, u) # call the explore helper function 
    return topo_list


if __name__ == "__main__":
    topo_list = topo_sort(graph)

    print("Topo list: ", topo_list)

# RUNTIME: O(n + m) where n = # vertices and m = # edges