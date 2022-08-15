class Stack:
    def __init__(self, item=None):
        if item == None:
            self.item = []
        else:
            self.item = item

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def size(self):
        return len(self.item)

    def peek(self):
        return self.item[-1]

    def isEmpty(self):
        return self.item == []

    def getItem(self):
        return self.item[0::]


### Main ###
inputText = input("Enter Infix : ")
stack = Stack()

print("Postfix : ", end='')
for item in inputText:
    # print(stack.item)
    if item in ['+', '-', '*', '/', '^', '(', ')']:
        if item in ['+', '-', '*', '/', '^']:
            while not stack.isEmpty() and item in ['+', '-'] and stack.peek() in ['*', '/', '+', '-', '^']:
                print(stack.pop(), end='')
            while not stack.isEmpty() and item in ['*', '/'] and stack.peek() in ['*', '/', '^']:
                print(stack.pop(), end='')
            while not stack.isEmpty() and item in ['^'] and stack.peek() in ['^']:
                print(stack.pop(), end='')
            stack.push(item)
        else:
            if item == '(':
                stack.push(item)
            if item == ')':
                while stack.peek() != '(':
                    print(stack.pop(), end='')
                stack.pop()
    else:
        print(item, end='')

while not stack.isEmpty():
    print(stack.pop(), end='')
