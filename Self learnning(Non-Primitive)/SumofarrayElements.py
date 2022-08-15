def sum(n, l):
    if n is 0:  # none list base case
        return 0
    elif n is 1:  # base case
        return l[0]
    else:
        return sum(n-1, l) + l[n-1]


l = [7, 3, 5, 4, 2, 6, 8, 9, 1]
print(sum(len(l)), l)
