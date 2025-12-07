"""
Rotate Matrix by 90 degrees (clockwise).
"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)

######### Method 1: Bruit Force #########
result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        result[j][(n-1)-i] = matrix[i][j]
print(result)

# Time Complexity : O(N^2)
# Space Complexity : O(N^2)


######### Method 1: Optimal Code #########
def PrintMatrix(matrix, r, c):
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=" ")
        print()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
r = len(matrix)
c = len(matrix[0])
print("Before Rotate")
PrintMatrix(matrix, r, c)

for i in range(n-1):            # O(N)
    for j in range(i+1, n):     # O(N)
        if i == j:
            continue
        else:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in range(n):              # O(N)
    matrix[i].reverse()

print("After Rotate")
PrintMatrix(matrix, r, c)

# Time Complexity : (O(N)*O(N)) + O(N) = O(N^2) + O(N) = O(N^2)
# Space Complexity : O(1)