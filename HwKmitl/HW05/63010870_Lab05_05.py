class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None, None)

    def __str__(self):
        sta = ''
        fa = self.head.next
        while fa is not None:
            sta += str(fa.data)
            if fa.next is not None:
                sta += ' -> '
            fa = fa.next
        return sta

    def display(self):
        sta = ''
        fa = self.head.next
        while fa is not None:
            sta += str(fa.data) + ' '
            fa = fa.next
        return sta

    def size(self):
        count = 0
        fa = self.head.next
        while fa is not None:
            count += 1
            fa = fa.next
        return count

    def checkMaxAndInsert(self, newValue):
        fa = self.head.next
        for index in range(self.size()):
            if newValue > fa.data:
                self.insert(index, newValue)
                return
            fa = fa.next
        else:
            self.append(newValue)

    def isEmpty(self):
        return self.size() == 0

    def nodeAt(self, index):
        fa = self.head
        for _ in range(-1, index):
            fa = fa.next
        return fa

    def insert(self, index, data):
        prevNode = self.nodeAt(index - 1)
        newNode = Node(data, prevNode.next)
        prevNode.next = newNode

    def append(self, data):
        self.insert(self.size(), data)

    def pop(self, index):
        if self.isEmpty():
            return 'No more to pop'
        if index > self.size() - 1:
            return 'out of range'

        prevNode = self.nodeAt(index - 1)
        nextNode = prevNode.next.next
        popNode = prevNode.next
        prevNode.next = nextNode
        return popNode


def radixSort(linkedList):
    state = False
    times = 0
    sizes = linkedList.size()
    zeroLink = SinglyLinkedList()
    oneLink = SinglyLinkedList()
    twoLink = SinglyLinkedList()
    threeLink = SinglyLinkedList()
    fourLink = SinglyLinkedList()
    fiveLink = SinglyLinkedList()
    sixLink = SinglyLinkedList()
    sevenLink = SinglyLinkedList()
    eightLink = SinglyLinkedList()
    nightLink = SinglyLinkedList()

    for check in range(1000):
        for _ in range(sizes):
            popNode = linkedList.pop(0)

            originalData = popNode.data
            if originalData >= 0:
                calculatedData = originalData // 10 ** check
            else:
                calculatedData = -originalData // 10 ** check

            if calculatedData % 10 == 0:
                zeroLink.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 1:
                oneLink.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 2:
                twoLink.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 3:
                threeLink.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 4:
                fourLink.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 5:
                fiveLink.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 6:
                sixLink.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 7:
                sevenLink.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 8:
                eightLink.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 9:
                nightLink.checkMaxAndInsert(originalData)

        print('------------------------------------------------------------')
        print('Round :', check + 1)
        print('0 :', zeroLink.display())
        print('1 :', oneLink.display())
        print('2 :', twoLink.display())
        print('3 :', threeLink.display())
        print('4 :', fourLink.display())
        print('5 :', fiveLink.display())
        print('6 :', sixLink.display())
        print('7 :', sevenLink.display())
        print('8 :', eightLink.display())
        print('9 :', nightLink.display())

        if not zeroLink.isEmpty() and oneLink.isEmpty() and twoLink.isEmpty() and \
                threeLink.isEmpty() and fourLink.isEmpty() and fiveLink.isEmpty() and \
                sixLink.isEmpty() and sevenLink.isEmpty() and eightLink.isEmpty() and nightLink.isEmpty():
            state = True

        while not zeroLink.isEmpty():
            linkedList.append(zeroLink.pop(0).data)
        while not oneLink.isEmpty():
            linkedList.append(oneLink.pop(0).data)
        while not twoLink.isEmpty():
            linkedList.append(twoLink.pop(0).data)
        while not threeLink.isEmpty():
            linkedList.append(threeLink.pop(0).data)
        while not fourLink.isEmpty():
            linkedList.append(fourLink.pop(0).data)
        while not fiveLink.isEmpty():
            linkedList.append(fiveLink.pop(0).data)
        while not sixLink.isEmpty():
            linkedList.append(sixLink.pop(0).data)
        while not sevenLink.isEmpty():
            linkedList.append(sevenLink.pop(0).data)
        while not eightLink.isEmpty():
            linkedList.append(eightLink.pop(0).data)
        while not nightLink.isEmpty():
            linkedList.append(nightLink.pop(0).data)

        if state is True:
            break
        times += 1
    return linkedList, times


newinp = [int(i) for i in input('Enter Input : ').split()]

LinkOrigins = SinglyLinkedList()
newList = SinglyLinkedList()


for j in newinp:
    newList.append(j)
    LinkOrigins.append(j)

time = 0
radixLinked, time = radixSort(newList)
print('------------------------------------------------------------')
print(time, 'Time(s)')
print('Before Radix Sort :', LinkOrigins)
print('After  Radix Sort :', radixLinked)
