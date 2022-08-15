max, min = 0, 100
while True:
    num = int(input("ป้อนตัวเลขที่ต้องการหา >>"))
    if num < 0:
        break
    if num > max:
        max = num
    if num < min:
        min = num
    print("ค่าต่ำสุด >>", min, "ค่าสูงสุด", max)
