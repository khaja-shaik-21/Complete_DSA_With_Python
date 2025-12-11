"""
BFS Traversal of a Adjacency List starting from vertex 1
"""

from collections import deque

def bfs(n, adj, node):
    ans = []
    queue = deque()
    visited = [0 for _ in range(n+1)]
    
    queue.append(node)         # Starting Vertex 1
    visited[node] = 1
    
    while len(queue) != 0:
        e = queue.popleft()
        ans.append(e)
        
        for node in adj[e]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = 1
    return ans


n = 9
node = 1
adj = [
        [1, 2], 
        [2, 4], 
        [3, 4], 
        [1, 3], 
        [3, 5], 
        [5, 4]
    ]
print(bfs(n, adj, node)) # [1, 2, 4, 3, 5]


"""
BFS Traversal of a Adjacency List starting from vertex 0
"""

class Solution:
    def bfs(self, adj):
        # code here
        ans = []
        queue = deque()
        visited = [0 for _ in range(len(adj)+1)]
        
        queue.append(0)         # Starting Vertex 0
        visited[0] = 1
        
        while len(queue) != 0:
            e = queue.popleft()
            ans.append(e)
            
            for node in adj[e]:
                if visited[node] == 0:
                    queue.append(node)
                    visited[node] = 1
        return ans

adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

result = Solution()
print(result.bfs(adj))


# Time Complexity: O(V + E)
# Space Complexity: O(V)