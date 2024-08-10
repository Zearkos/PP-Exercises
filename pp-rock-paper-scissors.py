play="y"
while True:
    play = str(input("Would you like to play?  Y/N "))
    if play.capitalize() == "Y":
        break
    else:
        quit()
player_one = "X"
while player_one != "Rock" or player_one != "Paper" or player_one != "Scissors":
    player_one = str(input(f"Player One: Choose Rock, Paper, or Scissors: "))
    if player_one.capitalize() == "Rock" or "Paper" or "Scissors":
         break     
    else:
        print("Please choose Rock, Paper, or Scissors.")
        continue
player_two = "X"
while player_two != "Rock" or player_two != "Paper" or player_two != "Scissors":
    player_two = str(input(f"Player Two: Choose Rock, Paper, or Scissors: "))
    if player_two.capitalize() == "Rock" or "Paper" or "Scissors":
         break     
    else:
        print("Please choose Rock, Paper, or Scissors.")
        continue

