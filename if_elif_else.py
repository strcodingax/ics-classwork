team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
if team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")

# 1
# it is happening because team a won the game, and so team_a_wins went from 15 to 16, which is the same as team_b_wins,
# so when the if statement comparing the amount of wins happened, it printed out the line:
# "Both Teams A and B have the same number of wins."

# 2
# elif checks if team b has more wins or points than team a, while else is there for when neither are true, and prints the last remaining possibility, that 
# being a tie.
 
# 3
# I changed the elif for line 18, which checks if team_b_wins is greater than team_a_wins into a if, and the difference is that it will run 
# regardless of whether or not team_a had more wins, because the elif would have just skipped it if the line 16's if returned true and printed the line.
