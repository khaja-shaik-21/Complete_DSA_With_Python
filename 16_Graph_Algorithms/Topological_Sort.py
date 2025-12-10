from collections import defaultdict

class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices
    
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)
    
    def topogologicalSortUtil(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topogologicalSortUtil(i, visited, stack)
        
        stack.insert(0, v)
    
    def topologicalSort(self):

        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topogologicalSortUtil(k, visited, stack)
        
        print(stack)


#############   Time & Space Complexity Table: Topological Sort Algorithm   #############

# | Algorithm        | Time Complexity | Space Complexity | Notes                            |
# | ---------------- | --------------- | ---------------- | -------------------------------- |
# | Topological Sort | O(V + E)        | O(V + E)         | Uses stack and visited array/set |
