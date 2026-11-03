user_first_string = input("")
user_second_string = input("")

output_string = ""

longer_string = user_first_string

if user_first_string < user_second_string:
    longer_string = user_second_string

for i in range(0,len(longer_string)):
    if i < len(user_first_string):
        output_string += user_first_string[i]
    if i < len(user_second_string):
          output_string += user_second_string[i]

print(output_string)
