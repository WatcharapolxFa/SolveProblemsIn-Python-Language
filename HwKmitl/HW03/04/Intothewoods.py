class Stack:
    def __init__(self, ls=None):
        self.stack = []
        if ls != None:
            self.stack = ls
        self.stack.reverse()  # reverse == เอาค่าตัวหน้าแทนที่จะเอาตัวหลัง

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        s = self.stack.pop()
        # s[0] == เอาค่าตำแหน่งที่ 0 : s[2:] == เอาค่าตำแหน่งที่สองจนถึงตัวสุดท้าย
        return s[0], s[2:]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0


inp = input("Enter Input : ").split(',')
S = Stack(inp)
tmp = []
for i in range(S.size()):
    case, height = S.pop()
    if case == "A":
        if len(tmp) == 0:
            tmp.append(int(height))  # เจอ A ครั้งแรกจะเข้านี้เสมอ
        else:
            # filter คือเข้าถึงทุกตัวเหมือน for แต่ในตัวมันเอง
            # ตัวแปรเก็บค่า = filter(lambda(ใช้เปรียบเทียบ) พารามิเตอร์ : เงื่อนไข ,ตามด้วยตัวที่จะดึงตาสมาใช้)
            tmp1 = filter(lambda num: num > int(height), tmp)
            tmp = list(tmp1)  # แปรงเป็น list
            tmp.insert(0, int(height))  # เอาข้อมูลเข้า เช่น 1234 -> 6 == 61234
    elif case == "B":
        print(len(tmp))
