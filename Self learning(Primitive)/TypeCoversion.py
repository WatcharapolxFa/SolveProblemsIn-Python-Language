fa = 110445
fah = 11.04
tuk = "260114"

print(type(fa))  # integer
print(type(fah))  # float
print(type(tuk))  # string

# บวกเลข

result = fa+fah
print(result)

# แปลง string => integer

result = fa+int(tuk)  # นำ int(ตัวที่ต้องการแปลง)
print(result)

# แปลง  integer => string

result = str(fa)+tuk  # นำ str(ตัวที่ต้องการแปลง)
print(result)

# แปลง float => string
result = str(fah)+tuk  # นำ str(ตัวที่ต้องการแปลง)
print(result)


# แปลง string => float
result = fah+float(tuk)  # นำ float(ตัวที่ต้องการแปลง)
print(result)

# แปลง float => integer
result = int(fah)+fa    # นำ int(ตัวที่ต้องการแปลง)
print(result)

# แปลง  integer => float
result = fah+float(fa)    # นำ float(ตัวที่ต้องการแปลง)
print(result)

# แปลง แบบตลอดไป
"""
z="20" z เป็น str
z= float(z)  z เป็น float
"""
