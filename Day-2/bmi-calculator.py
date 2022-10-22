# A simple BMI calculator.

usr_weight = float(input("Please enter your weight in Kg: " ))
usr_height = float(input("Please enter your height in m: "))

bmi = usr_weight / usr_height ** 2

print("Your BMI is ." + str(int(bmi)))