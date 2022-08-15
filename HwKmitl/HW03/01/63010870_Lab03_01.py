class Stack:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)
        print("Add = "+str(i)+" and Size = " + str(len(self.items)))

    def pop(self):
        if self.isEmpty():
            print("-1")
            return
        else:
            i = self.items.pop()
            print("Pop = "+str(i)+" and Index = " + str(len(self.items)))

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        if self.isEmpty():
            return "Value in Stack = Empty"
        s = "Value in Stack = "
        for i in self.items:
            s += str(i)+" "

        return s


lists = input("Enter Input : ").split(",")
s1 = Stack()
for i in lists:
    opt = i[0]
    if opt == "A":
        value = i.split(" ")
        s1.push(value[1])
    if opt == "P":
        s1.pop()
print(s1)
