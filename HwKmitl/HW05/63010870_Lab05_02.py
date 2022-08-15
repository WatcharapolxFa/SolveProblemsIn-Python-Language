class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizes = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        rotary, f = self.head, str(self.head.value) + " "
        while rotary.next != None:
            f += str(rotary.next.value) + " "
            rotary = rotary.next
        return f

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        rotary, f = self.tail, ""
        while rotary.previous != None:
            f += str(rotary.value) + " "
            rotary = rotary.previous
        f += str(rotary.value)
        return f

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        n = Node(item)
        if self.sizes == 0:
            self.head = self.tail = n
            self.sizes += 1
        else:
            n.next = self.tail.next
            n.previous = self.tail
            self.tail.next = n
            self.sizes += 1
            self.tail = n

    def addHead(self, item):
        newnode = Node(item)
        if self.isEmpty():
            self.head = self.tail = newnode
            self.sizes += 1
        else:
            newnode.next = self.head
            newnode.previous = self.head.previous
            self.head.previous = newnode
            self.head = newnode
            self.sizes += 1

    def insert(self, pos, item):
        newnode = Node(item)
        if pos >= 0:
            if pos != 0 and pos < self.sizes:
                rotary = self.head
                for i in range(pos-1):
                    rotary = rotary.next
                newnode.previous = rotary
                newnode.next = rotary.next
                self.sizes += 1
            elif pos == 0:
                self.addHead(item)
            elif pos > self.sizes-1:
                self.append(item)
        else:
            newnode = Node(item)
            if pos <= -1*(self.sizes):
                self.addHead(item)
            elif (self.sizes)*-1 < pos <= -1:
                rotary = self.tail
                for i in range(-1, pos, -1):
                    rotary = rotary.previous
                newnode.previous = rotary.previous
                newnode.next = rotary
                rotary.previous.next = newnode
                rotary.previous = newnode
                self.sizes += 1

    def search(self, item):
        rotary = self.head
        while rotary != None:
            if rotary.value == item:
                return 'Found'
            rotary = rotary.next
        else:
            return 'Not Found'

    def index(self, item):
        rotary = self.head
        i = 0
        while rotary != None:
            if rotary.value == item:
                return i
            i += 1
            rotary = rotary.next
        else:
            return -1

    def size(self):
        return self.sizes

    def pop(self, pos):
        rotary = self.head
        if pos < 0 or pos > self.sizes-1:
            return 'Out of Range'
        elif pos == 0:
            if self.head.next != None:
                self.head.next.previous = self.head.previous
            self.head = self.head.next
            self.sizes -= 1
            return 'Success'
        elif pos == self.sizes-1:
            if self.tail.previous != None:
                self.tail.previous.next = self.tail.next
            self.tail = self.tail.previous
            self.sizes -= 1
            return 'Success'
        else:
            rotary = self.head
            for i in range(pos-1):
                rotary = rotary.next
            rotary.next.next.previous = rotary
            rotary.next = rotary.next.next
            self.sizes -= 1
            return 'Success'


newlist = LinkedList()
newinp = input('Enter Input : ').split(',')
for j in newinp:
    if j[:2] == "AP":
        newlist.append(j[3:])
    elif j[:2] == "AH":
        newlist.addHead(j[3:])
    elif j[:2] == "SE":
        print("{0} {1} in {2}".format(newlist.search(j[3:]), j[3:], newlist))
    elif j[:2] == "SI":
        print("Linked List size = {0} : {1}".format(newlist.size(), newlist))
    elif j[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(
            j[3:], newlist.index(j[3:]), newlist))
    elif j[:2] == "PO":
        before = "{}".format(newlist)
        k = newlist.pop(int(j[3:]))
        print(("{0} | {1}-> {2}".format(k, before, newlist)) if k ==
              "Success" else ("{0} | {1}".format(k, newlist)))
    elif j[:2] == "IS":
        data = j[3:].split()
        newlist.insert(int(data[0]), data[1])
print("Linked List :", newlist)
print("Linked List Reverse :", newlist.reverse())
