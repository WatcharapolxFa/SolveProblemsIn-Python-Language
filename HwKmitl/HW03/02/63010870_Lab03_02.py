class Stack():
    def __init__(self, list=None):
        if list == None:
            self.word = []
        else:
            self.word = list

    def push(self, i):
        self.word.append(i)

    def pop(self):
        return self.word.pop()

    def isEmpty(self):
        return self.word == []

    def size(self):
        return len(self.word)


def ParenMatching(str):
    oopStack = Stack()
    counts = 0
    error = 0
    strcheck = str
    while counts < len(str) and error == 0:
        strcheck = str[counts]
        if strcheck in '{[(':
            oopStack.push(strcheck)
        else:
            if strcheck in '}])':
                if oopStack.size() > 0:
                    if not match(oopStack.pop(), strcheck):
                        error = 1
                else:
                    error = 2

        counts += 1

    if strcheck[-1] not in '}])':
        error = 3

    return error, strcheck, counts, oopStack


def match(op, cl):
    opens = "([{"
    closes = ")]}"
    return opens.index(op) == closes.index(cl)


str = input('Enter expresion : ')
checkeror, strcheck, counts, oopStack = ParenMatching(str)
if checkeror == 1:
    print(str, 'Unmatch open-close  ')
elif checkeror == 2:
    print(str, 'close paren excess')
elif checkeror == 3:
    print(str, 'open paren excess  ', oopStack.size(), ': ', end='')
    for ele in oopStack.word:
        print(ele, sep=' ', end='')
    print()
else:
    print(str, 'MATCH')
