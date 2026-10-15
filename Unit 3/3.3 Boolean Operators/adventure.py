print("WELCOME TO MITCHELL'S TINY ADVENTURE!")

print('You are in a creepy house! would you like to go "upstairs" or into the "kitchen"?')
decision_1 = input("> ")
if decision_1 == "upstairs":
    print("You go upstairs and see a hallway. At the end of the hallway is a \"bedroom\". There is also a \"bathroom\" off the hallway.\nWhere would you like to go?")
    decision_2 = input("> ")

    if decision_2 == "bedroom":
        print("You are in a plush bedroom, with expensive-looking hardwood furniture.  The bed is unmade.  \nIn the back of the room, the closet door is ajar.  Would you like to open the door? (\"yes\" or \"no\")")
        decision_4 = input("> ")

        if decision_4 == "yes":
            print("You open the door to see multiple dolls and plushies.")

        elif decision_4 == "no":
            print("You decide not to open the door, and instead opt to take a nap in the bed.")

    elif decision_2 == "bathroom":
        print("You have now entered the bathroom, around the corner you see a glimmer of orange light. You turn the corner and see a golden throne. Do you want to use the golden toilet? (\"yes\" or \"no\")")
        decision_5 = input("> ")

        if decision_5 == "yes":
            print("You sit on the golden toilet. Nothing special happens as you realize that all of this was just a waste of time.")

        elif decision_5 == "no":
            print("You decided not to sit on the toilet, so you just linger around in the bathroom forever and ever.")
        
elif decision_1 == "kitchen":
    print("There is a long countertop with dirty dishes everywhere.  Off to one side there is, as you'd expect, a refrigerator. You may open the \"refrigerator\" or look in a \"cabinet\".")
    decision_3 = input("> ")

    if decision_3 == "refrigerator":
        print("Inside the refrigerator you see food and stuff.  It looks pretty nasty. Would you like to eat some of the food? (\"yes\" or \"no\"")
        decision_6 = input("> ")

        if decision_6 == "yes":
            print("You eat the food, and get serious food posioning, and you then spend a very long time in the bathroom/")

    elif decision_3 == "cabinet":
        print("You opened the cabinet and found some snacks. They seem pretty old, but edible. Do you wnat to eat the food (\"yes\" or \"no\")?")
        decision_6 = input("> ")
