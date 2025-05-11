import random

# Select a random number between 1 and 100
print("Welcome to the Number Guessing Game!")
print("Your task is to try and guess the number I have in mind.")


def main_loop():
    print("Great! Let's start!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    while not guessed_correctly:
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("That's not a valid number. Please enter an integer.")
            continue
        if guess < number_to_guess:
            print("Too low! Try again.")
            attempts += 1
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1
        elif guess == number_to_guess:
            print(
                f"Congratulations! You've guessed the number {number_to_guess} in {attempts + 1} attempts!"
            )
            guessed_correctly = True
            print()
            ask_to_play_again()


def ask_to_play_again():
    print("Do you want to play again? (Y/N)")
    answer = input().strip().lower()
    if answer == "y":
        main_loop()
    elif answer == "n":
        print("Thanks for playing! Goodbye!")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        ask_to_play_again()


def ask_to_play():
    print("Are you ready to play? (Y/N)")
    answer = input().strip().lower()
    if answer == "y":
        main_loop()
    elif answer == "n":
        print("Okay, maybe next time!")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        ask_to_play()


ask_to_play()
