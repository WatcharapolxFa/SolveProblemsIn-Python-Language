def natural_sum(n):
    if n <= 0:
        return n
    else:
        return n+natural_sum(n-1)


def print_Num(n, k):
    if n == k:
        return n
    else:
        print(n, "+ ", end="")
        return n+print_Num(n+1, k)


print(" *** Natural sum ***")
num = int(input("Enter number : "))
print_Num(num-(num-1), num)
print(num, "=", natural_sum(num), end="")
