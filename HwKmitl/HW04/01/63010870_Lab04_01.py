class Queue:
    def __init__(self, lst=None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def enqueue(self, val):
        self.items.append(val)
        print(self)

    def dequeue(self):
        if self.isEmpty():
            print("Empty")
            return
        else:
            i = self.items.pop(0)
            return i

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        if self.isEmpty():
            return ("Empty")
        strprint = ", ".join(self.items)
        return strprint


inp = input("Enter Input : ").split(",")
que = Queue()
dq = []
for i in inp:
    opt = i[0]
    if opt == "E":
        value = i.split()
        que.enqueue(value[1])
    if opt == "D":
        value = que.dequeue()
        if value == "Empty":
            print(value)
        elif value != "Empty" and value != None:
            dq.append(str(value))
            print(str(value) + " <- ", end="")
            print(que)

newstr = ", ".join(dq)
if len(dq) != 0:
    print(newstr + " : ", end="")
else:
    print("Empty : ", end="")
print(que)
