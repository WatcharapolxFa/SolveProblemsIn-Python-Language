n = int(input("Input : "))

if n <= 0:
    print("!!!Please enter number greater than zero!!!")
else:
    print("  ")
    for i in range(n * 2):
        if i < n - 1:

            print("*" * (i + 1), " " * (n * 2 - 2 - (i * 2)),
                  "*" * (i + 1), sep="")
        elif i == n - 1:
            print("*" * (n * 2))
        else:
            n -= 1
            print("*" * n, " " * (i - n + 1), "*" * n, sep="")
