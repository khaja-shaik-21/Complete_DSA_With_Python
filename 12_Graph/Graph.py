# Graph using Adjacency List

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def addEdge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list:
            self.addVertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.addVertex(vertex2)
        
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        else:
            print(f"Edge already exists from '{vertex1}' to '{vertex2}'")
        
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)
        else:
            print(f"Edge already exists from '{vertex2}' to '{vertex1}'")

    def removeEdge(self, vertex1, vertex2):
        removed = False
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
                removed = True
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)
                removed = True
        return removed

    def removeVertex(self, vertex):
        if vertex in self.adjacency_list:
            for otherVertex in self.adjacency_list[vertex]:
                if vertex in self.adjacency_list[otherVertex]:
                    self.adjacency_list[otherVertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    # Graph Traversal
    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]

        while queue:
            curr_vertex = queue.pop(0)
            print(curr_vertex, end=" ")

            for adj_vertex in self.adjacency_list[curr_vertex]:
                if adj_vertex not in visited:
                    visited.add(adj_vertex)
                    queue.append(adj_vertex)
    
    # Graph Traversal
    def dfs(self, vertex):
        visited = set()
        stack = [vertex]

        while stack:
            curr_vertex = stack.pop()
            if curr_vertex not in visited:
                print(curr_vertex, end=" ")
                visited.add(curr_vertex)

                for adj_vertex in self.adjacency_list[curr_vertex]:
                    if adj_vertex not in visited:
                        stack.append(adj_vertex)
            
    def printGraph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])



if __name__ == "__main__":
    g = Graph()
    while True:
        print("\n==== Graph Menu ====")
        print("1. Add Vertex")
        print("2. Add Edge")
        print("3. Display Graph")
        print("4. Remove Edge")
        print("5. Remove Vertex")
        print("6. Graph Traversal Using BFS")
        print("7. Graph Traversal Using DFS")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            vertex = input("Enter vertex label: ")
            if g.addVertex(vertex):
                print(f"Vertex '{vertex}' added.")
            else:
                print(f"Vertex '{vertex}' already exists.")

        elif choice == '2':
            v1 = input("Enter first vertex: ")
            v2 = input("Enter second vertex: ")
            g.addEdge(v1, v2)

        elif choice == '3':
            print("\nGraph adjacency list:")
            g.printGraph()

        elif choice == '4':
            v1 = input("Enter first vertex: ")
            v2 = input("Enter second vertex: ")
            if g.removeEdge(v1, v2):
                print(f"Edge between '{v1}' and '{v2}' is removed.")
            else:
                print(f"No edge exists between '{v1}' and '{v2}'.")

        elif choice == '5':
            v = input("Enter the Vertex: ")
            if g.removeVertex(v):
                print(f"Vertex '{v}' is deleted.")
            else:
                print(f"Vertex '{v}' does not exist.")

        elif choice == '6':
            if not g.adjacency_list:
                print("Graph is empty. Add vertices first.")
            else:
                start = input("Enter start vertex for BFS: ")
                g.dfs(start)
        
        elif choice == '7':
            if not g.adjacency_list:
                print("Graph is empty. Add vertices first.")
            else:
                start = input("Enter start vertex for DFS: ")
                g.dfs(start)
        
        elif choice == '8':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


#############   Time & Space Complexity Table: Undirected Graph (Adjacency List)   #############

# | Operation              | Time Complexity   | Space Complexity   | Notes                                                   |
# |------------------------|-------------------|--------------------|---------------------------------------------------------|
# | addVertex(vertex)      | O(1)              | O(1)               | Constant time to check and add vertex if not present    |
# | addEdge(v1, v2)        | O(1) avg          | O(1) per edge      | Appends edge to both vertex lists (undirected)          |
# | removeEdge(v1, v2)     | O(E/V) worst      | O(1)               | List removal takes linear time per vertex's edge list   |
# | removeVertex(v)        | O(E)              | O(1)               | Remove vertex from all adjacency lists                  |
# | printGraph()           | O(V + E)          | O(1)               | Iterates over all vertices and their edges              |
# | BFS traversal	       | O(V + E)	       | O(V)	            | Uses queue and visited set                              |
# | DFS traversal          | O(V + E)          | O(V)               | Uses Stack and visited set                              |