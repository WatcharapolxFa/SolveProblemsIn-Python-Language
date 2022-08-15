class Stack:
    def __init__(self, lst=None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


HighTree = Stack()


def B():
    count = 0
    Hightnow = 0
    Temp = Stack()
    while not HighTree.isEmpty():
        if int(HighTree.peek()) > Hightnow:
            Hightnow = int(HighTree.peek())
            count += 1
        Temp.push(HighTree.pop())
    while not Temp.isEmpty():
        HighTree.push(Temp.pop())
    return count


def S():
    Temp = Stack()
    while not HighTree.isEmpty():
        if int(HighTree.peek()) % 2 == 0:
            if int(HighTree.peek())-1 > 0:
                Temp.push(int(HighTree.pop())-1)
        else:
            Temp.push(int(HighTree.pop())+2)
    while not Temp.isEmpty():
        HighTree.push(Temp.pop())


lst = input("Enter Input : ").split(",")
for i in lst:
    command = i.split(" ")
    if command[0] == "A":
        HighTree.push(command[1])
    if command[0] == "B":
        print(B())
    if command[0] == "S":
        S()
