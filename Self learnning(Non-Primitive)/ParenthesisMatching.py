class Stack:
    """ class Stack 
        default : empty stack / Stack([...])
    """

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = 'stack of ' + str(self.size())+' items : '
        for ele in self.items:
            s += str(ele)+' '
        return s

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def parenMatching(str):
    s = Stack()
    i = 0		 # index : str[i]
    error = 0

    while i < len(str) and error == 0:
        c = str[i]
        if c in '{[(':
            s.push(c)
        else:
            if c in '}])':
                if s.size() > 0:
                    if not match(s.pop(), c):
                        error = 1 	# open & close not match
                else: 	# empty stack
                    error = 2 	# no open paren
        i += 1

    if s.size() > 0:  	# stack not empty
        error = 3  # open paren(s) excesses
    return error, c, i, s


def match(op, cl):
    opens = "([{"
    closes = ")]}"
    return opens.index(op) == closes.index(cl)


str = '[(a+b-c}]'
err, c, i, s = parenMatching(str)
if err == 1:
    print(str, 'unmatch open-close  ')
elif err == 2:
    print(str, 'close paren excess')
elif err == 3:
    print(str, 'open paren(s) excess  ', s.size(), ': ', end='')
    for ele in s.items:
        print(ele, sep=' ', end='')
    print()
else:
    print(str, 'MATCH')
