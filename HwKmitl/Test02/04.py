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

    def push_front(self, data):
        if self.isEmpty():
            self.head = self.tail = self.Node(data)
        else:
            Check = self.Node(data, self.head)
            self.head = Check
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

    def content(self, other):
        if len(self) != len(other):
            return False
        str1 = str(self)
        str2 = str(other)

        list1 = []
        list2 = []

        list1 = str1.split()
        list2 = str2.split()

        list1 = sorted(list1)
        list2 = sorted(list2)
        return list1 == list2


if __name__ == '__main__':
    splitted = input('List1,List2 : ').split(',')
    list1 = splitted[0].split()
    list2 = splitted[1].split()
    link1 = LinkedList()
    link2 = LinkedList()
    for item in list1:
        link1.append(item)
    for item in list2:
        link2.append(item)
    print('List1 content Equivalence List2 : ' +
          str(link1.content(link2)))
