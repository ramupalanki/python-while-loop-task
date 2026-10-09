
# Initialization: start the total at 0.
total = 0

# Condition: continue asking for numbers until 0 is entered.
while True:
    number = int(input("Enter a number (0 to stop): "))

    # Termination: stop the loop when the user enters 0.
    if number == 0:
        break

    # Update: add the entered number to the running total.
    total = total + number

print("Sum:", total)
