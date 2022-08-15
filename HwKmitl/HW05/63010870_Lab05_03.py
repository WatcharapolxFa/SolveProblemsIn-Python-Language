class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def createList(l=[]):
    newnode = node(int(l.pop(0)))
    head = newnode
    while len(l) > 0:
        newnode.next = node(int(l.pop(0)))
        newnode = newnode.next
    return head


def printList(H):
    data = []
    while H is not None:
        data.append(str(H.data))
        H = H.next
    print(' '.join(data))


head = None


def mergeOrderesList(count, check):
    while count is not None:
        sorts(count.data)
        count = count.next
    while check is not None:
        sorts(check.data)
        check = check.next
    return head


def sorts(data):
    global head
    rotary = head
    if rotary is None:
        n = node(data)
        head = n
        return

    if rotary.data > data:
        n = node(data)
        n.next = rotary
        head = n
        return

    while rotary.next is not None:
        if rotary.next.data > data:
            break
        rotary = rotary.next
    n = node(data)
    n.next = rotary.next
    rotary.next = n
    return


#################### FIX comand ####################
newlist, list = map(str, input("Enter 2 Lists : ").split())
LL1 = createList(newlist.split(','))
LL2 = createList(list.split(','))
print('LL1 : ', end='')
printList(LL1)
print('LL2 : ', end='')
printList(LL2)
strm = mergeOrderesList(LL1, LL2)
print('Merge Result : ', end='')
printList(strm)
