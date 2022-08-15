class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)


def parents(r, data):
    # code here
    if r.data == data:
        return "none because " + str(data) + " is root!!!"

    CheckCnode = r
    while CheckCnode.right != None or CheckCnode.left != None:
        if CheckCnode.right != None and CheckCnode.right.data == data:
            return CheckCnode.data
        elif CheckCnode.left != None and CheckCnode.left.data == data:
            return CheckCnode.data
        elif data > CheckCnode.data:
            CheckCnode = CheckCnode.right
        elif data < CheckCnode.data:
            CheckCnode = CheckCnode.left
    return "not found!!!"


tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for j in data[0].split():
    tree.create(j)
printTree(tree.root)
print('\nParents of', data[1], 'is', parents(tree.root, data[1]))
