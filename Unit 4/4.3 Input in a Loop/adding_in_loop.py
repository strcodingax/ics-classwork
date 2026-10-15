print("I will add up the numbers you give me.")
total = 0

input_number = int(input("Number: "))
total += input_number
print(f"The total so far is {total}")

while input_number !=0:
    input_number = int(input("Number: "))
    total += input_number
    print(f"The total so far is {total}")

print(f"\nThe total is {total}.")
