import random


again = "y"

while True:
    flip = random.randrange(2)  # 0-1

    if flip == 1:
        coin = "HEADS"
    else:
        coin = "TAILS"

    print("You flip a coin and it is... " + coin)

    again = input("Would you like to flip again (y/n)? ")
    if again == "n":
        break

# 1
# In the code

# 2
# In the code

# 3
# If I delete the again = "y" line, nothing will change because it now use while true to run once regardless of the value of again.