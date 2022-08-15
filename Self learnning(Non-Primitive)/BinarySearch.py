a = [1, 3, 4, 5, 17, 18, 31, 33, 35]


def search(low, high, x):
    while (low <= high):
        mid = (low + high) // 2
        if (x == a[mid]):
            return mid
        elif (a[mid] < x):
            low = mid + 1
        else:
            high = mid - 1
    return (-1)


# def search(low, high, x):
#     if(high < low):
#         return(-1)
#     mid = (low + high) // 2
#     if (x == a[mid]):
#         return (mid)
#     elif (a[mid] < x):
#         return search(mid+1, high, x)
#     else:
#         return search(low, mid-1, x)


# print(search(0, 8, 17))
