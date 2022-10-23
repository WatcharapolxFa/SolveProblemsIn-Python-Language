def take_out(p1,p2):
    temp_p1 = dict(p1)
    for k in p2:
        if k in temp_p1:
            if temp_p1[k] >= p2[k]:
                temp_p1[k] = temp_p1[k] - p2[k]
    return temp_p1

p1 = {100:1 , 20:2 , 5:1}
p2 = {20:1 , 10:2 , 5:1}
p1 = take_out(p1,p2)
print(p1)