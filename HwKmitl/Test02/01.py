class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def bottom(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def __str__(self):
        if not self.is_empty():
            out = "Data in Stack is : "
            for item in self.items:
                out += str(item)+' '
            return out
        return 'Empty'


if __name__ == '__main__':
    newStack = Stack()
    CheckState = int(input("Enter choice : "))
    if CheckState == 1:
        newStack = Stack()
        newStack.push(10)
        newStack.push(20)
        print(newStack)
        newStack.pop()
        newStack.push(30)
        print("Peek of stack :", newStack.peek())
        print("Bottom of stack :", newStack.bottom())
    elif CheckState == 2:
        newStack = Stack()
        newStack.push(100)
        newStack.push(200)
        newStack.push(300)
        newStack.pop()
        print(newStack)
        print("Stack is Empty :", newStack.is_empty())
    elif CheckState == 3:
        newStack = Stack()
        newStack.push(11)
        newStack.push(22)
        newStack.push(33)
        newStack.pop()
        print(newStack)
        print("Stack size :", newStack.size())
