import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 30)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess (between 1 and 30): "))
            attempts += 1

            if guess < secret_number:
                print("Too low. Try again.")
            elif guess > secret_number:
                print("Too high. Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game
number_guessing_game()
