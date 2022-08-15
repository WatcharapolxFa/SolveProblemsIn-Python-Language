number = list(map(int, input("Enter All Bid : ").split()))
if len(number) == 1:
    print("not enough bidder")
    exit()
number.sort()  # เรียงจากน้อยไปมาก #มากไปน้อย .
if number[-1] == number[-2]:
    print("error : have more than one highest bid")
    exit()
print("winner bid is {} need to pay {}".format(number[-1], number[-2]))
exit()
