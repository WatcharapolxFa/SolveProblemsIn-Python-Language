start = int(input("ป้อแม่สูตรคูณเริ่มต้น >> "))
stop = int(input("ป้อแม่สูตรสุดท้าย >> "))

for x in range(start, stop+1):
    print("\nแม่ที่ >> ", x)
    for y in range(1, 13):
        print(x, 'x', y, '=', (x*y))
