# 1
animal_names = input("Enter animal names seperated by spaces: ")

animals = animal_names.split(" ")

for i in range (0,len(animals)):
    print(animals[i])

# 2
number_string = input("Enter numbers names seperated by spaces: ")

numbers = [int(item) for item in number_string.split(" ")]

for i in range (0,len(numbers)):
    print(f"{i}: {numbers[i]}")

# 3
number_word_string = input("Enter number words seperated by spaces: ")

number_words = number_word_string.split(",")
real_number_list = []

for i in range (0,len(number_words)):
    current_word = number_words[i]

    if current_word == "one":
        real_number_list.append(1)

    elif current_word == "two":
        real_number_list.append(2)
        
    elif current_word == "three":
        real_number_list.append(3)

    elif current_word == "four":
        real_number_list.append(4)

    elif current_word == "five":
        real_number_list.append(5)

print(real_number_list)

# 4
outcome_string = input("Enter your match outcomes seperated by spaces: ")

outcomes = outcome_string.split(" ")
points_list = []

for i in range (0,len(outcomes)):
    current_outcome = outcomes[i]

    if current_outcome == "W":
        points_list.append(2)

    elif current_outcome == "L":
        points_list.append(0)
        
    elif current_outcome == "T":
        points_list.append(1)

print(points_list)

# 5 

input_coords = input("Enter x-coordinates: ")

pairs = input_coords.split(",")

x_positions = []
for pair in range(0, len(pairs)):
    value = pair.split(":")[1]
    
    x_positions.append(int(value))

print(x_positions)

# 6

input_str = input("Enter coordinates: ")

point_strings = input_str.split(" - ")
points = []

for i in range(0, len(point_strings)):
    point_str = point_strings[i]
    
    x_part, y_part = point_str.split(",")
    
    x_val = int(x_part.split(":")[1])
    y_val = int(y_part.split(":")[1])
    
    points.append([x_val, y_val])

print(points)


