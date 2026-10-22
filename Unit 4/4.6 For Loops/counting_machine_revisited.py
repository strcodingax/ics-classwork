count_start = int(input("Count from: "))
count_end = int(input("Count to: "))
count_step = int(input("Count by: "))


for n in range (count_start, count_end + 1, count_step):
    print(n , end = " ")