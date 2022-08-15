# วิธีแรก
cheeck = input("ต้องการแปลง F >> C พิมพ์ (1) C >> F พิมพ์ (2)  : ")
cheeck = int(cheeck)  # นำ int(ตัวที่ต้องการแปลง)
if cheeck == 1:
    num = int(input("ป้อนอุณหภูมิ จาก  F >> C : "))
    sum = (num-32)*5/9
    print(" >> F ", num, "องศา", " >> C", sum, "องศา")


elif cheeck == 2:
    nUm = int(input("ป้อนอุณหภูมิ จาก  C >> F : "))
    sUm = (nUm * 9)/5+32
    print(" C >> ", nUm, "องศา", " >> F", sUm, "องศา")

else:
    print("กรุณากรอกตัวเลขให้ถูกต้อง")

# วิธีที่สอง
temp = input("ป้อนอุณหภูมิ (องศา):")

degree = int(temp[:-1])
unit = temp[-1].upper()
if unit == "C":
    result = (9*degree)/5+32
    unit_result = "ฟาเรนไฮน์"
if unit == "F":
    result = (degree-32)*5/9
    unit_result = "เซลเซียส"

print("แปลงตัวเลข =", temp, "เป็น", unit_result, " = ", result)
