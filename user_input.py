print("Enter the following information about an item you wish to purchase..")
print()

name = str(input("The name of the item: "))

price = float(input("The price: $"))

quantity = int(input(("How many do you want? ")))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")

# 1
# We took the price by printing a line asking about the price and then waited for the input in the same line, 
# while the name was found by asking for the item's name before going down a line before waiting for the input.
# When we get the name, we simply store it directly as a string, while price stores it specifically as a float 
# because there can be decimals.

# 2
# Is in the code

# 3
# A prompt is a command that essentially asks the user to provide data, which in this case is to type something. 
#If you were to switch the order, you would cause a useability issue as whoever is looking at the code will be confused,
# because you asked for the input before you even asked what you wanted them to type in.

# 4
# The int() and float() functions are used for the quantity and the price because the input() function stores your result as a string
# by default, so by using int() for quantity and float() for price, we can store numerical values and also decimals instead of strings.
