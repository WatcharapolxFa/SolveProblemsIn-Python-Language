class SinglyLinkedListNoDummy:  # ทำงานเหมือน List (อ้าง index แบบเดียวกัน)
    class Node:  # เก็บข้อมูล
        def __init__(self, data, next=None):
            self.data = data  # ส่งค่าไรมาเก็บไว้ที่นี้
            if next is None:
                self.next = None   # next  เก็บค่าตัวโยง
            else:
                self.next = next

    def __init__(self):  # มาแบบว่างไม่ได้รับค่าเข้ามา
        self.head = None  # ส่วนหัว
        self.size = 0

    def __str__(self):                # แสดงข้อมูลทุกตัวใน linked list
        strs = 'linked data : '
        p = self.head
        while p != None:  # loop จนกว่า P จะไม่มีค่าอยู่ในนั้น
            strs += str(p.data) + ' '  # เอาค่า P มาบวกต่อเป็นสายอักขระ
            p = p.next  # ให้ p ไปตัวถัดไป
        return strs    # return เป็น str

    def __len__(self):               # เพิ่ม เมื่อ เติมข้อมูล  ลด เมื่อ นำข้อมูลออก
        return self.size             # ขนาดของข้อมูล

    def isEmpty(self):               # ตรวจสอบว่ามีข้อมูลใน linked list ไหม
        return self.size == 0

    def indexOf(self, data):          # หา อินเด็กของข้อมูลว่าอยู่ที่ตำแหน่งใด
        p = self.head
        for count in range(len(self)):
            if p.data == data:  # ที่ node เริ่มต้น เท่ากับ data ที่ต้องการไหม
                return count
            p = p.next          # ไม่เจอก็จะขยับไปเรื่อยๆจนครับจำนวนสมาชิกที่อยู่ใน linked list
        return -1  # ส่งค่าไปบรรทัดที่ 37

    def isIn(self, data):             # ตรวจสอบว่าใน linked list นี้ มีข้อมูลตัวนี้ไหม
        # ถ้าบรรทัด 37 return -1 ตรงนี้จะ return false
        return self.indexOf(data) >= 0

    def nodeAt(self, i):              # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
        p = self.head
        for j in range(0, i):  # เข้าถึงข้อมูลใน linklist
            p = p.next
        return p

    def append(self, data):            # เพิ่ม ข้อมูล ไปที่ด้านท้ายของ linked list
        if self.head == None:  # กรณีที่เอาข้อมูลเข้าตัวแรก
            p = self.Node(data)
            self.head = p
            # self.head = self.Node(data, None) #สร้าง node ขึ้นมาใหม่
            self.size += 1
        else:                   # กรณีที่เอาข้อมูลเข้าไม่ใช่ตัวแรก
            # len(self) = จำนวนสมาชิก - 1 คือ index สุดท้าย
            self.insertAfter(len(self)-1, data)  # เรียก insertAfter

    def insertAfter(self, i, data):  # เพิ่ม ข้อมูล ในสายข้อมูลอยู่แล้ว
        q = self.nodeAt(i)
        p = self.Node(data)  # สร้าง node ขึ้นมาใหม่
        p.next = q.next
        q.next = p
        #q.next = self.Node(data,q.next)
        self.size += 1

    def deleteAfter(self, i):  # ลบ ข้อมูล ต้องมีข้อมูลอยู่แล้ว
        if self.size > 0:  # ตรวจว่ามีข้อมูลให้ลบไหม
            q = self.nodeAt(i)  # หาตำแหน่งที่ต้องมันคือ node อะไร
            q.next = q.next.next  # node ที่อยู่หลัง node q จะถูกลบไป
            self.size -= 1  # ลดขนาดตัวเก็บ

    def delete(self, i):  # ลบข้อมูลที่ อินเด็กซ์ที่กำหนด
        if i == 0 and self.size > 0:  # ลบตัวแรก
            self.head = self.head.next
            self.size -= 1
        else:
            self.deleteAfter(i-1)  # ลบตัวก่อนหน้า

    def removeData(self, data):  # ลบข้อมูลใน linked list
        if self.isIn(data):
            self.deleteAfter(self.indexOf(data)-1)

    def addHead(self, data):
        if self.isEmpty():
            p = self.Node(data)
            self.head = p
            self.size += 1
        else:
            p = self.Node(data, self.head)
            self.head = p
            self.size += 1


l1 = SinglyLinkedListNoDummy()
l1.addHead('a')
# l1.append('b')
# l1.append('c')
# l1.append('d')
# l1.append('e')
# l1.append('z')
# l1.append('aa')
# print(l1, len(l1))
# l1.delete(0)  # ลบข้อมูลที่ตำแหน่งแรก
print(l1)
# l1.delete(5)  # ลบข้อมูลที่ตำแหน่งindex 1
# print(l1, len(l1))
# l1.delete(len(l1)-1)  # ลบข้อมูลที่ตำแหน่งสุดท้าย
# print(l1)
# l1.delete(0)
# print(l1)
# l1.delete(0)
# print(l1)
