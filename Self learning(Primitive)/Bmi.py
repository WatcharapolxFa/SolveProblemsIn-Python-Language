
name = (input("ป้อนชื่อจริงของท่าน = > "))
wight = float(input("ป้อนน้ำหนักของท่าน(Kg) => "))
hight = float(input("ป้อนส่วนสูงของท่าน(M)=> "))
print("น้ำหนักของท่านคือ => ", wight)
print("ส่วนสูงของท่านคือ => ", hight)
sum = wight/(hight*hight)
result = "ไม่ที่บค่าที่ชัดเจน"
if sum > 0 and sum < 18:
    result = " ต่ำกว่าเกณฑ์ "
elif sum > 18.5 and sum < 24.9:
    result = " สมส่วน "
elif sum > 25.0 and sum < 29.9:
    result = " น้ำหนักเกิน "
else:
    result = " โรคอ้วน "
print("ค่า BMI ของท่านคือ => ", sum, "เกณฑ์ BMI ของท่านคือ => ", result)
"""
<18 ต่ำกว่าเกณฑ์
23.0 - 24.9  = สมส่วน
25.0 - 29.9 = น้ำหนักเกิน
>30 = โรคอ้วน
"""
