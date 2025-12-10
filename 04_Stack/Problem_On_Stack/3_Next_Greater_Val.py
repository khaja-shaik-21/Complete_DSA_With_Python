"""
You are given an array arr[] of integers, 
the task is to find the next greater element for each element of the array in order of their appearance in the array. 
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.

If there does not exist next greater of current element, 
then next greater element for current element is -1.

"""

class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n
        st = []

        for i in range(n - 1, -1, -1):
            while st and st[-1] <= arr[i]:
                st.pop()

            if st:
                res[i] = st[-1]

            st.append(arr[i])

        return res
