input_string = input("Input number words seperated by commas only: ")

number_words = input_string.split(",")

number_list = []

for i in range (0,len(number_words)):
    current_number_word = number_words[i]

    if current_number_word == "zero":
        number_list.append(0)

    elif current_number_word == "one":
        number_list.append(1)

    elif current_number_word == "two":
            number_list.append(2)        

    elif current_number_word == "three":
            number_list.append(3)

    elif current_number_word == "four":
            number_list.append(4)

    elif current_number_word == "five":
            number_list.append(5)

print(number_list)