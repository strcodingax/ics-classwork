# 1

numbers = []

for i in range(0,10):
    
    if i % 2 == 0:
        numbers.append(i)

print(numbers)

# 2

friends = ["Jeffery","George",]
print(friends[1])

# 3
numbers = [1, 2, 3, 4, 5]
# 1st way
print(numbers[-1])
# 2nd way
print(numbers[len(numbers)-1])

# 4
numbers = [76, 55, 34, 24]

print(numbers[1:2])

# 5 
words = ["hi","Hello","word","bonjour","guess","apple"]

print(words[-3:])

# 6
# 1
numbers = []

for i in range(0,11):
    if i % 2 == 0:
        numbers.append(i)

print(numbers)

# 2
friends = ["Frank", "Aiden", "George" ,"Jadon"]

print(friends[2])

# 3
numbers = [1,2,3,4,5]

print(numbers[-1])
print(numbers[len(numbers)-1])

# 4
numbers = [76, 55, 34, 24]

print(numbers[1:2])

# 5
words = ["Hi", "Good", "Day", "Week", "Games"]

print(numbers[len(numbers)-3:])

# 6
words = []

for i in range (0, 1000):
    word = input("Enter a word:")
    words.append(word)

print(words)

# 7 
words = []

for i in range (0, 1000):
    word = input("Enter a word for the list: ")
    words.append(word)

word_to_find = input("Enter a word to search for in the list: ")

for i in range (0,len(words)):
    word = words[i]

    if word == word_to_find:
        print(f"Found the word at index {i}.")
        break

# 8
input_string = input("Enter numbers on a single line separated by a space: ")

numbers = input_string.split()  
converted_numbers = []

for i in range(0, len(numbers)):
    current_number = numbers[i]
    converted_numbers.append(int(current_number))

# 9 
found = []

for i in range(len(numbers)):
    if numbers[i] < 0:
        found.append(i)



