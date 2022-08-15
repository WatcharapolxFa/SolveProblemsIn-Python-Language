class Queue:
    def __init__(self, ls=None):
        if ls == None:
            self.list = []
        else:
            self.list = ls
        self.size = len(self.list)

    def enQueue(self, val):
        self.size += 1
        return self.list.append(val)

    def deQueue(self):
        self.size -= 1
        return self.list.pop(0)

    def isEmpty(self):
        return self.list == 0


def encodemsg(msg, code):
    count = 0
    for i in range(msg.size):
        asci = ord(msg.deQueue())
        buak = asci + code.list[count]
        if 65 <= asci <= 90:
            if buak > 90:
                buak = 64 + (buak - 90)
        elif 97 <= asci <= 122:
            if buak > 122:
                buak = 96 + (buak - 122)
        msg.enQueue(chr(buak))
        count += 1
        if count >= code.size:
            count = 0
    print("Encode message is : ", msg.list)


def decodemsg(msg, code):
    count = 0
    for i in range(msg.size):
        asci = ord(msg.deQueue())
        buak = asci - code.list[count]
        if 65 <= asci <= 90:
            if buak < 65:
                buak = 90 - (64 - buak)
        elif 97 <= asci <= 122:
            if buak < 97:
                buak = 122 - (96 - buak)
        msg.enQueue(chr(buak))
        count += 1
        if count >= code.size:
            count = 0
    print("Decode message is : ", msg.list)


inp = input("Enter String and Code : ").split(',')
string = [i for i in inp[0] if i != " "]
number = [int(i) for i in inp[1]]

q1 = Queue(string)
q2 = Queue(number)
encodemsg(q1, q2)
decodemsg(q1, q2)
