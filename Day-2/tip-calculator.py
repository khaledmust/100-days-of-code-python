# This program calculates how much each person should pay given a certain tip percentage.

print("Welcome to the tip calculator.")

total_bill = float(input("What the total bill? $"))
tip_percentage = int(input("What percentage would you like to give? 10%, 12%, 15% " ))
num_person = int(input("How many people to split the bill? "))

tip_value = total_bill * tip_percentage / 100
total_bill_with_tip = total_bill + tip_value

amount_per_person = round(total_bill_with_tip / num_person, 2)

print(f"Every person should pay ${amount_per_person}.")

