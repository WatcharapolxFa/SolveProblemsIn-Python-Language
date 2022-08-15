print(" *** Recite the multiplication table ***")
inp = input("Enter pattern for child 1 to 3 (-1 for sep) : ").split("-1")

a = list(map(int, inp[0].split()))
b = list(map(int, inp[1].split()))
c = list(map(int, inp[2].split()))
tmp1 = [-1, 0, len(a)]
tmp2 = [-2, 0, len(b)]
tmp3 = [-3, 0, len(c)]
count = 0
check = True

while True:
    if tmp1[1] == tmp1[2]:
        tmp1[1] = 0
    if tmp2[1] == tmp2[2]:
        tmp2[1] = 0
    if tmp3[1] == tmp3[2]:
        tmp3[1] = 0
    count += 1
    tmp1[0], tmp2[0], tmp3[0] = a[tmp1[1]], b[tmp2[1]], c[tmp3[1]]
    if tmp1[0] == tmp2[0] == tmp3[0]:
        break
    tmp1[1] += 1
    tmp2[1] += 1
    tmp3[1] += 1
    if count > 365:
        check = False
        break
a = list(map(str, inp[0].split()))
b = list(map(str, inp[1].split()))
c = list(map(str, inp[2].split()))
aa = " ".join(a)
bb = " ".join(b)
cc = " ".join(c)
print("    ")
print(f"Pattern for child 1 : {aa}")
print(f"Pattern for child 2 : {bb}")
print(f"Pattern for child 3 : {cc}")
if check:
    print(f"They recite same multiplication table in {count} days")
else:
    print("This year they never recite same multiplication table !!!")
