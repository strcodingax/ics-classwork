store = "No Frills"
item = "Apples"
price = 0.99
quantity = 7
subtotal = price * quantity
tax = subtotal * 0.10
total = tax + subtotal

#f-string
print(f"At {store} I bought some {item}.")
#concatenation
print("They sold for $" + str(price) + " each.")
#"dot format"
print("I wanted to purchase {} of them.".format(quantity))
#f-string
print(f"The subtotal was ${subtotal}.")
#f-string
print(f"The tax was ${round(tax, 2)}.")
#f-string
print(f"The total price, with tax included, was ${round(total, 2)}.")