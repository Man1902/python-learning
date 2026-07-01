import random

print(36*"*")
print("Welcome to the Number Guessing Game!")
print(36*"*")

print("\nI am thinking of a number between 1 and 100.\n")
choosen_number = random.randint(1, 100)

diffculty_level = input("Choose a difficulty level: Type 'easy' or 'hard': ")
no_of_attempts = 10
if diffculty_level == "hard":
    no_of_attempts = 5

is_won = False
print(f"You have {no_of_attempts} attempts to Guess!")
while no_of_attempts > 0:
    guess = int(input("\nMake a guess: "))

    if guess == choosen_number:
        print("You guessed the number correctly.  You win!")
        is_won = True
        break
    else:
        if guess < choosen_number:
            print("Your guess is too low. Guess again")
        else:
            print("Your guess is too high. Guess again")

    no_of_attempts -= 1
    print(f"You have {no_of_attempts} attempts left to Guess.!")

if not is_won:
    print("You've run out of guesses, \nGame Over!")