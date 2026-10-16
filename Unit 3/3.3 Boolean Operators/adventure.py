print("WELCOME TO AIDEN'S TINY ADVENTURE!")

print('You are in a creepy house! would you like to go "upstairs" or into the "kitchen"?')
decision_1 = input("> ")
if decision_1 == "upstairs":
    print("You go upstairs and see a hallway. At the end of the hallway is a \"bedroom\". There is also a \"bathroom\" off the hallway.\nWhere would you like to go?")
    decision_2 = input("> ")

    if decision_2 == "bedroom":
        print("You are in a plush bedroom, with expensive-looking hardwood furniture.  The bed is unmade.  \nIn the back of the room, the closet door is ajar.  Would you like to open the door? (\"yes\" or \"no\")")
        decision_4 = input("> ")

        if decision_4 == "yes":
            print("You find a collection of old dolls, close the closet, and leave the house with a story to tell.")

        elif decision_4 == "no":
            print("You leave the closet closed, settle into the bed, and drift off to sleep.")

    elif decision_2 == "bathroom":
        print("You enter the bathroom and spot a candle burning beside the sink. Would you like to blow it out? (\"yes\" or \"no\")")
        decision_5 = input("> ")

        if decision_5 == "yes":
            print("You blow out the candle and leave the quiet house.")

        elif decision_5 == "no":
            print("You leave the candle glowing and head home, glad to be out of the strange house.")
        
elif decision_1 == "kitchen":
    print("There is a long countertop with dirty dishes everywhere.  Off to one side there is, as you'd expect, a refrigerator. You may open the \"refrigerator\" or look in a \"cabinet\".")
    decision_3 = input("> ")

    if decision_3 == "refrigerator":
        print("Inside the refrigerator you see food and stuff.  It looks pretty nasty. Would you like to eat some of the food? (\"yes\" or \"no\")")
        decision_6 = input("> ")

        if decision_6 == "yes":
            print("You try a bite, realize the food has gone bad, and leave the house to find something fresh.")

        elif decision_6 == "no":
            print("You skip the food, tidy the kitchen, and head home as evening falls.")

    elif decision_3 == "cabinet":
        print("You opened the cabinet and found some snacks. They seem pretty old, but edible. Do you want to eat the food? (\"yes\" or \"no\")")
        decision_7 = input("> ")

        if decision_7 == "yes":
            print("You try a snack, decide it isn't for you, and leave the house.")

        elif decision_7 == "no":
            print("You leave the snacks alone, tidy the kitchen, and head home feeling satisfied.")
