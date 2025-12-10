"""
Hashing Concept Understanding Uisng the problem
"""

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

###### Problem 1: ######
ln = len(n) + 1
hash_list = [0] * ln

for num in n:
    hash_list[num] += 1

for num in m:
    if num >= len(hash_list):
        print(0, end=" ")
    else:
        print(hash_list[num], end=" ")

print()


###### Problem 2: ######   
dict_result = dict()

for i in n:
    dict_result[i] = dict_result.get(i, 0) + 1

print(dict_result)

for num in m:
    print(dict_result[num] if num in dict_result else 0)
    