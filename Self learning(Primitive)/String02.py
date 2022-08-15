fname = "Wacharapol"
lname = "Yotadee"
age = "80"
salary = 999.9999
print("Name > "+fname+"\tLast Name > "+lname)

# จัดรูปแบบการแสดงผล
text = "Name >{} \tLast Name {}>\t Agr > {}\t Salary > {}"
print(text.format(fname, lname, age, salary))

# นับจำนวนคำในตัวแปร
markets = "ฉันไปซื้อผักและผลไม้เพื่อมาทำกับข้าวแต่ฉันลืมว่าต้องซื้อผักกาดและหมูสับไป เดี่ยวฉันมานะ"
print(markets.count("ผัก"))

# เช็คคำขึ้นต้นและคำลงท้าย

thai = "990739"

# if lottory.startswith("9"):
#     print("ถูกหวย")
# else:
#     print("ถูกกิน")

if thai.endswith("0"):
    print("ถูกหวย")
else:
    print("ถูกกิน")
