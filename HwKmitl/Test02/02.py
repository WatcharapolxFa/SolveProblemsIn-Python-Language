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
            check = self.head
            self.size = 1
            while check.next != None:
                check = check.next
                self.size += 1
            self.tail = check

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


class Queue:
    def __init__(self):
        self.items = LinkedList()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.removeHead()

    def __len__(self):
        return len(self.items)

    def __str__(self):
        if not self.is_empty():
            out = 'Queue data : '
            for i in range(len(self.items)):
                val = self.items.nodeAt(i).data
                out += str(val) + ' '
            return out
        return 'Empty Queue'


if __name__ == '__main__':
    CheckState = int(input('Enter choice : '))
    if CheckState == 1:
        newQ = Queue()
        newQ.enqueue(10)
        newQ.enqueue(20)
        newQ.enqueue(30)
        print(newQ)
        newQ.dequeue()
        newQ.enqueue(40)
        print("Size of Queue :", len(newQ))
        print(newQ)
    elif CheckState == 2:
        newQ = Queue()
        newQ.enqueue(100)
        newQ.enqueue(200)
        newQ.enqueue(300)
        newQ.dequeue()
        print(newQ)
        print("Queue is Empty :", newQ.is_empty())
    elif CheckState == 3:
        newQ = Queue()
        newQ.enqueue(11)
        newQ.enqueue(22)
        newQ.enqueue(33)
        newQ.dequeue()
        newQ.dequeue()
        newQ.dequeue()
        print(newQ)
        print("Size of Queue :", len(newQ))
        print("Queue is Empty :", newQ.is_empty())
