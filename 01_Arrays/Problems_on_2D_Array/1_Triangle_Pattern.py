"""
Printing the triangle patterns.
"""
Arr = [
    [5, 10, 8],
    [7, 6, 3],
    [2, 1, 9]
]
n = len(Arr)
col = len(Arr[0])


######### Pattern 1: Print Upper Right Triangle #########
print("Upper Right Triangle")
for i in range(n):
    for j in range(col):
        if j >= i:
            print(Arr[i][j], end=" ")
        else:
            print('*', end = " ")
    print()

""" Output : 
5 10 8 
* 6 3 
* * 9 
"""


######### Pattern 2: Print Lower Left Triangle #########
print("Lower Left Triangle")
for i in range(n):
    for j in range(col):
        if j <= i:
            print(Arr[i][j], end=" ")
        else:
            print('*', end = " ")
    print()
    
""" Output:
5 * * 
7 6 * 
2 1 9 
"""

######### Pattern 3: Print Right Cross #########
print("Right Cross")
for i in range(n):
    for j in range(col):
        if j == i:
            print(Arr[i][j], end=" ")
        else:
            print('*', end = " ")
    print()

"""
5 * * 
* 6 * 
* * 9 
"""


######### Pattern 4: Print Left Cross #########
print("Left Cross")
for i in range(n):
    for j in range(col):
        if i + j == col - 1:
            print(Arr[i][j], end=" ")
        else:
            print('*', end=" ")
    print()


"""
* * 8 
* 6 * 
2 * * 
"""



# Time Complexity : O(N^2)
# Space Complexity : O(1)