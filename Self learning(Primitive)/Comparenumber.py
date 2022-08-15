# เขียนโปรแกรมหาตัวเลข มาก / น้อย

number1 = int(input("ป้อนตัวเลขตัวแรก >> "))
number2 = int(input("ป้อนตัวเลขตัวที่สอง >> "))
# วิธีแปลงค่าเป็น string
print(str(number1)+"มากกว่า"+str(number1)
      ) if number1 > number2 else print(str(number1)+"น้อยกว่า"+str(number2))
# อีกวิธีโดยไม่แปลงค่าเป็น string
print(str(number1)+"มากกว่า"+str(number1)
      ) if number1 > number2 else print(str(number1)+"น้อยกว่า"+str(number2))
