# Chapter : 15 - item : 2 - Exam_3_2_2a จงเขียนโปรแกรมแบบ Recursive เพื่อหาค่า Min
def Min(newlst, j, min):
    value = int(newlst[j])
    if(value <= min):
        min = value
    j += 1
    if(j == len(newlst)):
        print("Min : " + str(min))
    if(j < len(newlst)):
        Min(newlst, j, min)


newlst = [e for e in input("Enter Input : ").split(" ")]
Min(newlst, 0, +99999)
