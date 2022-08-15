def move(n, A, B, C):
    if n > 0:
        move(n-1, A, C, B)
        lists[C-1].append(lists[A-1].pop())
        print("move", n, "from ", chr(ord('A')+A-1), "to", chr(ord('A')+C-1))
        print("|  |  |")
        printall(lists[0], lists[1], lists[2], fix_size)
        move(n-1, B, A, C)


def printall(a, b, c, x):
    if x == 0:
        return
    else:
        if len(a) >= x:
            print(a[x-1], end='  ')
        else:
            print("| ", end=' ')
        if len(b) >= x:
            print(b[x-1], end='  ')
        else:
            print("| ", end=' ')
        if len(c) >= x:
            print(c[x-1], end='  ')
        else:
            print("| ", end=' ')
        print()
        printall(a, b, c, x-1)


def init(n):
    if n == 0:
        return []
    return [n] + init(n-1)


fix_size = int(input("Enter Input : "))
lists = [[]]*3
lists[0] = init(fix_size)
lists[1] = list()
lists[2] = list()
print("|  |  |")
printall(lists[0], lists[1], lists[2], fix_size)
move(fix_size, 1, 2, 3)
