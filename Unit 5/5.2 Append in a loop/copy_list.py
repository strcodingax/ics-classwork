import random
first_list = []
second_list = []

for i in range (10):
    first_list.append(random.randint(1,100))

for n in range (len(first_list)):
    second_list.append(first_list[n])

first_list[9] = -7

print("List 1:", end = " ")
for i in range (len(first_list)):
    print(first_list[i], end = " ")

print("")

print("List 2:", end = " ")
for n in range (len(second_list)):
    print(second_list[n], end = " ")
