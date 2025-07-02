import numpy as np

# Create 2D Array
Array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
print(Array)


# Inserting values in Rows
Array = np.insert(Array, 3, [13, 14, 15, 16], axis=0)
print(Array)


# Inserting values in Columns
Array = np.insert(Array, 4, [1, 1, 1, 1], axis=1)
print(Array)


# Access elements
print(Array[1][1])

def Access(Array, RowIndex, ColIndex):
    if RowIndex >= len(Array) or ColIndex >= len(Array[0]):
        print("Incorrect Index")
    else:
        print(Array[RowIndex][ColIndex])

Access(Array, 1, 1)


# Traversal of Array
for i in range(len(Array)):
    for j in range(len(Array)):
        print(Array[i][j])


# Search a value of an Array
def SearchElement(Array, Val):
    for i in range(len(Array)):
        for j in range(len(Array)):
            if Array[i][j] == Val:
                return f'Element Found at {i}row, {j}column'
    return "Element Not Found...."
print(SearchElement(Array, 100))

# Delete Element, Row, Column from an Array
new_arr = np.delete(Array, 0, axis=0)
print(new_arr)