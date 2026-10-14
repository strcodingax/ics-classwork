import random

actual_number = random.randint(1, 100)
guess = 0
guesses = 0

print("I'm thinking of a number between 1-100.  You have 7 guesses.")

while guess != actual_number and guesses < 7:
    if guesses == 0:
        guess = int(input("First guess: "))
    else:
        guess = int(input(f"Guess # {guesses + 1}: "))
    guesses += 1

    if guess < actual_number:
        print("Sorry, you are too low.")
    elif guess > actual_number:
        print("Sorry, that guess is too high.")

if guess == actual_number:
    print("You guessed it!  What are the odds?!?")
else:
    print("Sorry, you didn't guess it in 7 tries.  You lose.")
