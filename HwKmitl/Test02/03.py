class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next

        def __str__(self):
            return str(self.data)

    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None:
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self):
        Status = 'Linked data : '
        Checkcount = self.head
        while Checkcount != None:
            Status += str(Checkcount.data) + ' '
            Checkcount = Checkcount.next
        return Status

    def __len__(self):
        return self.size

    def append(self, data):
        Check = self.Node(data)
        if self.head == None:
            self.head = self.tail = Check
        else:
            count = self.tail
            count.next = Check
            self.tail = Check
        self.size += 1

    def removeHead(self):
        if self.head == None:
            return
        if self.head.next == None:
            newp = self.head
            self.head = None
        else:
            newp = self.head
            self.head = self.head.next
        self.size -= 1
        return newp.data

    def isEmpty(self):
        return self.size == 0

    def nodeAt(self, i):
        checks = self.head
        for j in range(i):
            checks = checks.next
        return checks

    def removeDup(self):
        if not self.isEmpty():
            lists = {}
            Check = None
            buffers = self.head
            while buffers is not None:

                if lists.get(buffers.data, 0) == 0:
                    lists[buffers.data] = 1
                    Check = buffers
                    buffers = buffers.next
                else:
                    if buffers.next is not None:
                        Check.next = buffers.next
                        buffers.next = None
                        buffers = Check.next
                    else:
                        Check.next = None
                        buffers = None


if __name__ == '__main__':
    inputlist = [int(f) for f in input('Enter numbers : ').split()]

    newlist = LinkedList()
    for item in inputlist:
        newlist.append(item)
    print("Linkedlist Before removeDuplicate")
    print(newlist)
    print("Linkedlist After removeDuplicate")
    newlist.removeDup()
    print(newlist)
