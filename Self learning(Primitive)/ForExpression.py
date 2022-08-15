
def forloop():
    summation = 0
# 0 1 2 (start เริ่มนับที่รอบ, stop คือมันจะลบ 1  ,step นับเพิ่มที่ละเท่าไหร่)
    for i in range(4):
        summation += i
        print("รอบที่ >> ", i, "ผลรวมของ I == ",
              summation, "ค่าเฉลี่ย == ", summation/i)


def loop_string():

    s = "over the raimbow"
    for c in s:  # ใช้ for เข้าถึงค่าข้อมูลใน String
        print(c)


loop_string()
