def bon(x):
    counter = 0
    num = x[0]
    for i in x:
        curr_frequency = x.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
    result = (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'].index(num)+1)*4  # index เข้าถึงตำแหน่ง
    return result


secretCode = list(input("Enter secret code : "))
print(bon(secretCode))
