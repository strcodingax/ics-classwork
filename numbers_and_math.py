print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
# This prints the difference of 33 and 11, which is 22. THis is the number of boys
print(f"there are {(33 - 11)} boys.")
print()
# This prints the quotient of 11/33, which is 0.33333333333333333%. This is the percentage of girls in the class
print(f"That means {round((11 / 33) * 100 , 2)} % are girls...")
# This prints the percentage of the boys in the class, 
# which was found by first subtracting 11 (the number of girls) from 33 (the total number of people), 
# and then dividing by the total number of people to get the percentage of boys in the class.
print(f"and {(round(((33 - 11) / 33) * 100, 2))} % are boys.")
print()
print("If we made groups of six...")
# This uses floor division to divide and then remove everything behind the whole number (truncate) to get
# and find the number of groups of 6, being 5. This line then prints it out.
print(f"There would be {33 // 6} groups of six.")
# This prints the number of people in the remainder/small group, 
# which is found by using 33 % (modulus) 6,as 33 cannot divide evenly into 6 without decimals,
# which returns the remainder of 3. 
print(f"And then a smaller group of {33 % 6} people.")
# This prints "-" 30 times to make a line
print("-" * 30)
print("If we had 17 apples and 3 people...")
# This line prints the amount of apples that each person gets by using floor division of 17, which is 5
print(f"Each person would get {17 // 3} whole apples.")
# This line uses modulus to find the remainder of the floor division after it happened on the line above to 
# see how many apples would be left, which would be 2. The line then prints the result out.
print(f"There would be {(17 % 3)} apples remaining.")
print()
print("If we charged each person $2 each for their 5 apples..")
# This prints out how much money each person would pay for their 
# 5 apples by multiplying 5 by 2 (the cost of each apple) and printing the result
print(f"they would each pay ${(2 * 5)}")
