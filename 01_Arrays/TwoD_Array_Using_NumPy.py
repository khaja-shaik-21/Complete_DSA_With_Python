import numpy as np


# Initially Empty 2D Array
twoDarr = np.array([[]], dtype=int)


# Function to Create 2D Array
def create_array():
    global twoDarr

    # Taking Rows and Columns
    while True:
        try:
            rows = int(
                input("Enter the number of rows: ")
            )
            cols = int(
                input("Enter the number of columns: ")
            )
            if rows <= 0 or cols <= 0:
                print(
                    "Rows and columns must be greater than 0."
                )
            else:
                break

        except ValueError:
            print(
                "Please enter valid integer values."
            )

    # Taking Elements from User
    elements = []

    print(
        f"\nEnter {rows * cols} elements for the 2D Array:"
    )

    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    value = int(
                        input(
                            f"Enter element at [{i}][{j}] : "
                        )
                    )

                    row.append(value)
                    break

                except ValueError:
                    print(
                        "Please enter a valid integer value."
                    )

        elements.append(row)

    # Create NumPy 2D Array
    twoDarr = np.array(elements, dtype=int)

    print("\n2D Array Created Successfully.")

    print(twoDarr)


# Function to Display Array
def display_array():
    if twoDarr.size == 0:
        print("Array is empty.")
    else:
        print("\nCurrent 2D Array:")
        print(twoDarr)


# Function to Insert Single Value
def insert_value(row, col, value):
    global twoDarr

    # Check Valid Index
    if (
        row < 0
        or col < 0
        or row >= twoDarr.shape[0]
        or col >= twoDarr.shape[1]
    ):
        print("Index out of range.")
    else:
        twoDarr[row][col] = value
        print(
            f"Inserted {value} at "
            f"Row {row}, Column {col}"
        )


# Function to Insert Row
def insert_row(index, values):
    global twoDarr
    if len(values) != twoDarr.shape[1]:
        print(
            f"Row must contain exactly "
            f"{twoDarr.shape[1]} values."
        )
    else:
        if index < 0:
            print("Invalid row index.")
        elif index > len(twoDarr):
            print("Index out of bounds. Appending row at end.")

            twoDarr = np.insert(
                twoDarr,
                len(twoDarr),
                values,
                axis=0
            )
        else:
            twoDarr = np.insert(
                twoDarr,
                index,
                values,
                axis=0
            )
        print("Row inserted successfully.")


# Function to Insert Column
def insert_column(index, values):
    global twoDarr
    if len(values) != twoDarr.shape[0]:
        print(
            f"Column must contain exactly "
            f"{twoDarr.shape[0]} values."
        )
    else:
        if index < 0:
            print("Invalid column index.")
        elif index > twoDarr.shape[1]:
            print(
                "Index out of bounds. "
                "Appending column at end."
            )

            twoDarr = np.insert(
                twoDarr,
                twoDarr.shape[1],
                values,
                axis=1
            )
        else:
            twoDarr = np.insert(
                twoDarr,
                index,
                values,
                axis=1
            )

        print("Column inserted successfully.")


# Function to Access Element
def access_element(row, col):
    if (
        row < 0
        or col < 0
        or row >= twoDarr.shape[0]
        or col >= twoDarr.shape[1]
    ):
        print("Index out of range.")

    else:
        print(
            f"Value at [{row}][{col}] : "
            f"{twoDarr[row][col]}"
        )


# Function to Update Element
def update_element(row, col, new_value):
    global twoDarr

    # Check Valid Index
    if (
        row < 0
        or col < 0
        or row >= twoDarr.shape[0]
        or col >= twoDarr.shape[1]
    ):
        print("Index out of range.")

    else:
        old_value = twoDarr[row][col]

        twoDarr[row][col] = new_value

        print(
            f"Value updated successfully "
            f"from {old_value} to {new_value}"
        )


# Function to Traverse Array
def traverse_array():
    print("\nTraversing 2D Array:")
    for i in range(twoDarr.shape[0]):
        for j in range(twoDarr.shape[1]):
            print(twoDarr[i][j], end=' ')
        print()


# Function to Search Element
def search_element(value):
    for i in range(twoDarr.shape[0]):
        for j in range(twoDarr.shape[1]):
            if twoDarr[i][j] == value:
                print(
                    f"Element found at "
                    f"Row {i}, Column {j}"
                )
                return

    print("Element not found.")


# Function to Delete Row
def delete_row(index):
    global twoDarr
    if index < 0 or index >= twoDarr.shape[0]:
        print("Invalid row index.")
    else:
        twoDarr = np.delete(
            twoDarr,
            index,
            axis=0
        )
        print(f"Row {index} deleted successfully.")


# Function to Delete Column
def delete_column(index):
    global twoDarr
    if index < 0 or index >= twoDarr.shape[1]:
        print("Invalid column index.")
    else:
        twoDarr = np.delete(
            twoDarr,
            index,
            axis=1
        )
        print(f"Column {index} deleted successfully.")


# Menu Driven Program
def menu():
    while True:
        print("\n===== 2D ARRAY MENU =====")

        print("1. Create 2D Array")
        print("2. Display Array")
        print("3. Insert Single Value")
        print("4. Insert Row")
        print("5. Insert Column")
        print("6. Traverse Array")
        print("7. Access Element")
        print("8. Update Element")
        print("9. Search Element")
        print("10. Delete Row")
        print("11. Delete Column")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        # Create Array
        if choice == '1':
            create_array()

        # Display Array
        elif choice == '2':
            display_array()

        # Insert Single Value
        elif choice == '3':
            while True:
                try:
                    row = int(
                        input("Enter row index: ")
                    )
                    col = int(
                        input("Enter column index: ")
                    )
                    value = int(
                        input("Enter value: ")
                    )
                    break

                except ValueError:
                    print(
                        "Please enter valid integer values."
                    )

            insert_value(row, col, value)

        # Insert Row
        elif choice == '4':
            while True:
                try:
                    index = int(
                        input("Enter row index: ")
                    )
                    break

                except ValueError:
                    print(
                        "Please enter a valid integer index."
                    )

            while True:
                try:
                    values = list(
                        map(
                            int,
                            input(
                                f"Enter {twoDarr.shape[1]} "
                                f"row values separated by spaces: "
                            ).split()
                        )
                    )
                    break

                except ValueError:
                    print(
                        "Please enter valid integer values."
                    )

            insert_row(index, values)

        # Insert Column
        elif choice == '5':
            while True:
                try:
                    index = int(
                        input("Enter column index: ")
                    )
                    break

                except ValueError:
                    print(
                        "Please enter a valid integer index."
                    )

            while True:
                try:
                    values = list(
                        map(
                            int,
                            input(
                                f"Enter {twoDarr.shape[0]} "
                                f"column values separated by spaces: "
                            ).split()
                        )
                    )
                    break

                except ValueError:
                    print(
                        "Please enter valid integer values."
                    )

            insert_column(index, values)

        # Traverse Array
        elif choice == '6':
            traverse_array()

        # Access Element
        elif choice == '7':
            while True:
                try:
                    row = int(
                        input("Enter row index: ")
                    )
                    col = int(
                        input("Enter column index: ")
                    )
                    break

                except ValueError:
                    print(
                        "Please enter valid integer indices."
                    )

            access_element(row, col)

        # Update Element
        elif choice == '8':
            while True:
                try:
                    row = int(
                        input("Enter row index: ")
                    )
                    col = int(
                        input("Enter column index: ")
                    )
                    new_value = int(
                        input("Enter new value: ")
                    )
                    break

                except ValueError:
                    print(
                        "Please enter valid integer values."
                    )

            update_element(row, col, new_value)

        # Search Element
        elif choice == '9':
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

        # Delete Row
        elif choice == '10':
            while True:
                try:
                    index = int(
                        input("Enter row index to delete: ")
                    )
                    break

                except ValueError:
                    print(
                        "Please enter a valid integer index."
                    )

            delete_row(index)

        # Delete Column
        elif choice == '11':
            while True:
                try:
                    index = int(
                        input("Enter column index to delete: ")
                    )
                    break

                except ValueError:
                    print(
                        "Please enter a valid integer index."
                    )

            delete_column(index)

        # Exit
        elif choice == '12':
            print("Exiting program.")
            break

        # Invalid Choice
        else:
            print(
                "Invalid choice. "
                "Please enter a number between 1 and 12."
            )


# Main Function
if __name__ == "__main__":
    
    menu()



############# Time & Space Complexity Table: NumPy 2D Array Operations ############

# | Method            | Time Complexity | Space Complexity | Notes                                                  |
# | ----------------- | --------------- | ---------------- | ------------------------------------------------------ |
# | create_array()    | O(r × c)        | O(r × c)         | Creates complete 2D array                              |
# | display_array()   | O(r × c)        | O(1)             | Prints every element                                   |
# | insert_value()    | O(1)            | O(1)             | Direct value insertion using indexing                  |
# | insert_row()      | O(r × c)        | O(r × c)         | NumPy creates a new array during insertion             |
# | insert_column()   | O(r × c)        | O(r × c)         | Entire array copied into new memory                    |
# | access_element()  | O(1)            | O(1)             | Direct indexing                                        |
# | update_element()  | O(1)            | O(1)             | Directly updates element using indexing                |
# | traverse_array()  | O(r × c)        | O(1)             | Visits every element once                              |
# | search_element()  | O(r × c)        | O(1)             | Linear search through all elements                     |
# | delete_row()      | O(r × c)        | O(r × c)         | np.delete() creates a new array                        |
# | delete_column()   | O(r × c)        | O(r × c)         | New array allocation after deletion                    |
# | menu()            | O(1) per op     | O(1)             | Menu handling only                                     |