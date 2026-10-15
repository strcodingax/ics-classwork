import random

print("I'm thinking of a number from 1 to 10")
user_guess = int(input("Your guess: "))
actual_number = random.randrange(1,11) # 1- 10

if user_guess == actual_number:
    print(f"That's right! My secret number was {actual_number}!")
else:
    print(f"Sorry, but I was really thinking of {actual_number}.")