import random
list =  []

for i in range(0,10):
    list.append(random.randint(1,50))

print(f"List: {list}")

value_to_find = int(input("Value to find: "))
is_there = False

print("")

for i in range (0,len(list)):
    current_char = list[i]
    if current_char == value_to_find:
        is_there = True
        break
     
if is_there == True:
    print(f"{value_to_find} is in the list.")
elif is_there == False:
    print(f"{value_to_find} is not in the list.")