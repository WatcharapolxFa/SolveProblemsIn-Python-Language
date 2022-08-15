# if ซ้อน if

age = int(input("ป้อนอายุของคุณ : > "))
if age <= 15:
    print("ชั้นของคุณคือ ม.ต้น  ")
    if age == 15:
        print(">> ม.3")
    elif age == 14:
        print(">> ม.2")
    elif age == 13:
        print(">> ม.1")
elif age > 15 and age <= 18:
    print("ชั้นของคุณคือ ม.ปลาย  ")
    if age == 16:
        print(">> ม.4")
    elif age == 17:
        print(">> ม.5")
    elif age == 18:
        print(">> ม.6")
