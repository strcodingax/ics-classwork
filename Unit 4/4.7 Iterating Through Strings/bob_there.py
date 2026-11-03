user_input = input("")
bob_there = False

first_b_position = 0
for i in range (0,len(user_input)):
    current_char = user_input[i]
    if current_char == "b" and [i + 2] == "b":
        bob_there = True
        break
    else:
        continue
print(bob_there)
