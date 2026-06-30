weight =float(input("ENTER YOUR WEIGHT: "))
height = float(input("ENTER YOUR HEIGHT: "))

BMI = round(weight / (height**2), 2)

if(BMI<18.5):
    print("YOUR BMI IS", BMI, "AND YOU ARE UNDERWEIGHT")
elif(BMI>=18.5 and BMI<25):
    print("YOUR BMI IS", BMI, "AND YOU ARE NORMAL")
else:
    print("YOUR BMI IS", BMI, "AND YOU ARE OVERWEIGHT")
