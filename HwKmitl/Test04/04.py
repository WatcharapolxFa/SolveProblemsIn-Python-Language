def search(data, ser):
    m = max(data)
    if ser > m:
        print(str(ser) + " out of bound.")
        return
    for i in range(len(data)):
        if ser == data[i]:
            print("Found " + str(ser))
            return
    for i in range(len(data)):
        x = ser + i + 1
        for i in range(len(data)):
            if x == data[i]:
                print(str(data[i]) + " is successor of " + str(ser))
                return


print(" *** Search from list ***")
inp = input('Enter Input : ').split('/')
data, ser = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for i in range(len(ser)):
    search(data, ser[i])
