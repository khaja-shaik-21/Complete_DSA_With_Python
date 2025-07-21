import numpy as np

def display_array(arr):
    print("Current Array:", arr)

def access_element(arr, index):
    if arr.size == 0:
        print("Array is empty.")
    elif -arr.size <= index < arr.size:
        print(f"Value at index {index}: {arr[index]}")
    else:
        print("Index out of range.")

def search_element(arr, value):
    for i in range(arr.size):
        if arr[i] == value:
            return i
    return -1

def main():
    my_array = np.array([], dtype=int)
    print("Initialized an empty NumPy array.")

    while True:
        print("\n==== NumPy Array Menu ====")
        print("1. Insert element")
        print("2. Traverse array")
        print("3. Access element by index")
        print("4. Search element")
        print("5. Delete element by value")
        print("6. Display array")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            try:
                val = int(input("Enter value to insert: "))
                pos = int(input("Enter position to insert (0-based index): "))

                if my_array.size == 0:
                    if pos >= 0:
                        my_array = np.insert(my_array, 0, val)
                        print(f"Array was empty. Inserted {val} at index 0.")
                    else:
                        print("Invalid position. Only position 0 is allowed in an empty array.")
                else:
                    if 0 <= pos <= my_array.size:
                        my_array = np.insert(my_array, pos, val)
                        print(f"Inserted {val} at index {pos}.")
                    elif pos == -1 or pos > my_array.size:
                        my_array = np.insert(my_array, my_array.size, val)
                        print(f"Inserted {val} at the end (index {my_array.size - 1}).")
                    else:
                        print("Invalid position. Use a valid index (0 to length) or -1 to append at end.")

                display_array(my_array)

            except ValueError:
                print("Invalid input! Please enter integers.")

        elif choice == '2':
            if my_array.size == 0:
                print("Array is empty.")
            else:
                print("Traversing array:")
                for item in my_array:
                    print(item)

        elif choice == '3':
            try:
                idx = int(input("Enter index to access: "))
                access_element(my_array, idx)
            except ValueError:
                print("Invalid input! Please enter an integer.")

        elif choice == '4':
            try:
                val = int(input("Enter value to search: "))
                result = search_element(my_array, val)
                if result != -1:
                    print(f"Value {val} found at index {result}")
                else:
                    print("Value not found!")
            except ValueError:
                print("Invalid input! Please enter an integer.")

        elif choice == '5':
            try:
                val = int(input("Enter value to delete: "))
                index = np.where(my_array == val)[0]
                if index.size > 0:
                    my_array = np.delete(my_array, index[0])
                    print(f"Deleted value {val} successfully.")
                    display_array(my_array)
                else:
                    print("Value not found in the array!")
            except ValueError:
                print("Invalid input! Please enter an integer.")

        elif choice == '6':
            display_array(my_array)

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()




#############   Time & Space Complexity Table: NumPy 1D Array Operations  ############

# | Operation        | Time Complexity | Space Complexity | Notes                                                               |
# | ---------------- | --------------- | ---------------- | ------------------------------------------------------------------- |
# | insert(val, pos) | O(n)            | O(n)             | Inserts value at specific position, creates a new copy of the array |
# | traverse()       | O(n)            | O(1)             | Iterates through each element                                       |
# | access(index)    | O(1)            | O(1)             | Supports both positive and valid negative indexing                  |
# | search(value)    | O(n)            | O(1)             | Linear search through array                                         |
# | delete(value)    | O(n)            | O(n)             | Deletes first occurrence; uses np.delete (creates new array)        |
# | display\_array() | O(n)            | O(1)             | Just prints elements                                                |
# | display\_menu()  | O(1)            | O(1)             | Constant time menu rendering                                        |
