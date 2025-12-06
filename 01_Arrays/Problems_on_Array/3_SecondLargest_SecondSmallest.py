"""
Finding the Second Largest and Second Smallest from the List / Array
"""

a = [3, 4, 5, 2]

largest = float("-inf")
second_largest = float("-inf")

smallest = float("inf")  
second_smallest = float("inf")  
    
Len = len(a)

for i in range(Len):
    if a[i] > largest:
        second_largest = largest
        largest = a[i]
    elif a[i] > second_largest and a[i] != largest:
        second_largest = a[i]

    if a[i] < smallest:
        second_smallest = smallest
        smallest = a[i]
    elif a[i] < second_smallest and a[i] != smallest:  
        second_smallest = a[i]

print(second_largest, second_smallest)  # Output: 4 3


# Time Complexity : O(N)
# Space Complexity : O(1)