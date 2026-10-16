import time


swimmer1 = "GALLANT"
swimmer2 = "GOOFUS "

minimum_temperature = 79.0  # degrees Fahrenheit
current_temperature = 0.0
saved_temperature = 0.0
swim_time = 0

current_temperature = float(input("What is the current water temperature? "))
saved_temperature = current_temperature  # saves a copy of this value so we can get it back later.

print(f"\nOkay, so the current water temperature is {current_temperature} F.")
print(f"{swimmer1} approaches the lake....")

swim_time = 0
while current_temperature >= minimum_temperature:
    print(f"\t{swimmer1} swims for a bit.", end="")
    swim_time += 1
    print(f" Swim time: {swim_time} min.")
    time.sleep(0.6)  # pauses for 600 milliseconds
    current_temperature -= 0.5  # subtracts 1/2 a degree from the water temperature
    print(f"\tThe current water temperature is now {current_temperature} F.")


print(f"{swimmer1} stops swimming. Total swim time: {swim_time} min.")

current_temperature = saved_temperature  # restores original water temperature

print(f"\nOkay, so the current water temperature is {current_temperature} F.")
print(f"{swimmer2} approaches the lake....")

swim_time = 0
while True:
    print("\t" + swimmer2 + " swims for a bit.", end="")
    swim_time += 1
    print(f" Swim time: {swim_time} min.")
    time.sleep(0.6)
    current_temperature -= 0.5
    print(f"\tThe current water temperature is now {current_temperature} F.")
    
    if current_temperature < minimum_temperature:
        break

print(f"{swimmer2} stops swimming. Total swim time: {swim_time} min.")

# 1
# They do swim for the same amount of time when the water tempature is 80.5, as they both swim for 4 minutes.

# 2
# When the water tempature is 78, Gallant doesn't even swim at all, while Goofus swims for only a single minute

# 3
# I think that Gallant actually checks the water first before he dives in.

# 4
# Goofus just dives in and asks questions later.

# 5
# The first while loop use a simple loop with a condition, but the second one uses a while true loop to constantly run the loop and uses the
# if condition with a break at the very end to stop the loop.

# 6
# The first loop is the pre-test loop because it checks for the condition first before running the loop, while the second on is the
# post-test loop because it use while true to make sure it runs at least once. This is also why Goofus swims for at least one minute.