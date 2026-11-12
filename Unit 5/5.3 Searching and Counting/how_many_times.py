import random
list =  []

for i in range(0,10):
    list.append(random.randint(1,50))

print(f"List: {list}")

value_to_find = int(input("Value to find: "))

how_many_times = 0

for i in range (0,len(list)):
    current_char = list[i]
    if current_char == value_to_find:
      how_many_times += 1

print(f"{value_to_find} was found {how_many_times} times.")