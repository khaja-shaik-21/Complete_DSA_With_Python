import array

# Create an One Dimensional Array
my_array = array.array('i', [1, 2, 3, 4])
print(my_array)


# Inserting the values in the Array
my_array.insert(0, 5)   # Inserting at the begining of the Array
print(my_array)
my_array.insert(2, 6)   # Inserting in the Middle of the Array
print(my_array)
my_array.insert(10, 7)  # Inserting in the End of the Array, here if you give the index value out of the index also it adds into the end of array.
print(my_array)


# Traversing One Dimensional Array
for i in my_array:
    print(i)


# Access values in the Array
def AccessElement(my_array, index):
    if index >= len(my_array):
        print('Index out of Range')
    else:
        print(f'Value:{my_array[index]} at index:{index}')
AccessElement(my_array, 6)


# Searching values in the Array using Linear Search
def searchElement(Array, value):
    for i in range(len(Array)):
        if Array[i] == value:
            return i
    return -1
print(searchElement(my_array, 6))


# Remove the values from the array
my_array.remove(1)
print(my_array)