
# Initialization: set the secret number.
secret_number = 7

# Condition: keep asking until the correct number is guessed.
while True:
    guess = int(input("Guess the number: "))

    # Termination: exit the loop when the guess is correct.
    if guess == secret_number:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong guess. Try again.")

    # Update: the next iteration accepts another guess.
