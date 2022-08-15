# เกมทายเลขลูกเต๋า
# 1,2,3,4,5,6

import random

ran = random.randrange(1, 7)  # 1-6

count = 1
print("ตอบได้สูงสุด 3 ครั้ง")
while True:
    number = int(input("ป้อนคำตอบของคุณ : "))

    check = (number == ran)  # true / false
    if not check:
        if(number > ran):
            print("เค้าใบ้ให้นะ >> ป้อนที่น้อยกว่า >< ")
        else:
            print("เค้าใบ้ให้นะ >> ป้อนที่มากกว่า >< ")
    if check == True:
        print(" You Winner >><<")
        break

    else:
        print("You lose")

    if number < 0 or count == 3:
        break
    count += 1
print("เฉลย >> ", ran, "\nจบการทำงาน")
