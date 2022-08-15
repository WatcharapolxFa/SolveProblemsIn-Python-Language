def sum2(l, fromI, toi):
    if fromI > toi:
        return 0
    elif fromI == toi:
        return l[toi]
    else:
        x = l[fromI]
        y = sum2(l+fromI+1, toi)
        return x + y


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum2(l, 0, len(l)-1))
