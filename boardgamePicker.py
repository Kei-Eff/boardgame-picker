import json

with open("gamesList.json", "r") as json_file:
    game_data = json.load(json_file)

user_genre = ""

def inputNumberOfPlayers():
    while True: 

        # receive user answer for number of players
        answer = input('''How many people are playing?
        
        [1] One Player
        [2] Two Players
        [3] Three or more Players

Your Answer: ''')
    
        errorMessage = "Invalid input. Please choose 1, 2, or 3.\n"

        try:
            # try converting to int
            num_players = int(answer)

            # check if num_players is a valid choice
            if (num_players != 1) and (num_players != 2) and (num_players != 3):
                # it's not valid, so print error message
                print(errorMessage)
            else:
                # it's valid, return the value
                return num_players

        except ValueError:
            print(errorMessage)



def inputGameDuration():
    while True: 

        # receive user answer for game duration
        answer = input('''How long would you like the game to go?
        
        [1] Short (under 1 hour)
        [2] Long (over 1 hour)

Your Answer: ''')
    
        errorMessage = "Invalid input. Please choose 1 or 2.\n"

        try:
            # try converting to int
            duration = int(answer)

            if (duration == 1):
                return "short"
            elif (duration == 2):
                return "long"                      
            else:
                print(errorMessage)

        except ValueError:
            print(errorMessage)     



user_players = inputNumberOfPlayers()
print(f"Number of players: {user_players}\n\n")

user_duration = inputGameDuration()
print(f"You want to play a {user_duration} game.")