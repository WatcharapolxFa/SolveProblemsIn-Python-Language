class LinkedList:
    def __init__(self, list=None):
        if list == None:
            self.word = []
        else:
            self.word = list

    def push(self, i):
        self.word.append(i)

    def pop(self):
        return self.word.pop()

    def isEmpty(self):
        return self.word == []

    def size(self):
        return len(self.word)

    def reverse(self):
        newList = []
        for i in range(len(self.word)):
            newList.append(self.word.pop())
        self.word.extend(newList)

    def extend(self, list):
        self.word.extend(list)

    def __str__(self):
        if not self.isEmpty():
            out = "Linked data : "
            for word in self.word:
                out += str(word)+' '
            return out
        return 'Empty'

    def sort(self):
        newList = []
        while self.word:
            minimum = self.word[0]
            for x in self.word:
                if x < minimum:
                    minimum = x
            newList.append(minimum)
            self.word.remove(minimum)
        self.word = newList


def findMean(lst):
    sum = 0
    for i in lst:
        sum = sum+int(i)
    Mid = float(sum/len(lst))
    print("Mean = %.2f" % Mid)


def findmedian(lst):
    if(len(lst) % 2 != 0):
        ind = int(((len(lst)+1)/2))
        medium = float(lst[ind])
        print("Median  = %.2f" % medium)
    if(len(lst) % 2 == 0):
        ind1 = int(((len(lst))/2))
        ind2 = ind1 + 1
        x = float(lst[ind1])
        y = float(lst[ind2])
        medium = float((x+y) / 2)
        print("Median  = %.2f" % medium)


inputlists = [int(e) for e in input('Enter numbers : ').split()]
lst = LinkedList()
lst.extend(inputlists)
print("Output :")
lst.sort()
print(lst)
print("Amount of data =", lst.size())
lsts = [e for e in str(lst).split(' ')]
findMean(inputlists)
findmedian(lsts)
