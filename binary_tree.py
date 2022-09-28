#binary tree

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BinaryTree:
    def __init__(self,value):
        self.root=Node(value)

root=Node(1)
n1=Node(2)
s2=Node(3)

tree=BinaryTree(root)  #create root of tree i.e. Node having value 1
tree.left=n1
tree.right=n2