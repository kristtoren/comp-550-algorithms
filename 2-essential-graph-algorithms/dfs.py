# the adjacency list that will be used by bfs
graph = {
    0: [18, 19, 23],
    1: [2, 8, 36],
    2: [1, 8, 13],
    3: [29],
    4: [3, 15, 20, 28, 32],
    5: [8, 12, 18, 23, 28, 38],
    6: [17, 19, 31, 38],
    7: [0, 1, 10, 16, 17, 18, 22, 32, 36],
    8: [2, 25, 28, 33, 35, 37],
    9: [0, 2, 14],
    10: [11, 12, 30, 31],
    11: [6, 10, 12, 19, 20, 27, 28],
    12: [13, 26, 28],
    13: [14, 19, 32],
    14: [2, 26],
    15: [14, 19, 28, 30],
    16: [17, 36, 37],
    17: [4, 9, 19, 35, 39],
    18: [17, 20, 28],
    19: [16, 22, 27],
    20: [7, 11, 13, 14, 15, 17, 18, 24, 29, 33, 39],
    21: [23, 26, 30, 34],
    22: [16, 24, 32, 35],
    23: [0, 1, 3, 4, 24, 34, 38],
    24: [3, 9, 13, 14, 33, 38],
    25: [3, 6, 13, 15, 16, 31],
    26: [13, 38],
    27: [18, 25],
    28: [0, 26],
    29: [6, 7, 16, 31, 32],
    30: [3, 8, 21, 27, 29, 37],
    31: [9, 22, 24, 29, 35, 36],
    32: [1, 2, 8, 22, 25, 30],
    33: [],
    34: [5, 26, 36],
    35: [0, 14, 17, 30, 31, 38],
    36: [6, 9, 14, 18, 21, 26, 28, 30],
    37: [4, 10, 26, 32],
    38: [1, 7, 19, 23, 39],
    39: [8, 10, 13, 15, 35]
}

pre = {v: -1 for v in graph} # creating the pre dictionary that maps each vertex to its arrival time
post = {v: -1 for v in graph} # creating the pre dictionary that maps each vertex to its exit time
t = 1 #initializing the timer

back_edge_count = 0 # tracks the number of back edges
recursion_stack = set() # adds the current vertex to the 'recursion stack' to keep track of neighbors

def explore(graph, vertex): # helper function that recursively explores each vertex
    global t, pre, post, back_edge_count, recursion_stack # making sure that we are using the global variables, not local ones
    pre[vertex] = t # setting the arrival to the current time
    t += 1 # incrementing the time

    recursion_stack.add(vertex) # adding the called upon vertex to the recursion stack

    for v in graph[vertex]: # loops through every out-deg in the current vertex
        if pre[v] == -1: # check to see if the out-deg vertex has not been visited
            explore(graph, v) # explore once again
        elif v in recursion_stack:
            back_edge_count += 1
    post[vertex] = t # once we are done with the current vertex, we mark its exit time
    t += 1 # incrementing the clock

    recursion_stack.remove(vertex) # when we are done with the vertex, remove it from the stack

def dfs(graph): 
    for u in graph: #loops through each vertex in the graph
        if pre[u] == -1: # checks to see if the vertex has not yet been visited
            explore(graph, u) # call the explore helper function 
    return pre, post 


if __name__ == "__main__":
    pre, post = dfs(graph)

    print("Pre list: ", pre)
    print("Post list: ", post)
    print(f"Total Back Edges: {back_edge_count}")