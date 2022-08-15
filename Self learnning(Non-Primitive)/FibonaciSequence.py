def fibonaciSequenceIterative(n):
    if n == 0 or n == 1:
        return n
    else:
        low, hight = 0, 1
        for i in range(2, n+1):
            new = hight+low
            low = hight
            hight = new
            return new


for i in range(51):
    print(i, fibonaciSequenceIterative(i))


def fibonaciSequenceRecursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonaciSequenceRecursive(n-1) + fibonaciSequenceRecursive(n-2)


for i in range(51):
    print(i, fibonaciSequenceRecursive(i))
