# This program takes a two digit number as an input and then sums them together.

two_digit_number = input("Type a two digit number: ")

# Method 1
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Method 2
# print(int(two_digit_number) % 10 + int(int(two_digit_number) / 10))
