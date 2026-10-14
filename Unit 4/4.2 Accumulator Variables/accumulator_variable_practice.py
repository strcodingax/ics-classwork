# 1
n = 0
total = 0

while n <= 10:
    total += n
    n += 1

print(total)

# 2
n = 100
total = 0
while n <= 200:
    total += n
    n += 1

print (total)

# 3 

n = 100
total = 0
while n <= 200:
    total += n
    n += 1

m = 200
total_2 = 0
while m <= 300:
    total_2 += m
    m += 1

total_difference = total - total_2

print (total_difference)

# 4

n = 1000
total = 0
while n <= 10000:
    total += n
    n += 5

print(total)

# 5 
n = 0
total = 0
while n <= 100:
    if n % 5 == 0 and n % 3 != 0:
        total += n
    n +=5
print(total)


