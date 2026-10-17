print("Enter three integers:")
side1 = int(input("Side 1: "))
side2 = int(input("Side 2: "))

while side2 < side1:
    print(f"{side2} is smaller than {side1}.  Try again.")
    side2 = int(input("Side 2: "))

side3 = int(input("Side 3: "))

while side3 < side2:
    print(f"{side3} is smaller than {side2}.  Try again.")
    side3 = int(input("Side 3: "))

print(f"\nYour three sides are {side1} {side2} {side3}")

if side1 > 0 and side1**2 + side2**2 == side3**2:
    print("These sides *do* make a right triangle.  Yippy-skippy!")
else:
    print("NO!  These sides do not make a right triangle!")