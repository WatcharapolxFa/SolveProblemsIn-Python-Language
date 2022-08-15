class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.value)


class AVL:
    def __init__(self):
        self.root = None

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def insert(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getHeight(root.right),
                              self.getHeight(root.left))
        balance = self.getBalance(root)

        if balance > 1 and data < root.left.data:
            return self.rightRotate(root)
        if balance < -1 and data >= root.right.data:
            return self.leftRotate(root)
        if balance > 1 and data >= root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def rightRotate(self, z):
        y = z.left
        temp = y.right
        y.right = z
        z.left = temp
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def leftRotate(self, z):
        y = z.right
        temp = y.left
        y.left = z
        z.right = temp
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def inorder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")


print(" *** AVL Tree ***")
data = list(map(int, input("Enter some numbers : ").split()))
bst = AVL()
root = None
for i in data:
    root = bst.insert(root, i)
print("in_order  --> ", end='')
bst.inorder(root)
print()
print("preorder  --> ", end='')
bst.preorder(root)
print()
print("postorder --> ", end='')
bst.postorder(root)
print()
