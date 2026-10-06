input_string = str(input("Please enter a word:"))

length = len(input_string)

#print(f"The word is now {input_string[-(length - 1):-1]}")
print(f"The word is now {input_string[1 : length - 1]}")