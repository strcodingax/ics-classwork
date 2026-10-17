import math
print("SQUARE ROOT!")
user_input = int(input("Enter a number: "))

while True:
    if user_input < 0:
        print("You can't take a square root of a negative number.")
        user_input = int(input("Try again: "))
    else:
        break

square_root = math.sqrt(user_input)
print(f"The square root of {user_input} is {square_root}.")
