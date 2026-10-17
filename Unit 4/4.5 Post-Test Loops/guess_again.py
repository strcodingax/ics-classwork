import random

print("I'm thinking of a number from 1 to 10")
user_guess = int(input("Your guess: "))
actual_number = random.randrange(1,11) # 1- 10
attempts = 0

while True:
    attempts += 1
    if user_guess == actual_number:
        break
    print("That is incorrect. Guess again.")
    user_guess = int(input("Your guess: "))
    
print("That's right! You're a good guesser.")
print(f"It only took you {attempts} tries.")