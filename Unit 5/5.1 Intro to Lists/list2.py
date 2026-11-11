import random
list = []
n = 0
for i in range (10):
    n = random.randint(1,100)
    list.append(n)

for i in range (len(list)):
    print(f"Slot {i} contains a {list[i]}")


