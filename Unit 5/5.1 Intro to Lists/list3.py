import random
list = []
n = 0
for i in range (1000):
    n = random.randint(10,99)
    list.append(n)

for i in range (len(list)):
    print(list[i] , end = "  ")


