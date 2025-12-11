"""
Graph Representation using the List
"""

n = 5
m = 6

edges = [[1, 2], [2, 4], [3, 4], [1, 3], [3, 5], [5, 4]]

List = [[]for _ in range(n+1)]

for u, v in edges:
    List[u].append(v)
    List[v].append(u)

for i in List:
    print(i)

"""
[]
[2, 3]
[1, 4]
[4, 1, 5]
[2, 3, 5]
[3, 4]
"""


"""
Graph Representation using the Dictionary
"""
my_dict = {}
for i in range(n+1):
    my_dict[i] = []
    
for u, v in edges:
    my_dict[u].append(v)
    my_dict[v].append(u)

print(my_dict)