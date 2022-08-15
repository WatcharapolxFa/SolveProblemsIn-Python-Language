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
backup = []
status = False
for i in range(S.size()):
    case, height = S.pop()
    if case == "S":
        status = True
    if status and height != "":
        if int(height) > 1:
            if int(height) % 2 == 0:
                height = int(height) - 1
            elif int(height) % 2 != 0:
                height = int(height) + 2
        status = False
    if status:
        for i in range(len(tmp)):
            if tmp[i][1] == False:
                if tmp[i][0] % 2 == 0:
                    tmp[i][0] -= 1
                else:
                    tmp[i][0] += 2
                tmp[i][1] = True
        status = False
    if case == "A":
        ls = [int(height), status]
        if len(tmp) == 0:
            tmp.append(ls)
        else:
            tmp.insert(0, ls)
    elif case == "B":
        if len(tmp) == 0:
            print(0)
        else:
            count = [1, tmp[0][0]]
            for i in range(1, len(tmp)):
                if tmp[i][0] > count[1]:
                    count[0] += 1
                    count[1] = tmp[i][0]
            print(count[0])
