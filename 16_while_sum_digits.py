
number = int(input("Enter a number: "))

# Convert the number to a positive value.
number = abs(number)

# Initialization: start the sum at 0.
total = 0

# Condition: continue while there are digits left.
while number > 0:
    digit = number % 10
    total = total + digit

    # Update: remove the last digit.
    number = number // 10

print("Sum of digits:", total)
