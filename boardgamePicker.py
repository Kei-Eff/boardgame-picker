import json

with open("gamesList.json", "r") as json_file:
    game_data = json.load(json_file)

games = game_data["boardgames"]

def quitting(user_input):
    return user_input.lower() == "quit" or user_input.lower() == "q"


def welcomeScreen():
    print('''
        Welcome to...

        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        ██░▄▄▀██░▄▄▄░█░▄▄▀██░▄▄▀██░▄▄▀██░▄▄░█░▄▄▀██░▄▀▄░██░▄▄▄████░▄▄░█▄░▄██░▄▄▀██░█▀▄██░▄▄▄██░▄▄▀██
        ██░▄▄▀██░███░█░▀▀░██░▀▀▄██░██░██░█▀▀█░▀▀░██░█░█░██░▄▄▄████░▀▀░██░███░█████░▄▀███░▄▄▄██░▀▀▄██
        ██░▀▀░██░▀▀▀░█░██░██░██░██░▀▀░██░▀▀▄█░██░██░███░██░▀▀▀████░████▀░▀██░▀▀▄██░██░██░▀▀▀██░██░██
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀


    ''')



def getNumberOfPlayers():
    while True: 

        # receive user answer for number of players
        answer = input('''\n\tHow many people are playing?
        
        [1] One Player
        [2] Two Players
        [3] Three or more Players

\tYour Answer: ''')

        if quitting(answer):
            quit()

        errorMessage = "\n\tInvalid input. Please choose 1, 2, or 3.\n"

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
    while True: 

        # receive user answer for game duration
        answer = input('''\tHow long would you like the game to go?
        
        [1] Short (under 1 hour)
        [2] Long (over 1 hour)

\tYour Answer: ''')

        if quitting(answer):
            quit()
    
        errorMessage = "\n\tInvalid input. Please choose 1 or 2.\n"
    
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
        answer = input(f'''\tWhat kind of game would you like to play?

    {genreList}        
\tYour Answer: ''')

        if quitting(answer):
            quit()
    
        errorMessage = "\n\tInvalid input. Please choose a number from the options available.\n"

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

    filteredGames = filter(lambda game: players in game["players"] and duration in game["duration"] and genre in game["genre"], games)

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
        print(f"\n\tNumber of players: {user_players}\n")

        user_duration = getGameDuration()
        print(f"\n\tCool! Let's look for a {user_duration} game to play.\n")

        user_genre = getGameGenre(user_players, user_duration)
        print(f"\n\tAwesome! Here are some {user_duration} {user_players} player games in the {user_genre} genre you can play!\n")

        getGameRecs(user_players, user_duration, user_genre)
        print()

        # loop to ask user if they would like to restart
        while True:
            ask_restart = (input("\tWould you like to try again? (Y/N)\n\t")).upper()

            if ask_restart == "N":
                print("\tSee you next time!\n")
                quit()
            elif ask_restart != "Y":
                print("\tInvalid input. Please enter Y or N.\n")
            else:
                break


runApp()