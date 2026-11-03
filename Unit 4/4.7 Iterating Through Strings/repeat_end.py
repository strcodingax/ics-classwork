user_input = input("")
end = int(input(""))

ouput_string = ""
string_end = ""

for i in range (0,end):
    string_end = user_input[len(user_input) - end:]
    ouput_string += string_end

print(ouput_string)