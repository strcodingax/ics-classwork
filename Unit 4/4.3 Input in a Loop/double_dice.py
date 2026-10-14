import random

print("HERE COMES THE DICE!\n")

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

while dice1 != dice2:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print(f"Roll #1: {dice1}")
    print(f"Roll #2: {dice2}")

    total = dice1 + dice2
    print(f"The total is {total}!")

print(f"Roll #1: {dice1}")
print(f"Roll #2: {dice2}")
    
total = dice1 + dice2
print(f"The total is {total}!")
