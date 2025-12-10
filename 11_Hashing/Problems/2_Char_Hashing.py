"""
Hashing Concept Understanding Uisng the problem
"""
###### Method 1: Any value ######
s = "hsdgfuwewbefuybdcADJHFWEFB@#^*()#%&((9432742938430))"

t = ['a', '%', 'e', 'v', 'z', '!', '9', ')']

hash_table = [0] * 127               # why 26, because alphets are 26

for ch in s:
    ascii = ord(ch)
    hash_table[ascii] += 1

for ch in t:
    ascii = ord(ch)
    print(hash_table[ascii], end=" ")
print()


###### Method 2: lowercase alphabets ######
s = "iugfbfonfhbdisqvamuyrbfvgwaerbmiuerg"
t = ['s', 'q', 'v', 'a', 'm']
hash_table = [0] * 26

for ch in s:
    if 'a' <= ch <= 'z':
        hash_table[ord(ch) - ord('a')] += 1

for ch in t:
    if 'a' <= ch <= 'z':
        print(hash_table[ord(ch) - ord('a')], end=" ")
    else:
        print(0, end=" ")
