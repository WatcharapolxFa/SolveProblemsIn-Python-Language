from re import search

#แต่ละ node ของ tree
class TreeNode(object): 
    
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)

# AVL Tree คือ binary search tree ที่มีเงื่อนไขของความสมดุล (Balance Condition) โดยเงื่อนไขดังกล่าวคือ
# Condition: ในทุกๆ โหนด ความสูงของ subtree ทางด้ายซ้ายและด้านขวาต่างกันไม่เกิน 1  
class AVL_Tree(object): 


    # Adding node
    def insert(self, root, key):
        if not root:  # ถ้าค่า root ที่ส่งมาเป็น None ให้สร้าง node ใหม่ที่ใส่ค่า key เข้าไปเลย
            return TreeNode(key)
        elif int(key) < int(root.val): # ถ้าค่า key ที่ส่งมาน้อยกว่าค่า node ปัจจุบันให้ insert ไปทางซ้ายของ node
            root.left = self.insert(root.left, key)
        else: # ถ้าค่า key ที่ส่งมามากกว่าเท่ากับค่า node ปัจจุบันให้ insert ไปทางขวาของ node
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right)) #บวกค่า height ให้กับ node ปัจจุบันหลังจากเพิ่ม node แล้ว
        balance = self.getBalance(root) #เช็คว่า tree ตอนนี้ balance ไหม
        if balance > 1 and int(key) < int(root.left.val): #เช็คว่า nodeทางซ้าย สูงกว่า nodeทางขวามากกว่า1 และ ค่า key น้อยกว่าค่า root.left ให้ทำการหมุน node
            print("Not Balance, Rebalance!")
            return self.rightRotate(root)
 
        if balance < -1 and int(key) > int(root.right.val): #เช็คว่า nodeทางขวา สูงกว่า nodeทางซ้ายมากกว่า1 และ ค่า key มากกว่ากว่าค่า root.right ให้ทำการหมุน node
            print("Not Balance, Rebalance!")
            return self.leftRotate(root)
 
        if balance > 1 and int(key) > int(root.left.val): #เช็คว่า nodeทางซ้าย สูงกว่า nodeทางขวามากกว่า1 และ ค่า มากกว่าค่า root.left ให้ทำการหมุน node
            print("Not Balance, Rebalance!")
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and int(key) < int(root.right.val): #เช็คว่า nodeทางขวา สูงกว่า nodeทางซ้ายมากกว่า1 และ ค่า key น้อยกว่าค่า root.right ให้ทำการหมุน node
            print("Not Balance, Rebalance!")
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
    
    # Remove node
    def delete(self,root, data):
 
        #กรณี node เป็น None
        if root is None:
            print("Error! Not Found DATA")
            return root

        root.height-=1 #ลบค่าความสูง node ปัจจุบันลง 1

        if data < root.val: #ค่าที่จะลบน้อยกว่าเลื่อนลงไปทาง node ซ้าย
            root.left = self.delete(root.left, data)
            return root
        elif(data > root.val): #ค่าที่จะลบมากกว่าเลื่อนลงไปทาง node ขวา
            root.right = self.delete(root.right, data)
            return root


        # ถึง node เป้าหมายที่ต้องการลบ กรณีที่ nodeเป้าหมายไม่มี node ซ้ายและขวาต่ออยู่ return ค่ากลับมาเป็น none (การลบ node เป้าหมาย) 
        if root.left is None and root.right is None:
            return None

      
        if root.left is None: # ถึง node เป้าหมายที่ต้องการลบ กรณีที่ nodeเป้าหมายไม่มี nodeซ้ายต่ออยู่ return ค่า nodeขวากลับมา (การลบ node เป้าหมาย) 
            temp = root.right
            root = None
            return temp
        elif root.right is None: # ถึง node เป้าหมายที่ต้องการลบ กรณีที่ nodeเป้าหมายไม่มี nodeขวาต่ออยู่ return ค่า nodeซ้ายกลับมา (การลบ node เป้าหมาย) 
            temp = root.left
            root = None
            return temp

        succParent = root # ค่า root นี้จะเท่ากับค่าที่ return จาก recursive มา 
        # ด้านล่างจะเป็นการนำ node ที่ต่อจาก node ที่ถูกตัดมาเรียงแบบ Successor
        succ = root.right
    
        while succ.left != None:
            succParent = succ
            succ = succ.left
    
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
    
        root.val = succ.val
    
        return root

    #Balance node ทำการปรับ balance tree
    def balanceNode(self,root):
        if self.getBalance(root)>1: #ทำการปรับ balance เมื่อทางซ้ายหนักกว่าทางขวา
            newRoot = root.left
            temp = newRoot
            root.left = None
            while temp.right != None:
                temp = temp.right
                temp.height+=1
            root.height=1
            temp.right=root
            return newRoot
        if self.getBalance(root)<-1: #ทำการปรับ balance เมื่อทางขวาหนักกว่าทางซ้าย
            newRoot = root.right
            temp = newRoot
            root.right = None
            while temp.left != None:
                temp = temp.left
                temp.height+=1
            root.height=1
            temp.left=root
            return newRoot
        return root
    
    # Sorted number
    # เป็น function ที่ทำการ print ค่าแบบ inorder ทำให้ค่ามีการ sort จากน้อยไปมาก
    def sortNum(self,node):
        if node.left != None or node.right != None: 
            if node.left != None : self.sortNum(node.left)
            print(node.val,end=" ")
            if node.right != None : self.sortNum(node.right)
        else: print(node.val,end=" ")

    # หมุน node ทวนเข็มนาฬิกาใช้ตอน node ไม่ balance ตอน insert node
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
 
        return y
    
    # หมุน node ตามเข็มนาฬิกาใช้ตอน node ไม่ balance ตอน insert node
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        y.right = z
        z.left = T3
 
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
 
        return y

    # เป็น function ที่ return ค่าความสูงของ node ที่ส่งเข้าไป
    def getHeight(self, root): 
        if not root:
            return 0
 
        return root.height
    
    # เป็น function ที่เช็คว่า tree  balance ไหมโดยยืดจาก node ที่ส่งเข้าไปเป็น root
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

# เป็น function ที่ทำการ print tree ออกมาในแนวนอน nodeซ้ายจะอยู่ด้านล่าง nodeขวาจะอยู่ด้านบน
def printTree(node, level = 0):                     #Ex  
    if node != None:                                #              จากตัวอย่าง 5 เป็น root node
        printTree(node.right, level + 1)            #   7
        print('     ' * level, node)                # 5
        printTree(node.left, level + 1)             #   4
                                                    #     
myTree = AVL_Tree() 
root = None

# รับ input เพื่อสร้าง node ตัวอย่าง input : 30 50 70 90 55 95 10 80 35

data = input("Enter Input insert: ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree(root)
    print("===============")


# ทำการแสดงค่าเรียงจากน้อยไปมาก
myTree.sortNum(root)
print("\n===============")


# รับ input เพื่อลบ node ตัวอย่าง input : 10 50
dataDel = input("Enter Input Delete: ").split()
for e in dataDel:
    print("Delete :",e)
    root = myTree.delete(root, e)
    printTree(root)
    print("===============")
    if myTree.getBalance(root)>1 or myTree.getBalance(root)<-1:
        print("Not Balance, Rebalance!")
        root = myTree.balanceNode(root)
        printTree(root)
        print("===============")