print("*** Election ***")
number = int(input("Enter a number of voter(s) : "))
scores = input().split()
members = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0,
           '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0}
for score in scores:
    if score in members:
        members[score] += 1
rev_dict = {}  # สร้าง dict ว่าง
for key, value in members.items():
    rev_dict.setdefault(value, set()).add(key)
    result = [key for key, value in rev_dict.items()if len(value) > 1]
if len(result) == 1:
    print("*** No Candidate Wins ***")
    exit()
if members[max(members, key=members.get)] in result:
    print("*** No Candidate Wins ***")
    exit()
print("{}".format(max(members, key=members.get)))
exit()
