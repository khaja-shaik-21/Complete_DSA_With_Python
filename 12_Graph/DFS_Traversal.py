"""
DFS of Graph Traversal of the Adjacency List
"""
############ Method 1: ##############
def dfs(node, visited, adj, result):
    visited[node] = 1
    result.append(node)

    for nei in adj[node]:
        if not visited[nei]:
            dfs(nei, visited, adj, result)


adj = [
    [],         # 0 (not used)
    [2, 3],     # 1 → 2,3
    [4],        # 2 → 4
    [4, 5],     # 3 → 4,5
    [],         # 4
    [6],        # 5 → 6
    []          # 6
]

n = len(adj) - 1
visited = [0] * (n + 1)
result = []

dfs(1, visited, adj, result)
print(result)       #   [1, 2, 4, 3, 5, 6]



class Solution:
    def dfs(self, adj):
        n = len(adj) - 1     # 1-based indexing
        visited = [0] * (n + 1)
        result = []

        def travers(node):
            visited[node] = 1
            result.append(node)

            for nei in adj[node]:
                if not visited[nei]:
                    travers(nei)

        # run DFS starting from node 1
        travers(1)

        return result


adj = [
    [],         # 0 (not used)
    [2, 3],     # 1 → 2,3
    [4],        # 2 → 4
    [4, 5],     # 3 → 4,5
    [],         # 4
    [6],        # 5 → 6
    []          # 6
]

sol = Solution()
print(sol.dfs(adj))

# Time Complexity = O(V + E)    
# Space Complexity = O(V)       visited[] → O(V), result[] → O(V)