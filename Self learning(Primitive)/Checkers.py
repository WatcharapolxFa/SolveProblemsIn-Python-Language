"""
#####
#####
#####

##
##
"""

number = int(input("ป้อนขนาดที่ต้องการหา >>"))

for row in range(number):
    for column in range(number):
        print("x", end='') if(row == column) % 2 == 0 else print("o", end='')
    print(" ")

"""
####
#  #
####
"""
number = int(input("ป้อนขนาดที่ต้องการหา >>"))

for row in range(number):
    for column in range(number):
        if row == 0 or row == number-1 or column == 0 or column == number-1:
            print("x", end='')
        else:
            print(" ", end='')
    print(" ")
