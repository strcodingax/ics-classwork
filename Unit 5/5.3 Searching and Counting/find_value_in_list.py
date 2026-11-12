import random
list =  []

for i in range(0,10):
    list.append(random.randint(1,50))

print(f"List: {list}")

value_to_find = int(input("Value to find: "))

print("")

for i in range (0,len(list)):
    current_char = list[i]
    if current_char == value_to_find:
        print(f"{value_to_find} is in the list.")
        break
     