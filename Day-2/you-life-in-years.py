''' 
The following program calculates how many days, weeks, and months left in your life assuming you live till the age of 90 years.
Assuming that there is 365 days in a year, 52 weeks in a year and 12 months in a year.
'''

from math import remainder


usr_age = int(input("Please enter your age: "))

remaining_age = 90 - usr_age

age_months = remaining_age * 12
age_weeks =  remaining_age * 52
age_days = remaining_age * 365

print(f"You have {age_months} months, {age_weeks} weeks, and {age_days} days remaining.")
print("So put them in a good use.")