class queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        if self.isEmpty():
            return
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


kon, time = input("Enter people and time : ").split()
kon = [i for i in kon]
people = queue(kon)
Q1 = queue()
Q2 = queue()
check = 0
check1 = 0
check2 = 0
for i in range(1, int(time)+1):
    item = ""
    if people.isEmpty() == False:
        item += people.deQueue()
    else:
        check += 1

    if i > 2:
        if check1 == 3:
            Q1.deQueue()
            check1 = 0
        if check2 == 2:
            Q2.deQueue()
            check2 = 0

    if people.isEmpty() == False or check == 0:
        if Q1.size() < 5:
            Q1.enQueue(item)
        else:
            Q2.enQueue(item)

    if Q1.isEmpty() == False:
        check1 += 1
    if Q2.isEmpty() == False:
        check2 += 1
    print(i, people.items, Q1.items, Q2.items, sep=" ")
