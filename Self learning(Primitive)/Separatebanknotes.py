number = int(input("ป้อนจำนวนเงินของคุณ >> "))

# / หารปกติ //หารตัดทศนิยม
if number >= 1000:
    print(" 1000 บาท = ", number//1000, "ใบ")
    number = number % 1000
if number >= 500:
    print(" 500 บาท = ", number//500, "ใบ")
    number = number % 500
if number >= 100:
    print("100 บาท = ", number//100, "ใบ")
    number = number % 100

if number >= 50:
    print("50 บาท = ", number//50, "ใบ")
    number = number % 50
if number >= 20:
    print("20 บาท = ", number//20, "ใบ")
    number = number % 20
print("<< ขอบคุณที่ใช้บริการครับ >> ")
