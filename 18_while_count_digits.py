
number = int(input("Enter a number: "))

# Work with the absolute value.
number = abs(number)

# Handle 0 separately because it has one digit.
if number == 0:
    count = 1
else:
    # Initialization: start the digit count at 0.
    count = 0

    # Condition: continue while there are digits left.
    while number > 0:
        count = count + 1

        # Update: remove the last digit.
        number = number // 10

print("Number of digits:", count)
