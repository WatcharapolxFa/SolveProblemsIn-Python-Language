def recurfor(i, n, inpu):
    if i == n:
        return
    if inpu[i] > inpu[i+1]:
        inpu[i], inpu[i+1] = inpu[i+1], inpu[i]
    recurfor(i+1, n, inpu)


def callrecur(i, n, inpu):
    if i == n:
        return
    recurfor(0, n, inpu)
    callrecur(i, n-1, inpu)


inp = list(map(int, input('Enter Input : ').split()))
callrecur(0, len(inp)-1, inp)
print(inp)
