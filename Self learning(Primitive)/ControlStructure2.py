age = int(input("ป้อนอายุของคุณ : > "))

# if   เงื่อไขเป็นจริง จะให้ทำอะไร

if age >= 15 and age <= 20:
    print(" วัย รุ่น ")
elif age >= 20 and age <= 29:
    print(" วัย หนุ่มสาว ")
elif age >= 30 and age <= 39:
    print(" วัย ผู้ใหญ่ ")
else:
    print(" วัย เด็ก ")
