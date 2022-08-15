class Stack:
    def __init__(self, ls=None):
        self.stack = []
        if ls != None:
            self.stack = ls
        self.stack.reverse()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        s = self.stack.pop()
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
            tmp.append(int(height))
        else:
            tmp1 = filter(lambda num: num > int(height), tmp)
            tmp = list(tmp1)
            tmp.insert(0, int(height))
    elif case == "B":
        print(len(tmp))
