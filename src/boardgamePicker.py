import json
import os

with open("./gamesList.json", "r") as json_file:
    game_data = json.load(json_file)

games = game_data["boardgames"]

# thank you Google
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def quitting(user_input):
    return user_input.lower() == "quit" or user_input.lower() == "q"


def titleBanner():
    print('''
    
    
    ░░░░░░   ░░░░░░   ░░░░░  ░░░░░░  ░░░░░░   ░░░░░░   ░░░░░  ░░░    ░░░ ░░░░░░░     ░░░░░░  ░░  ░░░░░░ ░░   ░░ ░░░░░░░ ░░░░░░  
    ▒▒   ▒▒ ▒▒    ▒▒ ▒▒   ▒▒ ▒▒   ▒▒ ▒▒   ▒▒ ▒▒       ▒▒   ▒▒ ▒▒▒▒  ▒▒▒▒ ▒▒          ▒▒   ▒▒ ▒▒ ▒▒      ▒▒  ▒▒  ▒▒      ▒▒   ▒▒ 
    ▒▒▒▒▒▒  ▒▒    ▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒  ▒▒   ▒▒ ▒▒   ▒▒▒ ▒▒▒▒▒▒▒ ▒▒ ▒▒▒▒ ▒▒ ▒▒▒▒▒       ▒▒▒▒▒▒  ▒▒ ▒▒      ▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒  
    ▓▓   ▓▓ ▓▓    ▓▓ ▓▓   ▓▓ ▓▓   ▓▓ ▓▓   ▓▓ ▓▓    ▓▓ ▓▓   ▓▓ ▓▓  ▓▓  ▓▓ ▓▓          ▓▓      ▓▓ ▓▓      ▓▓  ▓▓  ▓▓      ▓▓   ▓▓ 
    ██████   ██████  ██   ██ ██   ██ ██████   ██████  ██   ██ ██      ██ ███████     ██      ██  ██████ ██   ██ ███████ ██   ██ 


    ''')


def welcomeScreen():

    clear_screen()

    print('''
    █▓▒▒░░░ Welcome to The Boardgame Picker! ░░░▒▒▓█

    It's Game Night! Need some help picking a game? Maybe after something new?

    This app is designed to give you some tabletop game suggestions, after answering a few short questions.


    Instructions:

        1. Choose the number of players.

        2. Select the game duration.

        3. Pick a genre.

        4. Get results!
    

    You can quit the application at any stage by entering 'q' or 'quit'.


    Now, let's find a game to play!
    ''')


def getNumberOfPlayers():

    titleBanner()

    while True: 

        # receive user answer for number of players
        answer = input('''\nHow many people are playing?
        
\t[1] One Player
\t[2] Two Players
\t[3] Three or more Players

Your Answer: ''')

        if quitting(answer):
            quit()

        errorMessage = "\nInvalid input. Please choose 1, 2, or 3.\n"

        try:
            # try converting to int
            num_players = int(answer)

            # check if num_players is a valid choice
            if (num_players == 1) or (num_players == 2):
                return str(num_players)
            elif (num_players == 3):
                return "3+" 
            else:
                print(errorMessage)

        except ValueError:
            print(errorMessage)


def getGameDuration():

    clear_screen()

    titleBanner()

    while True: 

        # receive user answer for game duration
        answer = input('''How long would you like the game to go?
        
\t[1] Short (under 1 hour)
\t[2] Long (over 1 hour)

Your Answer: ''')

        if quitting(answer):
            quit()
    
        errorMessage = "\nInvalid input. Please choose 1 or 2.\n"
    
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


def getGameGenre(players, duration):

    clear_screen()

    titleBanner()
    
    filteredGames = filter(lambda game: players in game["players"] and duration in game["duration"], games)

    # convert genre values from dictionary to list of games
    filteredGenres = map(lambda item: item["genre"], list(filteredGames))

    # convert list of genres into set to remove duplicates
    genres = list(set(filteredGenres))
    genres.sort()

    genreList = ""
    for x in range(len(genres)):
        genreList = genreList + f"\t[{x + 1}] {genres[x]}\n"

    while True: 

        # receive user answer for game genre preference
        answer = input(f'''What game genre would you like to play?

{genreList}
Your Answer: ''')

        if quitting(answer):
            quit()
    
        errorMessage = "\nInvalid input. Please choose a number from the options available.\n"

        try:
            # convert to int
            userGenre = int(answer)

            # check if userGenre is a valid choice
            if (userGenre-1) in range(len(genres)):
                return genres[userGenre-1]
            else:
                print(errorMessage)

        except ValueError:
            print(errorMessage)


def getGameRecs(players, duration, genre):
    
    filteredGames = filter(lambda game: players in game["players"] and duration in game["duration"] and genre == game["genre"], games)

    gamesList = list(filteredGames)

    sortedList = sorted(gamesList, key=lambda x: x["name"])

    # prints final game suggestions!
    for x in sortedList:
        print(f'''
        
         █▓▒▒░░░ {x['name']} ░░░▒▒▓█

         Description: {x['description']}
                
        ''')


def runApp():

    welcomeScreen()

    while True:
        # program starts here
        user_players = getNumberOfPlayers()

        user_duration = getGameDuration()

        user_genre = getGameGenre(user_players, user_duration)
        print(f"\nGreat! Here are some {user_duration} {user_players} player games in the {user_genre} genre you can play!\n")

        getGameRecs(user_players, user_duration, user_genre)
        print()

        # loop to ask user if they would like to restart
        while True:
            ask_restart = (input("Would you like to start again? (Y/N)\n")).upper()

            if ask_restart == "N":
                print("See you next time!\n")
                quit()
            elif ask_restart != "Y":
                print("Invalid input. Please enter Y or N.\n")
            else:
                clear_screen()
                break


runApp()