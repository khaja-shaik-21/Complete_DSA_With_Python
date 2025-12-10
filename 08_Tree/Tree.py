class TreeNode:
    def __init__(self, data, child = []):
        self.data = data
        self.child = child
    
    def __str__(self, level=0):
        ret = ' ' * level + str(self.data) + '\n'
        for child in self.child:
            ret += child.__str__(level + 1)
        return ret
    
    def append(self, TreeNode):
        self.child.append(TreeNode)
        
Tree = TreeNode('Drinks', [])
Cold = TreeNode('Cold', [])
Hot = TreeNode('Hot', [])
Tree.append(Cold)
Tree.append(Hot)

tea = TreeNode('tea', [])
coffee = TreeNode('coffee', [])
cola = TreeNode('cola', [])
fanta = TreeNode('fanta', [])
Cold.append(fanta)
Cold.append(cola)
Hot.append(tea)
Hot.append(coffee)
print(Tree)