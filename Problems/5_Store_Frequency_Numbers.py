"""
Store Number Frequency in dictionary
"""

n = [1, 2, 3, 4, 5, 1, 2, 3, 1]

###### Method 1: ######
freq = {}

for i in n:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

# Time complexity: O(n) where n is the length of the input list
# Space complexity: O(k) where k is the number of unique elements in the input list


###### Method 2: ######
from collections import Counter

freq = Counter(n)
print(freq)

# Time complexity: O(n) 
# Space complexity: O(k) 

###### Method 3: Hash Table ######

hash_table = {}
for i in n:
    hash_table[i] = hash_table.get(i, 0) + 1
print(hash_table)

# Time complexity: O(n) 
# Space complexity: O(k) 