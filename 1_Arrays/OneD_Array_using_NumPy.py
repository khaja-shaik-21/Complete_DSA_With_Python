import numpy as np

# Create an One Dimensional NumPy Array
my_array = np.array([1, 2, 3, 4], dtype=int)
print(my_array)


# Inserting the values in the NumPy Array
my_array = np.insert(my_array, 0, 5, axis=None) # Inserting at the begining of the Array
print(my_array)
my_array = np.insert(my_array, 2, 6, axis=None) # Inserting in the Middle of the Array
print(my_array)
my_array = np.insert(my_array, 6, 7, axis=None) # Inserting in the End of the Array, here you to gave the exact index of len of the array to insert at end.
print(my_array)
my_array = np.insert(my_array, len(my_array), 8, axis=None) # Inserting in the End of the Array using len of the array.
print(my_array)


# Traversing One Dimensional NumPy Array
for i in my_array:
    print(i)


# Access values in the NumPy Array
def AccessElement(my_array, index):
    if index >= my_array.size:
        print('Index out of Range')
    else:
        print(f'Value:{my_array[index]} at index:{index}')
AccessElement(my_array, 7)


# Searching values in the NumPy Array using Linear Search
def searchElement(array, value):
    for i in range(array.size):
        if array[i] == value:
            return i
    return -1
print(searchElement(my_array, 6))


# delete the values from the NumPy array
index = np.where(my_array == 10)[0]  # Find the index of value 6 and assign that index as 0
if index.size > 0:
    my_array = np.delete(my_array, index[0])
print(my_array)