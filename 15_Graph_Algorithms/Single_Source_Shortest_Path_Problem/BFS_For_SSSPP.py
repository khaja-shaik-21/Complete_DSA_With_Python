# BFS For Single Source Shortest Path Problem (SSSPP)

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs_ssspp(self, start, end):
        queue = []
        queue.append([start])
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node == end:
                return path
            for adj in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)
                
customdict = {
    'a': ["b", "c"],
    'b': ["d", "g"],
    'c': ["d", "e"],
    'd': ["f"],
    'e': ["f"],
    'g': ["f"]
}

g = Graph(customdict)

result = g.bfs_ssspp("a", "g")
print(result)


#############   Time & Space Complexity Table: BFS For Single Source Shortest Path Problem (SSSPP)  #############

# Time Complexity :  O(V+E)
# Space Complexity : O(E)