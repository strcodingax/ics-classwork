name = input("Hey, what's your name? ")
age = int(input(f"Ok, {name}, how old are you? "))

if age < 16:
    print(f"You can't drive, {name}.")

elif age < 18:
    print(f"You can drive but not vote, {name}.")

elif age < 21:
    print(f"You can vote but not rent a car, {name}.")

elif age >= 21:
    print(f"You can do pretty much everything, {name}.")



