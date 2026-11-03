user_input = input("")
xyz_there = False

for i in range (0 , len(user_input)):
    current_chars = user_input[i : i+3]
    if current_chars == "xyz":
        if user_input[i-1] == ".":
            continue
        else:
            xyz_there = True
            break

print(xyz_there)