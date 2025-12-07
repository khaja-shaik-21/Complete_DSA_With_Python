""" 
Given an m x n matrix, return all elements of the matrix in spiral order.
 1 →  2 →  3
           ↓
 4 →  5    6
 ↑         ↓
 7 ←  8 ←  9

"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]

result = []

top, left = 0, 0

bottom, right = len(matrix) - 1, len(matrix[0]) - 1

while top <= bottom and left<= right:       # O(N)
    for i in range(left, right + 1):        # O(M)
        result.append(matrix[top][i])
    top += 1
    
    for i in range(top, bottom + 1):        # O(M)
        result.append(matrix[i][right])
    right -= 1
    
    if top <= bottom:
        for i in range(right, left-1, -1):  # O(M)
            result.append(matrix[bottom][i])
        bottom -= 1
    
    if left <= right:
        for i in range(bottom, top-1, -1):  # O(M)
            result.append(matrix[i][left])
        left += 1

print(result)   # [1, 2, 3, 6, 9, 8, 7, 4, 5]

# Time Complexity : O(N*(O(M)+O(M)+O(M)+O(M)) = O(N*(O(4M))) = O(N*M)
# Space Complexity : O(1) or O(N*M)