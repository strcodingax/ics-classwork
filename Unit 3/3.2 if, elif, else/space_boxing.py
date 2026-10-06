current_weight = float(input("Please enter your current earth weight: "))

print("I have information for the following planets:")
print("   1. Venus   2. Mars   3. Jupiter")
print("   4. Saturn  5. Uranus 6. Neptune")

visiting_planet = int(input("Which planet are you visiting? "))

venus_weight = current_weight * 0.78
mars_weight = current_weight * 0.39
jupiter_weight = current_weight * 2.65
saturn_weight = current_weight * 1.17
uranus_weight = current_weight * 1.05
neptune_weight = current_weight * 1.23

if visiting_planet == 1:
    print(f"Your weight would be: {venus_weight} pounds on that planet.")
elif visiting_planet == 2:
    print(f"Your weight would be: {mars_weight} pounds on that planet.")
elif visiting_planet == 3:
    print(f"Your weight would be: {jupiter_weight} pounds on that planet.")
elif visiting_planet == 4:
    print(f"Your weight would be: {saturn_weight} pounds on that planet.")
elif visiting_planet == 5:
    print(f"Your weight would be: {uranus_weight} pounds on that planet.")
elif visiting_planet == 6:
    print(f"Your weight would be: {neptune_weight} pounds on that planet.")