weight = float(input("Enter your weight in kg: "))  
height = float(input("Enter your height in cm: ")) 

height = height / 100 

bmi = weight / (height ** 2)  

if bmi <= 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi}. Normal weight.")
elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi}. Slightly overweight.")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi}. Obese.")
else:
    print(f"Your BMI is {bmi}. Clinically obese.")