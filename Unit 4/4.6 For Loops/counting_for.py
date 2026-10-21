print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(2, 22, 2):
    print(f"{n}. {message}")    

# 1
# It would not change anything, because it uses n (or whatever) to essentially keep count of how many times it has run, so the name does not matter
# really. I think you chose n because it's a simple name, which makes it easy to keep track of it.

# 2
# I think that the first value is where it starts, like if it is 1, then it starts at 1. The second value is where it ends, but
# it is one less than what you put in. For example, if you put 6, it ends at 5.

# 3 
# I think it's how it increments n, or whatever name you want to call it. For example, if it's 2, then it will go from 0 to 2 to 4, and so on.

# 4
# If you call a range function with only one number, it starts from zero and counts by one until it ends up 1 step before the number

# 5 
# If you call a range function with two numbers, then it starts at the first value, and then counts up to one before the second value

# 6
# print("Type in a message, and I'll display it five times.")

# message = input("Message: ")

# for n in range(1, 11, 1):
#    print(f"{n}. {message}")    

# 7 
# In the code 