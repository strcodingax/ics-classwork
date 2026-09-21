#This stores the name of the team.
team = "Toronto Blue Jays"
#This stores the "current" date.
current_date = "July 18, 2021"
#This stores the name of the player.
player = "Vladimir Guerrero Jr."
#This stores the number of home runs the player has hit to date.
home_runs_to_date = 31
#This stores the number of games the player has played to date.
games_played = 88
#This stores the total number of games in the season.
total_season_games = 162
#This stores the MLB record for most home runs in a season.
home_run_record = 73

#This calculates the number of games remaining in the season by subtracting the number of games played from the total number of games in the season.
games_remaining = total_season_games - games_played
#This calculates his average number of home runs per game by dividing the number of home runs to date by the number of games played.
home_runs_per_game = home_runs_to_date / games_played
#This calculates the projected number of home runs he will hit in the season by multiplying his average number of home runs per game by the total number of games in the season.
projected_home_runs = home_runs_per_game * total_season_games
#This checks if the projected number of home runs is greater than the current home run record and stores the result in the variable.
can_break_record = projected_home_runs > home_run_record

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {round((home_runs_per_game), 2)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round((projected_home_runs), 2)} home runs this season.")

