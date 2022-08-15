# Assignment รับข้อมูลและเรียงลำดับ
number = []
while True:
    x = int(input("ป้อนตัวเลขของคุณ >>> "))
    if x < 0:
        break
    number.append(x)
print("ก่อน >> ", number)
number.sort()
print("หลัง >>> ", number)
