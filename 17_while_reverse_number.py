
number = int(input("Enter a number: "))

# Store the sign of the original number.
sign = -1 if number < 0 else 1

# Work with the absolute value.
number = abs(number)

# Initialization: start the reversed number at 0.
reverse = 0

# Condition: continue while there are digits left.
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit

    # Update: remove the last digit.
    number = number // 10

# Restore the original sign.
reverse = reverse * sign

print("Reversed number:", reverse)
