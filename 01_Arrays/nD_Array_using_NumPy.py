import numpy as np


# Initially Empty N-Dimensional Array
nDArray = np.array([])


# Function to Create N-Dimensional Array
def create_array():
    global nDArray

    # Taking Number of Dimensions
    while True:
        try:
            dimensions = int(
                input("Enter the number of dimensions: ")
            )
            if dimensions <= 0:
                print(
                    "Dimensions must be greater than 0."
                )
            else:
                break

        except ValueError:
            print(
                "Please enter a valid integer value."
            )

    # Taking Size of Each Dimension
    shape = []
    
    for i in range(dimensions):
        while True:
            try:
                size = int(
                    input(
                        f"Enter size of Dimension {i + 1}: "
                    )
                )
                if size <= 0:
                    print(
                        "Size must be greater than 0."
                    )
                else:
                    shape.append(size)
                    break

            except ValueError:
                print(
                    "Please enter a valid integer value."
                )

    # Create Empty Array Filled with Zeros
    nDArray = np.zeros(tuple(shape), dtype=int)

    print("\nN-Dimensional Array Created Successfully.")

    print(nDArray)


# Function to Display Array
def display_array():
    global nDArray

    if nDArray.size == 0:
        print("Array is empty.")
    else:
        print("\nCurrent N-Dimensional Array:")
        print(nDArray)


# Function to Insert/Update Value
def insert_value(indices, value):

    global nDArray
    try:
        nDArray[tuple(indices)] = value
        print(
            f"Inserted {value} at index {indices}"
        )

    except IndexError:
        print("Index out of range.")


# Function to Access Element
def access_element(indices):

    global nDArray

    try:
        print(
            f"Value at index {indices} : "
            f"{nDArray[tuple(indices)]}"
        )

    except IndexError:
        print("Index out of range.")


# Function to Update Element
def update_element(indices, new_value):

    global nDArray

    try:
        old_value = nDArray[tuple(indices)]
        nDArray[tuple(indices)] = new_value
        print(
            f"Value updated successfully "
            f"from {old_value} to {new_value}"
        )

    except IndexError:
        print("Index out of range.")


# Function to Traverse Array
def traverse_array():

    global nDArray
    
    print("\nTraversing Array:")

    for element in np.nditer(nDArray):
        print(element, end=' ')

    print()


# Function to Search Element
def search_element(value):

    global nDArray

    result = np.argwhere(nDArray == value)

    if len(result) > 0:
        for index in result:
            print(
                f"Element found at index "
                f"{tuple(index)}"
            )
    else:
        print("Element not found.")


# Function to Delete Element
def delete_element(indices):

    global nDArray

    try:
        nDArray[tuple(indices)] = 0
        print(
            f"Element at index {indices} "
            f"deleted successfully."
        )

    except IndexError:
        print("Index out of range.")


# Function to Take Indices Input
def get_indices():

    global nDArray

    indices = []

    for i in range(nDArray.ndim):
        while True:
            try:
                index = int(
                    input(
                        f"Enter index for Dimension {i + 1}: "
                    )
                )
                indices.append(index)
                break

            except ValueError:
                print(
                    "Please enter a valid integer value."
                )

    return indices


# Menu Driven Program
def menu():
    while True:
        print("\n===== N-DIMENSIONAL ARRAY MENU =====")

        print("1. Create N-Dimensional Array")
        print("2. Display Array")
        print("3. Insert Value")
        print("4. Access Element")
        print("5. Update Element")
        print("6. Traverse Array")
        print("7. Search Element")
        print("8. Delete Element")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        # Create Array
        if choice == '1':
            create_array()

        # Display Array
        elif choice == '2':
            display_array()

        # Insert Value
        elif choice == '3':
            if nDArray.size == 0:
                print("Please create the array first.")
            else:
                indices = get_indices()
                while True:
                    try:
                        value = int(
                            input("Enter value: ")
                        )
                        break

                    except ValueError:
                        print(
                            "Please enter a valid integer value."
                        )

                insert_value(indices, value)

        # Access Element
        elif choice == '4':
            if nDArray.size == 0:
                print("Please create the array first.")

            else:
                indices = get_indices()
                access_element(indices)

        # Update Element
        elif choice == '5':
            if nDArray.size == 0:
                print("Please create the array first.")

            else:
                indices = get_indices()
                while True:
                    try:
                        new_value = int(
                            input("Enter new value: ")
                        )
                        break

                    except ValueError:
                        print(
                            "Please enter a valid integer value."
                        )

                update_element(indices, new_value)

        # Traverse Array
        elif choice == '6':
            if nDArray.size == 0:
                print("Please create the array first.")

            else:
                traverse_array()

        # Search Element
        elif choice == '7':
            if nDArray.size == 0:
                print("Please create the array first.")
            else:
                while True:
                    try:
                        value = int(
                            input("Enter value to search: ")
                        )
                        break

                    except ValueError:
                        print(
                            "Please enter a valid integer value."
                        )

                search_element(value)

        # Delete Element
        elif choice == '8':
            if nDArray.size == 0:
                print("Please create the array first.")

            else:
                indices = get_indices()
                delete_element(indices)

        # Exit
        elif choice == '9':
            print("Exiting program.")
            break

        # Invalid Choice
        else:
            print(
                "Invalid choice. "
                "Please enter a number between 1 and 9."
            )


# Main Function
if __name__ == "__main__":

    menu()



############# Time & Space Complexity Table: N-Dimensional Array Operations ############

# | Method             | Time Complexity | Space Complexity | Notes                                                  |
# | ------------------ | --------------- | ---------------- | ------------------------------------------------------ |
# | create_array()     | O(n)            | O(n)             | Creates entire N-Dimensional array                     |
# | display_array()    | O(n)            | O(1)             | Prints all elements                                    |
# | insert_value()     | O(1)            | O(1)             | Direct indexing insertion                              |
# | access_element()   | O(1)            | O(1)             | Direct indexing access                                 |
# | update_element()   | O(1)            | O(1)             | Direct indexing update                                 |
# | traverse_array()   | O(n)            | O(1)             | Visits every element once                              |
# | search_element()   | O(n)            | O(k)             | Searches all elements, stores matching indices         |
# | delete_element()   | O(1)            | O(1)             | Replaces value with 0                                  |
# | get_indices()      | O(d)            | O(d)             | d = number of dimensions                               |
# | menu()             | O(1) per op     | O(1)             | Menu handling only                                     |