import json

with open("gamesList.json", "r") as json_file:
    game_data = json.load(json_file)

user_duration = ""

user_genre = ""

def inputNumberOfPlayers():
    valid = False

    while not valid: 

        # Receive user answer for number of players
        answer = input('''How many people are playing?
        
        [1] One Player
        [2] Two Players
        [3] Three or more Players

Your Answer: ''')
    
        errorMessage = "Invalid input. Please choose 1, 2, or 3.\n"

        try:
            # try converting to int
            num_players = int(answer)
        except ValueError:
            print(errorMessage)
            continue

        if (num_players != 1) and (num_players != 2) and (num_players != 3):
            print(errorMessage)
        else:
            valid = True
            return num_players


user_players = inputNumberOfPlayers()
print(user_players)
