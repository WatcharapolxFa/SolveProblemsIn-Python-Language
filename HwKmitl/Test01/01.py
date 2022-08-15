print(" *** BMI *** ")
wei, hig = input("Enter your weight(kg) and height(m) : ").split()
weight = int(wei)
hight = float(hig)

sum = weight/(hight*hight)

if sum > 0 and sum < 18.5:
    result = "Below normal weight."
elif sum >= 18.5 and sum < 25:
    result = "Normal weight."
elif sum >= 25 and sum < 30:
    result = "Overweight."
elif sum >= 30 and sum < 35:
    result = "Case I Obesity."
elif sum >= 35 and sum < 40:
    result = "Case II Obesity."
else:
    result = "Case III Obesity."
print("Your status is :", result)
