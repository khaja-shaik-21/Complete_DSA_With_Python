"""
The transpose of a matrix is obtained by swapping rows and columns.
"""

A = [
    [1, 2, 3],
    [4, 5, 6]
]


######### Method 1: Works for any matrix #########
rows = len(A)
cols = len(A[0])

transpose = [[0] * rows for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        transpose[j][i] = A[i][j]

print(transpose)    # [[1, 4], [2, 5], [3, 6]]



######### Method 2: Only for Square Matrix #########

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = len(A)
for i in range(n):
    for j in range(i + 1, n):
        A[i][j], A[j][i] = A[j][i], A[i][j]

print(A)        # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Time Complexity : O(N^2)
# Space Complexity : O(1)