def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


nweinp = input("Enter Input : ").split()
number = int(nweinp[0])
number2 = int(nweinp[1])
if number == 0 and number2 == 0:
    print("Error! must be not all zero.")
elif number > 0 and number2 > 0:
    if number > number2:
        print("The gcd of {} and {} is : {}".format(
            number, number2, abs(gcd(number, number2))))
    else:
        print("The gcd of {} and {} is : {}".format(
            number2, number, abs(gcd(number2, number))))
elif number == 0 or number2 == 0:
    if number < number2:
        print("The gcd of {} and {} is : {}".format(
            number2, number, abs(gcd(number2, number))))
    else:
        print("The gcd of {} and {} is : {}".format(
            number, number2, abs(gcd(number, number2))))
elif number < 0 or number2 < 0:
    if abs(number) < abs(number2):
        print("The gcd of {} and {} is : {}".format(
            number2, number, abs(gcd(number2, number))))
    else:
        print("The gcd of {} and {} is : {}".format(
            number, number2, abs(gcd(number, number2))))
