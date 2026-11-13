import random
list =  []

for i in range(0,10):
    list.append(random.randint(1,50))

largest_value = list[0]
index_location = 0

for n in range(0,len(list)):
    if list[n] > largest_value:
        largest_value = list[n]
        index_location = n
    

print(f"List: {list}\n")
print(f"The largest value is {largest_value}")
print(f"It is at index {index_location}")