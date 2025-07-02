import array

# Create a one-dimensional integer array
my_array = array.array('i', [])


# Function to display the array
def display_array():
    print("Current Array:", list(my_array))


# Function to insert an element
def insert_element(index, value):
    if index < 0:
        print("Invalid index. Cannot be negative.")
    else:
        if index > len(my_array):
            print("Index out of bounds. Appending at the end.")
            my_array.append(value)
            if len(my_array) == 1:
                print(f"Inserted {value} at index 0 ")
            else:
                print(f"Inserted {value} at index {len(my_array) - 1}")
        else:
            my_array.insert(index, value)
            print(f"Inserted {value} at index {index}")


# Function to traverse the array
def traverse_array():
    print("Traversing array:")
    for element in my_array:
        print(element, end=' ')
    print()


# Function to access an element by index
def access_element(index):
    if len(my_array) == 0:
        print("The array is empty. No elements to access.")
        return

    try:
        print(f"Value at index {index}: {my_array[index]}")
    except IndexError:
        print("Index out of range.")


# Function to search for an element
def search_element(value):
    for i in range(len(my_array)):
        if my_array[i] == value:
            print(f"Element {value} found at index {i}")
            return
    print(f"Element {value} not found.")


# Function to remove an element
def remove_element(value):
    try:
        my_array.remove(value)
        print(f"Removed {value} from the array")
    except ValueError:
        print(f"Element {value} not found in the array")


# Menu-driven interface
def menu():
    while True:
        print("\nMENU")
        print("1. Display Array")
        print("2. Insert Element")
        print("3. Traverse Array")
        print("4. Access Element by Index")
        print("5. Search for an Element")
        print("6. Remove Element")
        print("7. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            display_array()
        elif choice == '2':
            try:
                index = int(input("Enter index to insert at: "))
                value = int(input("Enter value to insert: "))
                insert_element(index, value)
            except ValueError:
                print("Please enter valid integer values.")
        elif choice == '3':
            traverse_array()
        elif choice == '4':
            try:
                index = int(input("Enter index to access: "))
                access_element(index)
            except ValueError:
                print("Please enter a valid integer index.")
        elif choice == '5':
            try:
                value = int(input("Enter value to search: "))
                search_element(value)
            except ValueError:
                print("Please enter a valid integer value.")
        elif choice == '6':
            try:
                value = int(input("Enter value to remove: "))
                remove_element(value)
            except ValueError:
                print("Please enter a valid integer value.")
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Start the menu
menu()


############# Time & Space Complexity Table: 1D Array using Python array Module ############

# | Method             | Time Complexity | Space Complexity | Notes                                                      |
# | ------------------ | --------------- | ---------------- | ---------------------------------------------------------- |
# |  insert_element()  | O(n)            | O(1)             | Worst case: shift elements to insert at given index        |
# |  access_element()  | O(1)            | O(1)             | Direct indexing (supports negative index with validation)  |
# |  search_element()  | O(n)            | O(1)             | Linear search; worst case is element not present           |
# |  remove_element()  | O(n)            | O(1)             | Searches + shifts all elements after the removed one       |
# |  traverse_array()  | O(n)            | O(1)             | Iterates over each element once                            |
# |  display_array()   | O(n)            | O(1)             | Prints all elements; linear pass                           |
# |  menu()            | O(1) per op     | O(1)             | Menu logic constant, user input based                      |
