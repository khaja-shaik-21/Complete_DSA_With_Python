"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

matrix = [[1,1,1],[1,0,1],[1,1,1]]
"""

######### Method 1: Bruit Force #########
def MarkInf(matrix, row, col):
    for i in range(r):
        if matrix[i][col] != 0:
            matrix[i][col] = float("inf")
    
    for j in range(r):
        if matrix[row][j] != 0:
            matrix[row][j] = float("inf")


def FindZeros(matrix):
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                MarkInf(matrix, i, j)

def PrintMatrix(matrix):
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=" ")
        print()

matrix = [[1,1,1],[1,0,1],[1,1,1]]

r = len(matrix)
c = len(matrix[0])

print("Before Set Zeros")
PrintMatrix(matrix)


FindZeros(matrix)

for i in range(r):
    for j in range(c):
        if matrix[i][j] == float("inf"):
            matrix[i][j] = 0
print("After Set Zeros")
PrintMatrix(matrix)


# Time Complexity : O(N*M)
# Space Complexity : O(1)





######### Method 2: Optimal Code #########
"""
     ┌──────────────-┐
     │ 0 │ -1│ -1│ 0 │  
     └──────────────-┘
┌───┐┌──────────────-┐
│ 0 ││ 7 │ 9 │ 2 │ 3 │
│-1 ││ 20│ 8 │ 0 │ 10│
│-1 ││ 29│ 0 │-10│ 5 │
│ 0 ││ 4 │ 14│ 6 │ 7 │
└───┘└──────────────-┘

"""

matrix = [[7,9, 2, 3],[20, 8, 0, 10],[29, 0, -10, 5], [4, 14, 6, 7]]
"""
"""

r = len(matrix)
c = len(matrix[0])
print("Before")
PrintMatrix(matrix)

row = [0 for _ in range(r)]
col = [0 for _ in range(c)]

for i in range(r):              # O(N)
    for j in range(c):          # O(M)
        if matrix[i][j] == 0:
            row[i] = -1
            col[j] = -1
for i in range(r):              # O(N)
    for j in range(c):          # O(M)
        if row[i] == -1 or col[j] == -1:
            matrix[i][j] = 0
print("After")
PrintMatrix(matrix)
""" 
Before                After
7  9  2  3            7 0 0 3 
20 8  0  10           0 0 0 0 
29 0 -10 5            0 0 0 0 
4  14 6  7            4 0 0 7 
"""

# Time Complexity : O(N*M) + O(N*M) = O(2(N*M)) = O(N*M)
# Space Complexity : O(N+M)
# N = no.of rows
# M = no.of colomns