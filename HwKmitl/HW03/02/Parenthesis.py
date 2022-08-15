open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


lists = input("Enter expresion : ")
s1 = Stack()
# Function to check parentheses
for i in lists:
    if i in open_list:
        s1.push(i)
    elif i in close_list:
        pos = close_list.index(i)
        if ((len(s1) > 0) and (open_list[pos] == s1[len(s1) - 1])):

            s1.pop()
        else:
            print("Unbalanced")
    if s1.isEmpty():
        print("Balanced")
    else:
        print("Unbalanced")


# start = ""
# count01 = 0
# count02 = 0
# count03 = 0
# count04 = 0
# last = ""
# for i in lists:
#     s1.push(i)
# while not s1.isEmpty():
#     count = s1.pop()
#     if count01 == 0 and count02 == 0 and count03 == 0 and count04 == 0:
#         check = count
#     if count == "[":
#         count01 += 1
#     if count == "]":
#         count02 += 1
#     if count == "(":
#         count03 += 1
#     if count == ")":
#         count04 += 1
#     if s1.isEmpty():
#         last = count
# if count01 != 0 and count01 > count04 or count02 != 0 and count01 > count04:
#     if count01 > count02:
#         print("".join(lists)+" open paren excess   " +
#               str(count01)+" "+"["*count01)
#     elif count01 < count02:
#         print("".join(lists)+" close paren excess")
# elif count03 != 0 and count03 > count02 or count04 != 0 and count03 > count02:
#     if count03 > count04:
#         print("".join(lists)+" open paren excess   " +
#               str(count03)+" "+"("*count03)
#     elif count03 < count04:
#         print("".join(lists)+" close paren excess")
# else:
#     if start == "[" and last == "]" or start == "(" and last == ")":
#         print("".join(lists)+" Match")
#     else:
#         print("".join(lists)+" Unmatch open-close")
