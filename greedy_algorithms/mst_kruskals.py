G = [
    [[2, 459], [4, 46], [7, 144], [8, 420], [11, 589], [14, 185], [16, 127], [23, 758], [25, 158], [26, 569]], 
    [[1, 459], [3, 48], [4, 496], [5, 543], [6, 753], [10, 183], [11, 339], [16, 573], [18, 595], [26, 445], [29, 278], [30, 887]], 
    [[2, 48], [4, 643], [5, 399], [11, 317], [19, 402], [20, 632], [21, 759], [26, 748], [27, 234], [30, 507]], 
    [[3, 643], [5, 885], [1, 46], [2, 496], [7, 308], [9, 779], [10, 531], [14, 468], [20, 511], [29, 33], [30, 409]], 
    [[4, 885], [6, 791], [2, 543], [3, 399], [7, 321], [12, 401], [14, 889], [19, 328], [21, 764], [22, 11], [24, 28], [27, 540], [29, 865], [30, 213]], 
    [[5, 791], [7, 654], [2, 753], [8, 834], [10, 323], [17, 489], [22, 801], [26, 843]], 
    [[6, 654], [8, 279], [1, 144], [4, 308], [5, 321], [11, 559], [12, 446], [14, 106], [15, 642], [21, 248], [23, 702], [24, 661], [30, 119]], 
    [[7, 279], [9, 52], [1, 420], [6, 834], [13, 166], [16, 684], [19, 246], [23, 683], [26, 847], [29, 551]], 
    [[8, 52], [10, 533], [4, 779], [11, 741], [12, 782], [13, 712], [15, 772], [18, 770], [19, 47], [20, 793], [21, 284], [28, 469]], 
    [[9, 533], [11, 126], [2, 183], [4, 531], [6, 323], [12, 560], [14, 594], [16, 303], [18, 746], [21, 274], [23, 84], [28, 230], [30, 832]], 
    [[10, 126], [12, 156], [1, 589], [2, 339], [3, 317], [7, 559], [9, 741], [13, 627], [28, 118]], 
    [[11, 156], [13, 458], [5, 401], [7, 446], [9, 782], [10, 560], [22, 350], [28, 650], [29, 151]], 
    [[12, 458], [14, 839], [8, 166], [9, 712], [11, 627], [16, 390], [22, 75], [27, 417], [28, 41], [30, 655]], 
    [[13, 839], [15, 434], [1, 185], [4, 468], [5, 889], [7, 106], [10, 594], [16, 617], [20, 802], [21, 603], [24, 501], [26, 591], [29, 299], [30, 689]], 
    [[14, 434], [16, 406], [7, 642], [9, 772], [26, 349], [27, 347], [29, 377]], 
    [[15, 406], [17, 848], [1, 127], [2, 573], [8, 684], [10, 303], [13, 390], [14, 617], [18, 700], [22, 667], [23, 827]], 
    [[16, 848], [18, 96], [6, 489], [20, 275], [21, 600]], 
    [[17, 96], [19, 792], [2, 595], [9, 770], [10, 746], [16, 700], [24, 735], [25, 171], [29, 174]], 
    [[18, 792], [20, 675], [3, 402], [5, 328], [8, 246], [9, 47], [21, 137], [24, 87]], 
    [[19, 675], [21, 717], [3, 632], [4, 511], [9, 793], [14, 802], [17, 275], [26, 42], [27, 67]], 
    [[20, 717], [22, 200], [3, 759], [5, 764], [7, 248], [9, 284], [10, 274], [14, 603], [17, 600], [19, 137], [25, 241]], 
    [[21, 200], [23, 636], [5, 11], [6, 801], [12, 350], [13, 75], [16, 667], [27, 546]], 
    [[22, 636], [24, 586], [1, 758], [7, 702], [8, 683], [10, 84], [16, 827], [26, 740], [27, 548], [30, 705]], 
    [[23, 586], [25, 692], [5, 28], [7, 661], [14, 501], [18, 735], [19, 87], [27, 561]], 
    [[24, 692], [26, 295], [1, 158], [18, 171], [21, 241], [27, 886]], 
    [[25, 295], [27, 611], [1, 569], [2, 445], [3, 748], [6, 843], [8, 847], [14, 591], [15, 349], [20, 42], [23, 740]], 
    [[26, 611], [28, 547], [3, 234], [5, 540], [13, 417], [15, 347], [20, 67], [22, 546], [23, 548], [24, 561], [25, 886]], 
    [[27, 547], [29, 557], [9, 469], [10, 230], [11, 118], [12, 650], [13, 41], [30, 99]], 
    [[28, 557], [30, 386], [2, 278], [4, 33], [5, 865], [8, 551], [12, 151], [14, 299], [15, 377], [18, 174]], 
    [[29, 386], [2, 887], [3, 507], [4, 409], [5, 213], [7, 119], [10, 832], [13, 655], [14, 689], [23, 705], [28, 99]]
]

# helper to check if u and v are connected in the current MST (F)
# this implements the logic: "run BFS on (V, F) to check if endpoints are already connected"
def is_connected_bfs(u, v, current_edges, n):
    # builds a temporary adjacency list for the current forest F
    adj = {i: [] for i in range(1, n + 1)}
    for edge in current_edges:
        node1, node2, _ = edge
        adj[node1].append(node2)
        adj[node2].append(node1)
    
    # BFS
    queue = [u]
    visited = {u}
    
    while queue:
        curr = queue.pop(0)
        if curr == v:
            return True
        for neighbor in adj[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

def kruskal(G_input):
    # flatten adjacency list into edge list
    edges = []
    seen_edges = set()
    n = len(G_input)

    for i in range(n):
        u = i + 1  # for the 1-based index
        for neighbor_info in G_input[i]:
            v = neighbor_info[0]
            w = neighbor_info[1]
            
            # makes sure we only add the edge once
            if u < v:
                edges.append((u, v, w))

    # sort edges by increasing weight
    edges.sort(key=lambda x: x[2])
    
    # empty list of edges
    F = []
    
    #iterating thru the sorted edges
    for edge in edges:
        u, v, w = edge
        
        # check if F + e is acyclic by checking if u and v are already connected
        if not is_connected_bfs(u, v, F, n):
            # if not connected, adding this edge won't create a cycle
            F.append(edge)
            
    return F

if __name__ == "__main__":
    result_mst = kruskal(G)

    result_mst.sort(key=lambda x: x[2])
    print(f"Number of edges in MST: {len(result_mst)}")
    print(f"First 5 edges: {result_mst[:5]}")
    
    total_weight = sum(w for _, _, w in result_mst)
    print(f"Total MST Weight: {total_weight}")

# RUNTIME: O(m^2) 
# 1. Sorting E takes O(m log m).
# 2. The algorithm iterates m times (once for each edge).
# 3. In each iteration, we run BFS on the current forest (V, F) to check for cycles.
#    Since (V, F) is a forest with at most n - 1 edges, BFS takes O(n).
# 4. Total time = O(m log m) + m * O(n) = O(mn).
#    Since m can be up to O(n^2), this is effectively O(m^2).