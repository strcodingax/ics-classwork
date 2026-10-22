x = 0
y = 0
print("x \t y")
print("-" * 18)

for n in range(-20 , 21, 1 ):
    halve_step = 0
    x = 0
    y = 0

    halve_step = n/2

    x = x + halve_step
    y = x ** 2

    print(f"{x} \t {y}")

