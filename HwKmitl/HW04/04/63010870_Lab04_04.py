def combine(inp):
    value = []
    value[:0] = inp
    return int(value[0])  # จะเอาตัวแรกค่าที่ป้อนเข้ามา


inp1, inp2 = input("Enter Input : ").split("/")
listinp = inp2.split(",")
listput = []


for i in range(len(listinp)):  # D,E 101,E 201,E 102,D,D,D,D
    check_str = listinp[i]
    if(check_str != 'D'):  # มันจะเป็น E แน่นอน
        value = check_str.split(" ")
        checksame = False
        for j in range(len(listput)):
            if(combine(str(value[1])) == combine(str(listput[j]))):
                if(j+1 < len(listput)):
                    if(combine(str(value[1])) != combine(str(listput[j+1]))):
                        listput.insert(j+1, value[1])
                        checksame = True
                        break

        if(checksame == False):
            listput.append(value[1])

    if(check_str == 'D'):
        if(listput == []):
            print("Empty")
        else:
            print(listput.pop(0))
