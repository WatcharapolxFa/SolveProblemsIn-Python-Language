class Queue:
    def __init__(self, lst=None):
        self.countinput = 0
        self.countbom = 0
        if lst == None:
            self.items = []
        else:
            self.items = lst
        self.getTripleCharactor()

    # def enqueue(self, val):
    #     self.items.append(val)

    # def dequeue(self):
    #     return self.items.pop(0)

    def __str__(self):
        self.items.reverse()
        if self.isEmpty():
            return ("Empty")
        strprint = ""
        for i in range(self.size()):
            strprint += self.items[i][0]
        return strprint

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def getTripleCharactor(self):
        countcheckqueue = 0
        checkdefend = False
        while(True):
            if countcheckqueue < len(self.items) - 2:  # AAABBBCDEE
                if self.items[countcheckqueue][0] == self.items[countcheckqueue+1][0] == self.items[countcheckqueue+2][0]:
                    if self.items[countcheckqueue][1] or self.items[countcheckqueue+1][1] or self.items[countcheckqueue+2][1]:
                        self.countbom += 1  # 2
                    self.items.pop(countcheckqueue+2)
                    self.items.pop(countcheckqueue+1)
                    self.items.pop(countcheckqueue)
                    self.countinput += 1
                    checkdefend = True
                    countcheckqueue = -1
            if countcheckqueue == len(self.items) and checkdefend:
                countcheckqueue = 0
                checkdefend = False
            elif self.size() < 3 or (countcheckqueue == len(self.items) and checkdefend == False):
                break
            countcheckqueue += 1


class Stack:
    def __init__(self, lst=None):
        self.stack = []
        self.items = []
        self.countnotbom = 0
        if lst != None:
            for i in range(len(lst)):
                # new lsit [] == list [] []
                lst2 = [lst[len(lst) - 1 - i], True]
                self.push(lst2)
        self.getTripleCharactor()
        self.items.reverse()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.items.pop()

    def __str__(self):
        self.stack.reverse()
        if self.is_empty():
            return ("ytpmE")
        stroutput = ""
        for i in range(self.size()):
            stroutput += self.stack[i][0]
        return stroutput

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def getTripleCharactor(self):
        countcheckstack = 0
        check = False
        while(True):
            if countcheckstack < self.size() - 2:
                if self.stack[countcheckstack][0] == self.stack[countcheckstack+1][0] == self.stack[countcheckstack+2][0]:
                    self.items.append(self.stack[countcheckstack])
                    self.stack.pop(countcheckstack+2)
                    self.stack.pop(countcheckstack+1)
                    self.stack.pop(countcheckstack)
                    self.countnotbom += 1
                    check = True
                    countcheckstack = -1
            if countcheckstack == len(self.stack) and check:
                countcheckstack = 0
                check = False
            elif (countcheckstack == len(self.stack) and check == False) or self.size() < 3:
                break
            countcheckstack += 1


inp = input("Enter Input (Normal, Mirror) : ").split()
stack01 = Stack(inp[1])  # HHH
ls_checks = []  # [A,False][A,False][A,False][B,False][B,False][B,False]
Ls_positions = []  # 0 #3
ls_bool = []  # [A,False][A,False][A,False][B,False][B,False][B,False]
insert_bom = [0, 0, 0]
for i in range(len(inp[0])):  # AAABBBCDEE
    if i < len(inp[0]) - 2:  # 0<8
        if inp[0][i] == inp[0][i+1] == inp[0][i+2]:
            Ls_positions.append(i)  # 0
    # [A,False][A,False][A,False][B,False][B,False][B,False]
    checkstate = [inp[0][i], False]
    ls_checks.append(checkstate)
ls_bool = ls_checks.copy()
for i in range(len(ls_checks)):
    if insert_bom[0] < len(Ls_positions) and stack01.countnotbom > insert_bom[2]:
        if Ls_positions[insert_bom[0]] == i:
            ls_bool.insert(i + 2 + insert_bom[0], stack01.pop())
            insert_bom[0] += 1
            insert_bom[2] += 1
queue01 = Queue(ls_bool)
print("NORMAL : \n{}".format(queue01.size()))
print(queue01)
print("{} Explosive(s) ! ! ! (NORMAL)".format(
    queue01.countinput - queue01.countbom))
if queue01.countbom > 0:
    print("Failed Interrupted {} Bomb(s)".format(queue01.countbom))
print("------------MIRROR------------\n: RORRIM\n{}".format(stack01.size()))
print(stack01)
print("(RORRIM) ! ! ! (s)evisolpxE {}".format(stack01.countnotbom))
