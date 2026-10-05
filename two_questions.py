print("TWO QUESTIONS!")
print("Think of an object, and I'll try to guess it.")

is_animal = False
is_vegetable = False
is_mineral = False

bigger_than_breadbox = False

print("\nQuestion 1) Is it a animal, vegetable, or mineral?")
question_1_answer = input("> ")

if question_1_answer == "animal":
    is_animal = True
elif question_1_answer == "vegetable":
    is_vegetable = True
elif question_1_answer == "mineral":
    is_mineral = True

print("\nQuestion 2) Is it bigger than a breadbox?")
question_2_answer = input("> ")

if question_2_answer == "yes":
    bigger_than_breadbox = True
elif question_2_answer == "no":
    bigger_than_breadbox = False

if is_animal == True and bigger_than_breadbox == False:
    print("My guess is that you are thinking of a squirrel.")
elif is_animal and bigger_than_breadbox == True:
    print("My guess is that you are thinking of a moose.")

if is_vegetable == True and bigger_than_breadbox == False:
    print("My guess is that you are thinking of a carrot.")
elif is_vegetable and bigger_than_breadbox == True:
    print("My guess is that you are thinking of a watermelon.")

if is_mineral == True and bigger_than_breadbox == False:
    print("My guess is that you are thinking of a paper clip.")
elif is_mineral and bigger_than_breadbox == True:
    print("My guess is that you are thinking of a Camaro.")
