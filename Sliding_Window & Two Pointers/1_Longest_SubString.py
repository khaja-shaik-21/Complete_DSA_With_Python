"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

###### Method 1: Bruite Force ######
s = 'abcbdbc'
n = len(s)
maxi = 0

for i in range(0, n):
    my_set = set()
    for j in range(i, n):
        if s[j] in my_set:
            break
        maxi = max(maxi, j-i+1)
        my_set.add(s[j])
print(maxi)

# Time Complexity : O(N(N+1)/2) ~ O(N^2)
# Space Complexity : O(N)


###### Method 2: Sliding Window and Two Pointers ######

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxi = 0
        my_dict = {}   # stores last index of each character
        left = 0

        for right in range(n):
            if s[right] in my_dict:
                # move left pointer to the right of last occurrence
                left = max(left, my_dict[s[right]] + 1)

            # update the longest window
            maxi = max(maxi, right - left + 1)

            # update last position of char
            my_dict[s[right]] = right

        return maxi

s = 'abcbdbc'
result = Solution()

print(result.lengthOfLongestSubstring(s))


# Time Complexity: O(n)
# Space Complexity: O(min(n, m)) ~ O(1) for ASCII