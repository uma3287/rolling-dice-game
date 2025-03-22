import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    guessed = False

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess}.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")

number_guessing_game()
