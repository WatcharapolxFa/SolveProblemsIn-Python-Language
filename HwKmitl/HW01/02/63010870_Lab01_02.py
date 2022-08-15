def sum():
    print("*** multiplication or sum ***")

    number, nUmber = list(map(int, input("Enter num1 num2 : ").split(' ')))
    #number, nUmber = [int(x) for x in input("Enter num1 num2 : ").split()]
    sum = number * nUmber
    if sum > 1000:
        sUm = number + nUmber
        print("The result is", sUm)

    elif sum <= 1000:
        suM = number * nUmber
        print("The result is", suM)


sum()


# print("*** multiplication or sum ***")
# number, nUmber = [int(x) for x in input("Enter num1 num2 : ").split()]
# result = number+nUmber if (number*nUmber) > 1000 else number*nUmber
# print("The result is %.0f" % result)
