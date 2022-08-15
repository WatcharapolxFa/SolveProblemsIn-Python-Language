# gcd
def gcd(num, num1):
    if num1 == 0:
        return num
    else:
        return gcd(num1, num % num1)


inp = input("Enter Input : ").split()
number01 = int(inp[0])
number02 = int(inp[1])
if number01 == 0 and number02 == 0:
    print("Error! must be not all zero.")
elif number01 > 0 and number02 > 0:
    if number01 > number02:
        print("The gcd of {} and {} is : {}".format(
            number01, number02, abs(gcd(number01, number02))))
    else:
        print("The gcd of {} and {} is : {}".format(
            number02, number01, abs(gcd(number02, number01))))
elif number01 == 0 or number02 == 0:
    if number01 < number02:
        print("The gcd of {} and {} is : {}".format(
            number02, number01, abs(gcd(number02, number01))))
    else:
        print("The gcd of {} and {} is : {}".format(
            number01, number02, abs(gcd(number01, number02))))
elif number01 < 0 or number02 < 0:
    if abs(number01) < abs(number02):
        print("The gcd of {} and {} is : {}".format(
            number02, number01, abs(gcd(number02, number01))))
    else:
        print("The gcd of {} and {} is : {}".format(
            number01, number02, abs(gcd(number01, number02))))
