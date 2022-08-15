class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[- 1]

    def size(self):
        return len(self.items)


print(" ***Infix to Postfix***")
inp = input("Enter Infix expression : ")
strcheck = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
Stc = Stack()
postfix = []
for count in inp:
    if count.isupper() or count.islower():
        postfix.append(count)
    else:
        if Stc.isEmpty():
            Stc.push(count)
        elif count == '(':
            Stc.push('(')
        elif count == ')':
            while Stc.isEmpty() == False and Stc.peek() != '(':
                postfix.append(Stc.pop())
            Stc.pop()
        else:
            while Stc.isEmpty() == False and Stc.peek() != '(' and strcheck[Stc.peek()] >= strcheck[count]:
                postfix.append(Stc.pop())
            Stc.push(count)
while not Stc.isEmpty():
    postfix.append(Stc.pop())
print("PostFix : ", ''.join(postfix))
