# 1
 
def main():
    name = input("Enter your name: ")

    if name == "":
        name = "User"

    print(f"Hello, {name}!")

if __name__ == "__main__":
        main()

# 2
def greet():
     print("Welcome to the awesome area calculator!")
     print()


def main():
   
    greet()

    length = int(input("Enter a length: "))
    width = int(input("Enter a width: "))
    print()

    area = length * width

    print(f"The area is {area} units squared")

if __name__ == "__main__":
        main()

# 3
TICKET_PRICE = 13.95

def main():
      ticket_num = int(input("How many tickets would you like to buy? "))
      
      total = ticket_num * TICKET_PRICE

      print(f"The total cost is {total}.")

if __name__ == "__main__":
        main()
