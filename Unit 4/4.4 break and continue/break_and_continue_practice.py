# 1
n = -1

while n < 10:
    n += 1
    if n == 7:
        continue
    print(n)

# 2 
n = 4
total = 0

while n <= 20:
    n += 1
    if n % 3 == 0:
        continue
    total += n
    print(total)

# 3
start_number =int(input("starting number: "))
end_number = int(input("ending number: "))
n = start_number - 1
total = 0

while n <= end_number:
    n += 1
    if n == 13 or n == 31:
        total += n
        print (f"The total is {total}")
        break
    total += n
   
# 4 
while True:
   user_word = input("Type a word: ")
   if user_word == "stop":
       print("Goodbye!")
       break
   print(f"Your word: {user_word}") 