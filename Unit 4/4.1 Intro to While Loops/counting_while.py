print("Type in a message, and I'll display it several times.")

message = input("Message: ")
print()

how_many_times = int(input("How many times? "))
n = 0
while n < how_many_times:
    print(f"{n * 10 + 10}. {message}")
    n += 1

    # 1
    # It increments n by 1 every time it prints the message so when it eventually hits 5, it will stop as the loop's condition
    # is no longer true. By removing it 

    # 2 
    # message = input("Message: ")
    # print()

    # n = 0
    # while n < 10:
    #   print(f"{n + 1}. {message}")
    #   n += 1

    # 3 
    #message = input("Message: ")
    #print()

    # n = 10
    # while n < 110:
    #   print(f"{n}. {message}")
    #   n += 10
  
