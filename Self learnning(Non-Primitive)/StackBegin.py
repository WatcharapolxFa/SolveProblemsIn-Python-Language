class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.size = len(self.items)

    def push(self, i):
        self.items.append(i)
        self.size += 1

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        S = 'stack of'+str(self.size())+'items:'
        for ele in self.items:
            S += str(ele)+''
        return S


# push(): ใส่ด้านบน
# pop(): เอาด้านบนออก
# peek():ดู บนสุดแต่ไม่เอาออก
# isEmpty():Stack สถานะว่างหรือไม่
# size():Stack มีสมาชิกเท่าไหร่
s1 = Stack([1, 2, 3])
print(s1)
print(s1.items)
# s.push('A')
# s.push('B')
# s.push('C')สามารถเพิ่มค่าได้เหมือนกัน
# print(s.size)
# print(s.items)
# print(s.pop())
# print(s.items)
# print(s.peek())
# print(s.items)
# print(s.isEmpty())
# print(s.size())
