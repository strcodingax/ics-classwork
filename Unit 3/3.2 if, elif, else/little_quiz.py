input("Are you ready for a quiz? ")
print("Okay, here it comes!")

wrong = 0

print("\nQ1) What is the capital of Alaska?")
print("    1) Melbourne")
print("    2) Anchorage")
print("    3) Juneau")

if input("\n> ") == "3":
    print("\nThat's right!")
else:
    print("\nSorry, the capital of Alaska is Juneau.")
    wrong += 1

print("\n Q2) Is keyboard_input the Python function for getting keyboard input?")
print("    1) true")
print("    2) false")

if input("\n> ") == "2":
    print("\nThat's right!")
else:
    print('\nSorry, in Python, you would use the "input" function to get keyboard input.')
    wrong += 1

print("\n Q3) What is the result of 9 + 6 / 3?")
print("    1) 5")
print("    2) 11")
print("    3) 15/3")    

if input("\n> ") == "2":
    print("\nThat's right!")
else:
    print("\nSorry, the answer is 11.")
    wrong += 1

print(f"\nOverall, you got {3 - wrong} out of 3 correct.")
print("Thanks for playing!")