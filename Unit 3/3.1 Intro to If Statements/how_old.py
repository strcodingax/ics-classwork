name = input("Hey, what's your name? ")
age = int(input(f"Ok, {name}, how old are you? "))

if age < 16:
    print(f"You can't drive, {name}.")

if age < 18:
    print(f"You can't vote, {name}.")

if age < 21:
    print(f"You can't rent a car, {name}.")

if age >= 21:
    print(f"You can do anything that's legal, {name}.")



