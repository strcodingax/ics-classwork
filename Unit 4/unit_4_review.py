# 1
i = 55
while i < 100:
    print(i)
    i +=2

for n in range (55,100,2):
    print(n)

# 2
total = 0
for i in range (0,100,1):
    user_number = int(input("Input a number: "))
    total += user_number

average = total / 100

print(average)

# 3
print("Welcome the the Genetic Editing System (GES)\nPlease use irresponsibly.\n")

genetic_sequence = input("Enter genetic sequence (letters a-g only): ")
edited_sequence = ""

print("Editing sequence...\n... done!\n")

length = len(genetic_sequence)

changes_made = 0

for i in range (0,length,1):
    current_char = genetic_sequence[i]

    if current_char == "c":
        edited_sequence += "f"
        changes_made += 1

    if current_char == "b":
        edited_sequence += "ag"
        changes_made += 1

    else:
        edited_sequence += current_char

print(f"The edited sequence is: {edited_sequence}")
print(f"There were {changes_made} modifications.")