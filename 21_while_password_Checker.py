
# Initialization: store the correct password.
correct_password = "python123"

# Condition: keep asking until the correct password is entered.
while True:
    password = input("Enter password: ")

    # Termination: exit the loop when the password is correct.
    if password == correct_password:
        print("Correct password!")
        break
    else:
        print("Incorrect password. Try again.")

    # Update: the next iteration asks the user for a new password.
