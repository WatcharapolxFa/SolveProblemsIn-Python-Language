name = "watcharapol อายุ 19 19นิ้ว"

# แสดงข้อความแบบตัด print(ชื่อตัวแปร[ตัวเริ่ม:ตัวสุดท้ายที่ต้องการ])
print(name[0:3])  # กรณีนี้นับช่องว่างด้วย

# แสดงข้อความแบบตัด print(ชื่อตัวแปร[ตัวเริ่ม:ตัวสุดท้ายที่ต้องการ])
# หลังไปหน้า
print(name[-2:])  # กรณีนี้นับช่องว่างด้วย

# นับจำนวน String
print(len(name))
# ลบช่องว่างซ้ายขวา ถ้าอยากลบข้างใดข้างหนึ่งใช้คำสั่ง rstrip() หรือ lstrip()
name = name.strip()
print(len(name))


print(name.upper())  # String เป็นพิมพ์ใหญ่

print(name.lower())  # String เป็นพิมพ์เล็ก

print(name.capitalize())  # String ตัวแรกพิมพ์ใหญ่ที่เหลือเล็ก

print(name.replace("pol", "555"))  # แทนที่ " " == " "

print(name.replace("19", "20", 1))  # แทนที่ " " == " ",ตำแหน่ง

# เช็คว่ามีคำนี้ในประโยคไหม
x = "wat" in name
print(x)
