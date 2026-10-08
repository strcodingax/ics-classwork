name = input("Your name: ")
age = int(input("Your age: "))

if age < 16:
    print(f"You can't drive, {name}.")

if 16 <= age <= 17:
    print(f"You can drive but not vote, {name}.")

if 18 <= age <= 24:
    print(f"You can vote but not rent a car, {name}.")

if age >= 25:
    print(f"You can do pretty much everything, {name}.")



