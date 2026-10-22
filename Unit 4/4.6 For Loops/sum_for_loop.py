number = int(input("Number: "))

total = 0

print("")

for n in range (1 , number + 1 , 1):
    print (n , end = " ")
    total += n

print("")

print(f"The sum is {total}.")