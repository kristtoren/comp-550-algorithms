from collections import deque

# the adjacency list that will be used by bfs
graph = {
    0: [41],
    1: [26, 31, 37, 42],
    2: [],
    3: [13, 24, 37, 41],
    4: [11, 22, 37],
    5: [20, 29, 38, 45, 46],
    6: [0, 11, 46],
    7: [22],
    8: [29, 44, 49],
    9: [7, 16, 40],
    10: [3, 5, 31, 36],
    11: [],
    12: [11, 25],
    13: [3, 24],
    14: [11, 34, 44],
    15: [23, 28],
    16: [7, 11, 20, 29],
    17: [20, 42, 49],
    18: [7, 10, 39, 49],
    19: [3, 8, 14, 20, 48],
    20: [8, 11, 26],
    21: [23],
    22: [],
    23: [10, 35],
    24: [2, 21, 31],
    25: [6, 18, 26, 46, 49],
    26: [4],
    27: [8, 30],
    28: [10, 31, 39],
    29: [1, 4, 26],
    30: [5, 13, 32],
    31: [1, 10, 12, 17, 46],
    32: [4],
    33: [1, 5, 8, 30],
    34: [8, 17],
    35: [17],
    36: [30, 34, 48],
    37: [48],
    38: [11, 29],
    39: [2, 34, 36, 46, 47],
    40: [0, 12, 18, 38],
    41: [20],
    42: [1, 36],
    43: [4, 11, 15, 17],
    44: [11],
    45: [12],
    46: [3, 5, 26, 35, 36, 43],
    47: [2],
    48: [4, 14, 24],
    49: [31, 36]
}

def bfs(graph, start):
    distances = {v: -1 for v in graph} # creating a dictionary where we set the value for each key to -1
    distances[start] = 0 # setting the first node to distance zero

    parents = {v: None for v in graph} # creating a dictionary where we set the value for each key to None
    parents[start] = start # setting the parent of the start node to itself
    Q = deque([start]) # creating a queue with the start node as the only initial value

    while Q: # runs as long as there is a value in Q
        u = Q.popleft() # pops the leftmost element and sets it equal to u -- u is a vertex in the graph
        for v in graph[u]: # loops through every out-degree vertex of vetex u
            if distances[v] == -1: # checks if the out-deg vertex has been visited
                distances[v] = distances[u] + 1 # adding one to the value of the out-deg vertex
                parents[v] = u # setting the parent of the out-deg vertex to the current vertex
                Q.append(v) # adding the out-deg vertex to the queue
    return distances, parents #returns both distances and parents

if __name__ == "__main__":
    start = 0 # defining the start node
    distances, parents = bfs(graph, start) # running bfs

    print("Distances:", distances)
    print("Parents:", parents)

# RUNTIME: O(n + m) where n = # vertices and m = # edges