#สร้าง class สำหรับใช้เป็น node ของ tree
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        
    def __str__(self):
        return str(self.value)
    
# AVL Tree คือ binary search tree ที่มีเงื่อนไขของความสมดุล (Balance Condition) 
# โดยเงื่อนไขดังกล่าวคือ
# ในทุกๆ node ความสูงของ subtree ทางด้ายซ้ายและด้านขวาต่างกันไม่เกิน 1  
class AVLTree(object):
    
    # สร้าง root ของ tree
    def __init__(self):
        self.root = None
    
    # method for insert new node
    def insertNode(self, node, value):
        if node == None: # ถ้ายังไม่มี root node ให้ตัวแปรที่ส่งเข้ามาเป็น root node เลย
            return Node(value)
        elif value < node.value: # ถ้าค่าที่ส่งเข้ามาน้อยกว่า node ปัจจุบัน ให้ไปเทียบกับทางซ้ายของ node ปัจจุบัน
            node.left = self.insertNode(node.left, value)
        elif value > node.value: # ถ้าค่าที่ส่งเข้ามาน้อยกว่า node ปัจจุบัน ให้ไปเทียบกับทางขวาของ node ปัจจุบัน
            node.right = self.insertNode(node.right, value)
        else: # ถ้าค่าที่ส่งเข้ามามีค่าเท่ากับ node ปัจจุบัน จะไม่มีการเพิ่ม node ใหม่เข้ามา
            return node
        
        # กำหนดความสูงของ node ที่มีถูกเพิ่ม child node จากค่าที่ส่งเข้ามา
        node.height = 1 + max(self.getNodeHeight(node.left), self.getNodeHeight(node.right))
        # จัดสมดุลหลังจากเพิ่ม node ใหม่เสร็จ
        return self.balanceInsert(node, value)
        
    # ลบ node จากค่าที่ส่งเข้ามา
    def deleteNode(self, node, value):
        if not node: # ถ้าไม่มี node ใดๆเลยใน tree ก็ไม่มต้องลบ และแจ้งเตือนผู้ใช้ไปทาง terminal
            print("No node value found!")
            return node
        if value < node.value: # ถ้าค่าที่ส่งเข้ามาน้อยกว่าค่าของ node ปัจจุบัน ให้ไปเช็คกับ node ทางซ้ายของ node ปัจจุบัน โดยการเรียกฟังก์นี้เดิมนี้ซ้ำ
            node.left = self.deleteNode(node.left, value)
            return node
        elif value > node.value: # ถ้าค่าที่ส่งเข้ามาน้อยกว่าค่าของ node ปัจจุบัน ให้ไปเช็คกับ node ทางขวาของ node ปัจจุบัน โดยการเรียกฟังก์นี้เดิมนี้ซ้ำ
            node.right = self.deleteNode(node.right, value)
            return node
        else: # ถ้าค่าที่ส่งเข้ามาตรงกับค่าของ node ปัจจุบัน
            if node.left is None or node.right is None: # เช็คว่าซ้าย-ขวา ว่ามี node มั้ย
                temp = None # ประกาศตัวแปรที่เอาไว้เก็บ node เพียงชั่วคราว
                if node.left is None: # ถ้าด้านซ้ายไม่มี node ให้ค่าของ temp คือ node ขวา
                    temp = node.right
                else: # ถ้าไม่ใช่ ให้ค่าของ temp คือ node ซ้าย
                    temp = node.left
                if temp is None: # ถ้า temp ยังไม่มีค่าอะไร (เช็คซ้ำ)
                    temp = node # ให้ temp มีค่าเท่ากับ node ปัจจุบัน
                    node = None
                else: # ถ้าไม่ใช่ ให้ node ปัจจับุันเท่ากับ temp กล่าวคืขยับซ้ายหรือขวามา 1 step
                    node = temp
            else: # ถ้าซ้าย-ขวา มี node ทั้ง 2 ฝั่ง ให้สร้าง node ฝั่งขวาใหม่ จาก node ฝั่งขวาที่มีอยู่แล้ว จากนั้นลบตัวเองซ้ำไปทางขวา (เพื่อเช็ค)
                temp = self.createNodeWithMinimumValue(node.right)
                node.value = temp.value
                node.right = self.deleteNode(node.right, temp.value)
        if not node: # ถ้า node ไม่มีอะไรแล้วก็ return ตัวนั้นกลับไป (return None)
            return node
        
        # กำหนดความสูงของ node ปัจจุบันหลังจากลบเสร็จแล้ว
        node.height = 1 + max(self.getNodeHeight(node.left), self.getNodeHeight(node.right))
        # return ค่าที่ได้จากการปรับสมดุลของ tree แล้ว
        return self.balanceInsert(node, value)
    
    # จัดสมดุลหลังจากที่เพิ่ม node ใหม่เข้ามา
    def balanceInsert(self, node, value):
        balance = self.getNodeBalance(node) # เช็คว่า node หนักไปทางไหน
        if balance > 1: # node หนักซ้าย
            if value < node.left.value:
                print("AVL Tree Not Balance, Rebalanced!")
                return self.rotateRight(node) # ขยับค่า node ไป tree ให้สมดุล
            elif value > node.right.value:
                print("AVL Tree Not Balance, Rebalanced!")
                node.left = self.rotateLeft(node.left)
                return self.rotateRight(node)
        if balance < -1: # node หนักขวา
            if value > node.right.value:
                print("AVL Tree Not Balance, Rebalanced!")
                return self.rotateLeft(node) # ขยับค่า node ไป tree ให้สมดุล
            elif value < node.right.value:
                print("AVL Tree Not Balance, Rebalanced!")
                node.right = self.rotateRight(node.right)
                return self.rotateLeft(node)
        return node # คืนค่า node ที่ปรับสมดุลแล้ว
    
    # จักสมดุลหลังจากที่ลบ node ออกไป
    def balanceDelete(self, node, balance):
        if balance > 1: # node หนักซ้าย
            temp_root = node.left
            temp = temp_root
            node.left = None
            while temp.right is not None:
                temp = temp.right
                temp.height += 1
            node.height = 1
            temp_root.right = node
            return temp_root
        elif balance < -1: # node หนักขวา
            temp_root = node.right
            temp = temp_root
            node.right = None
            while temp.left is not None:
                temp = temp.left
                temp.height += 1
            node.height = 1
            temp_root.left = node
            return temp_root
        return node
            
    # สร้าง node ใหม่จากค่าที่น้อยที่สุดของฝั่งนั้น ๆ
    def createNodeWithMinimumValue(self, node):
        current = node
        while current.left is not None:
            current = current.left;
        return current
        
    # ดึงค่าความสูงของ node นั้น ๆ
    def getNodeHeight(self, node):
        if node == None:
            return 0
        return node.height
    
    # เช็คว่า node หนักซ้ายหรือหนักขวา
    def getNodeBalance(self, node):
        if node == None:
            return 0
        return self.getNodeHeight(node.left) - self.getNodeHeight(node.right)
    
    # ขยับ node ไปทางซ้าย
    def rotateLeft(self, node):
        right = node.right
        node2 = right.left
        right.left = node
        node.right = node2
        node.height = 1 + max(self.getNodeHeight(node.left), self.getNodeHeight(node.right))
        right.height = 1 + max(self.getNodeHeight(right.left), self.getNodeHeight(right.right))
        return right

    # ขยับ node ไปทางขวา
    def rotateRight(self, node):
        left = node.left
        node2 = left.right
        left.right = node
        node.right = node2
        node.height = 1 + max(self.getNodeHeight(node.left), self.getNodeHeight(node.right))
        left.height = 1 + max(self.getNodeHeight(left.left), self.getNodeHeight(left.right))
        return left

    # เรียงค่าของตัวเลขใน node จากนั้น print ออกมา
    def sortNumInNode(self, node):
        if node.left is not None or node.right is not None:
            if node.left is not None:
                self.sortNumInNode(node.left)
            print(node.value, end=" ")
            if node.right is not None:
                self.sortNumInNode(node.right)
        else:
            print(node.value, end=" ")
            
    # แสดงผล tree
    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
if __name__ == "__main__":
    treeNode = AVLTree()
    
    inp = map(int, input("Enter number : ").split())
    for num in inp:
        print(f"inserted -> {num}")
        treeNode.root = treeNode.insertNode(treeNode.root, num)
        treeNode.printTree(treeNode.root)
        print("--------------------")
        
    treeNode.sortNumInNode(treeNode.root)
    print("\n--------------------")
    
    inp = map(int, input("Enter number that you want delete : ").split())
    for num in inp:
        print(f"Delete -> {num}")
        treeNode.root = treeNode.deleteNode(treeNode.root, num)
        treeNode.printTree(treeNode.root)
        print("--------------------")
        balance = treeNode.getNodeBalance(treeNode.root)
        if balance > 1 or balance < -1:
            treeNode.root = treeNode.balanceDelete(treeNode.root, balance)
            treeNode.printTree(treeNode.root)
            print("--------------------")
