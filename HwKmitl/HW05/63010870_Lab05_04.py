class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.size = 0

    def __str__(self):
        rotary = self.head.next
        string = ""
        count = 0
        while rotary is not None:
            string += str(rotary.data) + " "
            rotary = rotary.next

            if count >= self.size:
                return "Found Loop"
            count += 1

        if string == "":
            return "Empty"
        else:
            return "->".join(string.split())

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        rotary = self.head
        while rotary.next is not None:
            rotary = rotary.next
        rotary.next = Node(data, None)
        self.size += 1

    def setNextOnNode(self, src_position, des_position):
        rotary = self.head
        for i in range(src_position+1):
            rotary = rotary.next

        rotary_des = self.head
        for i in range(des_position+1):
            rotary_des = rotary_des.next

        print("Set node.next complete!, index:value = {}:{} -> {}:{}".format(
            src_position, rotary.data, des_position, rotary_des))
        rotary.next = rotary_des


commandListes = input("Enter input : ").split(',')

singlyLinkedList = SinglyLinkedList()
for command in commandListes:
    option = command.split()[0]

    if option == 'A':
        param = command.split()[1]
        singlyLinkedList.append(param)
        print(singlyLinkedList)

    elif option == 'S':
        firstParammiter, secondParamiter = command.split()[1].split(':')
        firstParammiter = int(firstParammiter)
        secondParamiter = int(secondParamiter)
        if singlyLinkedList.isEmpty():
            print("Error! {list is empty}")
        else:
            if firstParammiter >= singlyLinkedList.size or firstParammiter < 0:
                print("Error! {index not in length}:", firstParammiter)
            else:
                if secondParamiter >= singlyLinkedList.size or secondParamiter < 0:
                    singlyLinkedList.append(secondParamiter)
                    print("index not in length, append :", secondParamiter)
                else:
                    singlyLinkedList.setNextOnNode(
                        firstParammiter, secondParamiter)

if str(singlyLinkedList) != "Found Loop":
    print("No Loop")
print(singlyLinkedList)
