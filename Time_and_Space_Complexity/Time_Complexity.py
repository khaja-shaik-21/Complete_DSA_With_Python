"""
Time Complexity Examples in Python
---------------------------------
This file contains examples of common time complexities
from O(1) to O(n!) with explanations and sample implementations.
"""

######### O(1) - Constant Time #########

# Doesn't depend on input size
# Only one operation regardless of input size

def get_first_element(arr):
    """
    Returns the first element of the array
    Time Complexity: O(1)
    """
    return arr[0]
arr = [1, 2, 3, 4, 5]
print(get_first_element(arr))  # Output: 1

######### O(n) – Linear Time #########

# Grows directly with input size

def find_sum(arr):
    """
    Returns the sum of all elements
    Time Complexity: O(n)
    """
    total = 0
    for num in arr:
        total += num
    return total
arr = [1, 2, 3, 4, 5]
print(find_sum(arr))  # Output: 15

######### O(log n) – Logarithmic Time #########

# Input is reduced by half each step

def binary_search(arr, target):
    """
    Binary search in a sorted array
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
arr = [1, 2, 3, 4, 5]
print(binary_search(arr, 3))  # Output: 2



######### O(n log n) – Linearithmic Time #########

# Used in efficient sorting algorithms like Merge Sort

def merge_sort(arr):
    """
    Merge Sort algorithm
    Time Complexity: O(n log n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
arr = [5, 2, 9, 1, 5, 6]
print(merge_sort(arr))  # Output: [1, 2, 5, 5, 6, 9]

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
arr = [5, 2, 9, 1, 5, 6]
print(merge_sort(arr))  # Output: [1, 2, 5, 5, 6, 9]



######### O(n^2) – Quadratic Time #########

# Two nested loops

def bubble_sort(arr):
    """
    Bubble Sort algorithm
    Time Complexity: O(n^2)
    """
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
arr = [5, 2, 9, 1, 5, 6]
print(bubble_sort(arr))  # Output: [1, 2, 5, 5, 6, 9]


######### O(n^3) – Cubic Time #########

# Three nested loops

def matrix_multiply(A, B):
    """
    Matrix multiplication (brute force)
    Time Complexity: O(n^3)
    """
    n = len(A)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result
arrA = [[1, 2], [3, 4]]
arrB = [[5, 6], [7, 8]]
print(matrix_multiply(arrA, arrB))  # Output: [[19, 22], [43, 50]]


######### O(2^n) – Exponential Time #########

# Doubles with each additional input

def fib(n):
    """
    Recursive Fibonacci
    Time Complexity: O(2^n)
    """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
n = 5
print(fib(n))  # Output: 5



######### O(n!) – Factorial Time #########

# Generates all permutations

def permute(nums):
    """
    Generate all permutations
    Time Complexity: O(n!)
    """
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result
nums = [1, 2, 3]
print(permute(nums))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]