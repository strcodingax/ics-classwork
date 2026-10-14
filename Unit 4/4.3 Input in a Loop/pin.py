PIN = "12345"

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

# 1
# A while loop is similar to an if statement in that it checks for a certain condition

# 2
# A while loop will continue to run as long as the condition is true. However, an if statement will only run once if the condition is true.

# 3
# If th pin were to be an integer, the input would need to be converted to an integer using int() before comparing it to the PIN, like int(input("ENTER YOUR PIN: ")).

# 4
# when we comment out the entry = input("ENTER YOUR PIN: ") line, the program will not prompt the user to enter their PIN, 
# and the while loop will not have a value to compare against the PIN. This will  variable 'entry' will be undefined, because there was no input that was given.
