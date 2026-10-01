robot_location = 40
ball_location = 45
goal_location = 30
have_ball = False
forward_distance = 0
backward_distance = 0

if robot_location < ball_location:
    print("Almost at the ball")

if robot_location > goal_location:
    print("You are beyond the goal.")

if robot_location == goal_location:
    print("The robot is at the goal.")

forward_distance += 5

if forward_distance > 0:
    print(f"Moving forward {forward_distance}")
    robot_location += forward_distance
    forward_distance = 0
elif backward_distance > 0:
    print(f"Moving back {backward_distance}")
    robot_location -= backward_distance
    backward_distance = 0

if robot_location == goal_location:
    print("At the goal.")

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

backward_distance += 15

if forward_distance > 0:
    print(f"Moving forward {forward_distance}")
    robot_location += forward_distance
    forward_distance = 0
elif backward_distance > 0:
    print(f"Moving back {backward_distance}")
    robot_location -= backward_distance
    backward_distance = 0


if robot_location < goal_location:
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    print("You reached the goal and scored! ")
    have_ball = False

    # 1 
    #The if statement checks if the condition is true, and if it is, then it will run the code inside of the if statement.
    #if it is false, then it will skip the code inside of the statement.

    # 2
    # It's so whoever is reading the code can see what is in and not inside of a if statement. You can tell if code is inside an if branch if it has a indent before it. If it isn't,
    # then the code is not inside of the if statement.

    # 3
    # in the code

    # 4
    # += and -= adds or subtracts the variable by the value and stores that as the new value of the variable.
