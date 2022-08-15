class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def index(self, item):
        rotary = self.head
        count = 0
        while rotary != None:
            if rotary.data == item:
                return count
            count += 1
            rotary = rotary.next
        if rotary == None:
            return '-1'

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head == None:
            self.addHead(item)
        else:
            rotary = self.head
            while rotary.next != None:
                rotary = rotary.next
            rotary.next = Node(item)

    def search(self, item):
        rotary = self.head
        while rotary != None:
            if rotary.data == item:
                return 'Found'
            rotary = rotary.next
        if rotary == None:
            return 'Not Found'

    def addHead(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    def remove(self, item):
        rotary = self.head
        if rotary is not None:
            if rotary.data == item:
                self.head = rotary.next
                rotary = None
                return
        while rotary is not None:
            if rotary.data == item:
                break
            prev = rotary
            rotary = rotary.next
        if rotary == None:
            return
        prev.next = rotary.next
        rotary = None

    def size(self):
        rotary = self.head
        count = 0
        while rotary != None:
            rotary = rotary.next
            count += 1
        return count

    def pop(self, item):
        rotary = self.head
        if item == 0:
            if not self.isEmpty():
                self.head = self.head.next
                return "Success"
            else:
                return "Out of Range"
        else:
            previous = None
            index = 0
            while rotary is not None:
                if index == item:
                    previous.next = rotary.next
                    return "Success"
                index += 1
                previous = rotary
                rotary = rotary.next
            return "Out of Range"

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, f = self.head, str(self.head.data) + " "
        while cur.next != None:
            f += str(cur.next.data) + " "
            cur = cur.next
        return f


newlist = LinkedList()
newinput = input('Enter Input : ').split(',')
for count in newinput:
    if count[:2] == "AP":
        newlist.append(count[3:])
    elif count[:2] == "AH":
        newlist.addHead(count[3:])
    elif count[:2] == "SE":
        print("{0} {1}".format(newlist.search(count[3:]), count[3:]), end='')
        print(" in {}".format(newlist))
    elif count[:2] == "SI":
        print("Linked List size = {0} : {1}".format(newlist.size(), newlist))
    elif count[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(
            count[3:], newlist.index(count[3:]), newlist))
    elif count[:2] == "PO":
        before = "{}".format(newlist)
        lastlist = newlist.pop(int(count[3:]))
        print(("{0} | {1}-> {2}".format(lastlist, before, newlist)) if lastlist ==
              "Success" else ("{0} | {1} ".format(lastlist, newlist)))
print("Linked List :", newlist)
