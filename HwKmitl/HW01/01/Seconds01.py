print("*** Converting hh.mm.ss to seconds ***")
hour, minute, second = list(map(int, input("Enter hh mm ss : ").split(' ')))
if hour < 24:
    if minute < 60 and minute >= 0:
        if second < 60 and second >= 0:
            sum = 0
            sum += hour*3600
            sum += minute*60
            sum += second
            print("{:02d}:{:02d}:{:02d} = {:,} seconds".format(
                hour, minute, second, sum))  # {:,}ตัวคั้นหลักร้อย
        else:
            print("ss({:02d}) is invalid!".format(second))
    else:
        print("mm({:02d}) is invalid!".format(minute))
else:
    print("hh({:02d}) is invalid!".format(hour))
