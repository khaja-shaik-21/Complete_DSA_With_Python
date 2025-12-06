"""
Check if the Array is Sorted or not
"""

arr = [10, 20, 30, 40]

for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
        print("False'")
        break
print("True") 

# Time Complexity : O(N)
# Space Complexity : O(1)