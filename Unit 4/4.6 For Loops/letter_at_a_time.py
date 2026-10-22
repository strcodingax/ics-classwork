message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")

a_count = 0
for i in range(len(message)):
    letter = message[i].lower()
    if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E'or letter == 'i' or letter == 'I' or letter == 'o' or letter == 'O' or letter == 'u' or letter == 'U':
        a_count += 1

print(f"\nYour message contains the letter 'a' {a_count} times.")

# 1
# It just prints range(0,7), which is the range itself, but if you make it a list, you get the integers covered by range 7, that being 0-6, leaving out 7 because it's non-inclusive.

# 2
# The number that is sent to the range function is 5, and the numbers that would be included are [0 ,1, 2, 3, 4].

# 3
# Their length is 3, and the last character's index would be 2, because it starts at 0, not 1. So the last character is 1 - the length of the string, which is 3, resulting in 2.

# 4
# in the code
