input_message_1 = input("")
input_message_2 = input("")

end_other = False

str1_low = input_message_1.lower()
str2_low = input_message_2.lower()

len1 = len(str1_low)
len2 = len(str2_low)

if str1_low[-len2:] == str2_low:
    end_other = True
elif str2_low[-len1:] == str1_low:
    end_other = True
else:
    end_other = False

print(end_other)