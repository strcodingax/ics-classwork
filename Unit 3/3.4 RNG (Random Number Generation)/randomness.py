import random


x = random.randrange(10)  # 0-9
print(f"My random number is {x}.")

print()

print("Here are some random numbers from 1 to 5...")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6))

print()
print("Here are some random numbers from 1 to 100...")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101))

print()
print("Will these next two random number be the same?")
a = random.randrange(10)  # 0-9
b = random.randrange(10)


if a == b:
    print(f"Wow! Both numbers were {a}!")
else:
    print("The two random numbers were different. Not too surprising.")

    # 1
    # It changes the range of possible values of the random numbers from 1-5 to 1-4. As stated earlier, the new range of numbers is now 1-4. 

    # 2
    # The random numbers suddenlt became predictable, as the printed numbers are the same every time.

    # 3
    # If we change the seed, then the random numbers will be the same each time, but the actual numbers will be different. For example, with a seed of 200, the random numbers are 1,2,1,2,5,3,89,57,91,22,92,3,57,36,57,59, and 30
    # while with a seed of 100, the random numbers are 2,1,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2. The numbers are different but they are still the same each time the program is run.

    # 4
    # Games use the seed system to generate random numbers for things like loot drops, enemy behavior, and procedural generation. By using a seed, developers can ensure that the same sequence of random numbers is generated each time the game is played, 
    # which can be useful for testing and debugging. However, if the seed is not set or is changed, the random numbers will be different each time the game is played, 
    # which can add an element of unpredictability and replayability to the game.