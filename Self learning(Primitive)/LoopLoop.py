count = 1
while count <= 3:
    point = 1
    while point <= 5:
        print("รอบที่ ", count, "ตำแหน่งที่  = ", point)
        point += 1
    count += 1

for i in range(1, 4):
    print("รอบที่ ", i)
    for j in range(1, 6):
        print("ตำแหน่งที่ ", j)
