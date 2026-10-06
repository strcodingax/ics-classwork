height_feet = float(input("Height (feet only): "))
height_inches = float(input("Height (inches): "))
weight_in_pounds = float(input("Weight in pounds: "))

height_in_meters = (height_feet * 0.3048) + (height_inches * 0.0254)
weight_in_kilograms = weight_in_pounds * 0.453592

print("")

bmi = weight_in_kilograms / (height_in_meters ** 2)

print(f"Your BMI is {bmi}")