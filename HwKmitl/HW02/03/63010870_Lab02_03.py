def odd_even(arr, s):
    lts = []
    if type(arr) == str:
        strs = ""
        if s == "Odd":
            for i in range(0, len(arr), 2):
                strs += arr[i]

        elif s == "Even":
            for i in range(1, len(arr), 2):
                strs += arr[i]
        print(strs)

    elif type(arr) == list:
        lists = []
        if s == "Odd":
            for i in range(0, len(arr), 2):
                lists.append(arr[i])

        elif s == "Even":
            for i in range(1, len(arr), 2):
                lists.append(arr[i])
        print(lists)


print("*** Odd Even ***")
checktype, checkdata, check = input("Enter Input : ").split(',')
if checktype == 'S':
    odd_even(checkdata, check)
elif checktype == 'L':
    odd_even(checkdata.split(), check)
