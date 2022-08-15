def hbd(age):

    for i in range(age, 3, -1):

        if age % (i-1) == 0:
            if int((age/(i-1))) % (i-1) == 2:
                count = 20
                break
        if age % (i-1) == 1:

            if int((age/(i-1))) % (i-1) == 2:
                count = 21
                break
    return count, i-1


year = input("Enter year : ")
count, year = hbd(int(year))
print("saimai is just {}, in base {}!".format(count, year))

# num1 = age
# num2 = age
# if age % 2 == 0:
#     num1 = num1 % 20
#     print(str(20), num1)
# else:
#     num2 = num2 % 21
#     print("21", num2)
