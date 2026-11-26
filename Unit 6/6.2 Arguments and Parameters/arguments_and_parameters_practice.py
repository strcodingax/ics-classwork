import math

# 1
# a) 
# There are two arguments to be sent to the num_chairs function, that being 4, and 5

# b)
# The names of the parameter variables are tables, and chairs_per_table. Tables is assigned the value 4, and the num_chairs function is 
# assigned the value 5.

# c)
# The output will be "You will need 20 chairs."

# d)
# When you remove an arguement, you don't have enough to run the function, as there are two parameter variables, those being
# tables, and chairs_per_table. Without one, it cannot calculate the amount of chair needed, so they send you an error. If you add
# a argument, then the program does not know what to do with the extra argument, so it gives you an error.

# 2
def print_integer(number):
    print(number)

print_integer(5)

# 3
def subtract(first_int,second_int):
    print(math.abs(first_int - second_int))

# 4
# Firstly, there is only one parameter, which is a, meaning that only a will get a value and not b, and also it should be def, not function.

# 5
# activate_thrusters("5%")
# activate_thrusters(5)

# 6
# There are no arguments at all, and there should be two there for the two parameters, those being the person's name, and 
# the amount of apples the person will eat. A correct version would probably look like this:
# person_apples("John,3")