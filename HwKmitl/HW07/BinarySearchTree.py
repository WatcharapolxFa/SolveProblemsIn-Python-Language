class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        nNode = Node(data)
        if self.root == None:
            self.root = nNode
        else:
            Check = self.root
            while True:
                if data < Check.data:
                    '''data less the root pai left'''
                    if Check.left == None:
                        Check.left = nNode
                        break
                    Check = Check.left
                else:
                    if Check.right == None:
                        Check.right = nNode
                        break
                    Check = Check.right
        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


Tree = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for j in inp:
    root = Tree.insert(j)
Tree.printTree(root)
